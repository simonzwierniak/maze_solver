import os
from google import genai
from dotenv import load_dotenv
import sys


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) > 1:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=" ".join(sys.argv[1:]),
        )
    else:
        sys.exit(1)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()