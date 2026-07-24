from langchain_core.prompts import ChatPromptTemplate
from parsers.feedback_parser import get_feedback_parser

parser = get_feedback_parser()

feedback_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert coding interviewer.

Evaluate the candidate's solution.

Score it fairly.

{format_instructions}
            """
        ),
        (
            "human",
            """
Question:

{question}

Candidate Solution:

{solution}
            """
        )
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)