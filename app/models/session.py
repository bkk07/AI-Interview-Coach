from pydantic import BaseModel, Field

from models.question import Question
from models.feedback import Feedback


class InterviewRound(BaseModel):
    question: Question
    answer: str
    feedback: Feedback


class InterviewSession(BaseModel):
    difficulty: str
    company: str
    rounds: list[InterviewRound] = Field(default_factory=list)