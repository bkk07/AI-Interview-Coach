from pydantic import BaseModel, Field

class Feedback(BaseModel):
    score: int = Field(
        ...,
        ge=0,
        le=10,
        description="Overall score out of 10."
    )

    correctness: str = Field(
        ...,
        description="Whether the approach is correct."
    )

    strengths: list[str] = Field(
        ...,
        description="Things the candidate did well."
    )

    improvements: list[str] = Field(
        ...,
        description="Suggestions for improvement."
    )

    final_feedback: str = Field(
        ...,
        description="Overall summary."
    )