from langchain_core.prompts import ChatPromptTemplate
from parsers.pydantic_output_parser import get_pydantic_parser

parser = get_pydantic_parser()

question_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert Competitive Programming and Technical Interview Coach.

Generate ONE original coding interview question.

Rules:
1. Generate exactly one original problem.
2. Match the requested domain and difficulty.
3. Do NOT generate the solution or hints.
4. The output MUST follow the format below.

{format_instructions}
"""
        ),
        (
            "human",
            """
Domain: {domain}
Difficulty: {difficulty}
Interview Round: {round}
"""
        ),
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)