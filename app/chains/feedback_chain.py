from llm.ollama_client import get_ollama_model
from prompts.feedback_prompt import feedback_prompt
from parsers.feedback_parser import get_feedback_parser

llm = get_ollama_model()
parser = get_feedback_parser()

feedback_chain = feedback_prompt | llm | parser

