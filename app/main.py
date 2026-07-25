from llm.ollama_client import get_ollama_model
from prompts.question_prompt import question_prompt
from parsers.pydantic_output_parser import get_pydantic_parser
from utils.display import display_feedback
from parsers.feedback_parser import get_feedback_parser
from chains.feedback_chain import feedback_chain

from models.session import InterviewRound, InterviewSession



llm = get_ollama_model()
parser = get_pydantic_parser()

chain = question_prompt | llm | parser
session = InterviewSession()


# Ask for the domain
print("Choose Domain")
print("1. Arrays")
print("2. Strings")
print("3. Graphs")
print("4. Trees")
print("5. Dynamic Programming")

choice = input("Enter choice: ")

domains = {
    "1": "Arrays",
    "2": "Strings",
    "3": "Graphs",
    "4": "Trees",
    "5": "Dynamic Programming",
}

domain = domains.get(choice)

if domain is None:
    print("Invalid choice")
    exit()


# Step 2 — Ask difficulty

print("\nChoose Difficulty")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter choice: ")


difficulties = {
    "1": "Easy",
    "2": "Medium",
    "3": "Hard",
}

difficulty = difficulties.get(choice)

if difficulty is None:
    print("Invalid choice")
    exit()


company = input("\nEnter Company: ")


question = chain.invoke(
    {
        "domain": domain,
        "difficulty": difficulty,
        "round": company,
    }
)
print(question.question_text)

print("Enter your answer (type END on a new line when finished):")

lines = []

while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)

answer = "\n".join(lines)

feedback = feedback_chain.invoke(
    {
        "question": question.question_text,
        "answer": answer,
    }
)
display_feedback(feedback)
round1 = InterviewRound(
    question=question,
    answer=answer,
    feedback=feedback,
)

session.rounds.append(round1)
print(session.model_dump_json(indent=4))