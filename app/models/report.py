from pydantic import BaseModel


class InterviewReport(BaseModel):
    overall_score: int
    summary: str
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]