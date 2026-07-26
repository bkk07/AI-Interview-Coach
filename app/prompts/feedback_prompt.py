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
7. Evaluate only what is explicitly present in the candidate answer.
8. Do not assume, invent, or infer code, algorithms, complexity, or edge cases that the candidate did not write.
9. If the candidate answer is empty or only whitespace, the score must be 0 and the strengths must say that no answer was submitted.

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
