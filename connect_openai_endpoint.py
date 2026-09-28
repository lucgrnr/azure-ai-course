from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import os
from dotenv import load_dotenv

# Load variables from .env file into os.environ
load_dotenv()

# Read the endpoint from the environment
endpoint = os.getenv("OPENAI_ENDPOINT")
if not endpoint:
    raise ValueError("OPENAI_ENDPOINT environment variable is missing or empty.")


token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

openai_client = OpenAI(  
  base_url = endpoint,  
  api_key=token_provider,
)

"""
In addition to Microsoft Entra ID (recommended), you can authenticate using an API key or environment variables.

API key authentication:

Python
import os
from openai import OpenAI

openai_client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url="https://{resource-name}.openai.azure.com/openai/v1/"
)

Important
Use API keys with caution. Store them securely in Azure Key Vault and never include them directly in your code.

Environment variables:
If you set OPENAI_BASE_URL and OPENAI_API_KEY environment variables, the client uses them automatically:

Python
from openai import OpenAI

openai_client = OpenAI()  # Uses environment variables
"""