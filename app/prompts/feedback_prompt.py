from langchain_core.prompts import ChatPromptTemplate
from parsers.feedback_parser import get_feedback_parser

parser = get_feedback_parser()

feedback_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert technical interviewer.

Evaluate the candidate's answer fairly.

Rules:

1. Score the answer from 0 to 10.
2. Mention strengths.
3. Mention weaknesses.
4. Mention missing concepts.
5. Give a concise ideal answer.
6. Give actionable improvement suggestions.

Return ONLY the following format.

{format_instructions}
"""
        ),
        (
            "human",
            """
Interview Question:

{question}


Candidate Answer:

{answer}
"""
        ),
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)