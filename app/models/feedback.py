from pydantic import BaseModel, Field


class Feedback(BaseModel):
    """
    Represents the evaluation of a candidate's answer.
    """

    score: int = Field(
        ...,
        ge=0,
        le=10,
        description="Overall score out of 10."
    )

    strengths: list[str] = Field(
        ...,
        description="Things the candidate did well."
    )

    weaknesses: list[str] = Field(
        ...,
        description="Things the candidate should improve."
    )

    missing_concepts: list[str] = Field(
        ...,
        description="Important concepts missing from the answer."
    )

    ideal_answer: str = Field(
        ...,
        description="A concise ideal answer."
    )

    improvement_suggestions: list[str] = Field(
        ...,
        description="Actionable suggestions to improve."
    )