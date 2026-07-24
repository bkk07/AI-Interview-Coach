from langchain_core.output_parsers import PydanticOutputParser
from models.question import Question

def get_pydantic_parser():
    return PydanticOutputParser(
    pydantic_object=Question
)


