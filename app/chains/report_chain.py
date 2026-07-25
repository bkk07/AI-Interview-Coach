from llm.ollama_client import get_ollama_model
from prompts.report_prompt import report_prompt
from models.report import InterviewReport
from langchain_core.output_parsers import PydanticOutputParser

llm = get_ollama_model()

parser = PydanticOutputParser(
    pydantic_object=InterviewReport
)

report_chain = (
    report_prompt.partial(
        format_instructions=parser.get_format_instructions()
    )
    | llm
    | parser
)