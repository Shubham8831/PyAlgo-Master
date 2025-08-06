import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL

load_dotenv()
key = os.getenv("GROQ_API_KEY")



def return_model_client():
    model_client = OpenAIChatCompletionClient(
            base_url="https://api.groq.com/openai/v1",
            model=MODEL,
            api_key=key,
            model_info={
                "family": "llama",
                "vision": False,
                "function_calling": True,
                "json_output": True,
                "structured_output": True,      # ← new required field
            })
    return model_client

