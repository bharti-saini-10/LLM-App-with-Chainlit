from openai import AzureOpenAI
from src.prompt import system_instruction
import os 

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT = os.getenv("OPENAI_AZURE_ENDPOINT") 
AZURE_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
AZURE_OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")  
AZURE_OPENAI_DEPLOYMENT = os.getenv("OPENAI_DEPLOYMENT_NAME")  
USER_ID = os.getenv("USER_ID")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION, 
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    default_headers={"User-Id": USER_ID}
)

messages=[
    {"role": "system", "content": system_instruction}
]

def ask_order(messages, temperature=0):
    response = client.chat.completions.create(
        model = AZURE_OPENAI_DEPLOYMENT,
        messages=messages,
        temperature=temperature
    )
    
    return response.choices[0].message.content