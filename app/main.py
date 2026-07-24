from llm.ollama_client import get_ollama_model
from prompts.question_prompt import question_prompt
from parsers.pydantic_output_parser import get_pydantic_parser
from utils.display import display_feedback
from parsers.feedback_parser import get_feedback_parser
from chains.feedback_chain import feedback_chain



llm = get_ollama_model()
parser = get_pydantic_parser()

chain = question_prompt | llm | parser

question = chain.invoke(
    {
        "domain": "Graphs",
        "difficulty": "Easy",
        "round": "Microsoft",
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
