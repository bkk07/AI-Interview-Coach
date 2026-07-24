from pydantic import BaseModel, Field


class Question(BaseModel):
    """
    Represents a coding interview or competitive programming question.
    """

    domain: str = Field(
        ...,
        description="Primary topic of the question (e.g. Graphs, DP, Trees).",
    )

    difficulty: str = Field(
        ...,
        description="Difficulty level (Easy, Medium, Hard).",
    )

    round: str = Field(
        ...,
        description="Interview or contest round (Google L3, Amazon OA, Codeforces Div2).",
    )

    focus_area: str = Field(
        ...,
        description="Specific concept within the domain (BFS, DFS, Binary Search, DSU, etc.).",
    )

    question_text: str = Field(
        ...,
        description="Complete problem statement.",
    )