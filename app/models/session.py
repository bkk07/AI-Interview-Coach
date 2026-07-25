from pydantic import BaseModel

from models.question import Question
from models.feedback import Feedback


class InterviewRound(BaseModel):
    question: Question
    answer: str
    feedback: Feedback


class InterviewSession(BaseModel):
    rounds: list[InterviewRound] = []