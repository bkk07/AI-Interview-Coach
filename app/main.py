from llm.ollama_client import get_ollama_model
from prompts.question_prompt import question_prompt
llm = get_ollama_model()
prompt = question_prompt.invoke(
    {
        "domain": "Graphs",
        "difficulty": "EASY",
        "round": "Microsoft"
    }
)
for chunck in llm.stream(prompt):
    print(chunck.content, end="", flush=True)