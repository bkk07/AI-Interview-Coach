from langchain_core.output_parsers import PydanticOutputParser
from models.feedback import Feedback


def get_feedback_parser():
    return PydanticOutputParser(
        pydantic_object=Feedback
    )