from langchain_ollama import ChatOllama
def get_ollama_model(
    model: str = "llama3.1:8b",
    temperature: float = 0.0,
) -> ChatOllama:
    """
    Returns a configured ChatOllama instance.

    Args:
        model: Ollama model name.
        temperature: Sampling temperature.

    Returns:
        ChatOllama: Configured LLM.
    """
    return ChatOllama(
        model=model,
        temperature=temperature,
    )