from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os
from dotenv import load_dotenv

# Load variables from .env file into os.environ
load_dotenv()

# Read the endpoint from the environment
endpoint = os.getenv("PROJECT_ENDPOINT")
if not endpoint:
    raise ValueError("PROJECT_ENDPOINT environment variable is missing or empty.")

# Azure Foundry
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=endpoint
)

# Creating a chat client
# openai_client = project_client.get_openai_client(api_version="2024-10-21")
# You can then use this chat client object to submit prompts to models and return responses.