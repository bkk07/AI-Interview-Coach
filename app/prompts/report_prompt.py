from langchain_core.prompts import ChatPromptTemplate

report_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert technical interviewer.

You are given an interview session consisting of multiple interview rounds.

Analyze the overall performance and return:

- overall_score (0-100)
- summary
- strengths
- weaknesses
- recommendations

{format_instructions}
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
)