from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableParallel
from pydantic import BaseModel, Field

from llm.ollama_client import get_ollama_model
from models.report import InterviewReport


class OverallAssessment(BaseModel):
    overall_score: int = Field(..., ge=0, le=100)
    summary: str


class ReportItems(BaseModel):
    items: list[str]


llm = get_ollama_model()

overall_parser = PydanticOutputParser(pydantic_object=OverallAssessment)
items_parser = PydanticOutputParser(pydantic_object=ReportItems)


def extract_json_text(output):
    text = output.content if hasattr(output, "content") else str(output)
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1 or end < start:
        return text

    return text[start : end + 1]


def build_report_prompt(task: str, format_instructions: str):
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
You are an expert technical interviewer.

Analyze the interview session and produce only this part of the final report:

{task}

Return ONLY the requested structured output.

{{format_instructions}}
                """,
            ),
            (
                "human",
                """
Interview Session:

{session}
                """,
            ),
        ]
    ).partial(format_instructions=format_instructions)


overall_chain = (
    build_report_prompt(
        "overall_score from 0 to 100 and a concise performance summary.",
        overall_parser.get_format_instructions(),
    )
    | llm
    | RunnableLambda(extract_json_text)
    | overall_parser
)

strengths_chain = (
    build_report_prompt(
        "a list of the candidate's main strengths.",
        items_parser.get_format_instructions(),
    )
    | llm
    | RunnableLambda(extract_json_text)
    | items_parser
)

weaknesses_chain = (
    build_report_prompt(
        "a list of the candidate's main weaknesses.",
        items_parser.get_format_instructions(),
    )
    | llm
    | RunnableLambda(extract_json_text)
    | items_parser
)

recommendations_chain = (
    build_report_prompt(
        "a list of actionable recommendations for improvement.",
        items_parser.get_format_instructions(),
    )
    | llm
    | RunnableLambda(extract_json_text)
    | items_parser
)


def merge_report(parts):
    overall = parts["overall"]

    return InterviewReport(
        overall_score=overall.overall_score,
        summary=overall.summary,
        strengths=parts["strengths"].items,
        weaknesses=parts["weaknesses"].items,
        recommendations=parts["recommendations"].items,
    )


report_chain = (
    RunnableParallel(
        overall=overall_chain,
        strengths=strengths_chain,
        weaknesses=weaknesses_chain,
        recommendations=recommendations_chain,
    )
    | RunnableLambda(merge_report)
)
