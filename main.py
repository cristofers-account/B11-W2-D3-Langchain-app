import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Check required API keys
required_keys = [
    "OPENAI_API_KEY",
    "LANGSMITH_API_KEY",
]

missing_keys = [
    key for key in required_keys
    if not os.getenv(key)
]

if missing_keys:
    print("ERROR: Missing required environment variable(s):")

    for key in missing_keys:
        print(f"  - {key}")

    print("\nPlease add the missing key(s) to your .env file.")
    raise SystemExit(1)


# Create the LangChain OpenAI chat model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# Get input from the user
user_input = input("Enter your prompt: ")


# Send the prompt through LangChain
response = llm.invoke(user_input)


# Print the model response
print("\nAI Response:")
print(response.content)