from llm.ollama_client import get_ollama_model
from prompts.question_prompt import question_prompt
from parsers.pydantic_output_parser import get_pydantic_parser

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
print(question)