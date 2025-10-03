import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from config import system_prompt

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    try:
        prompt = sys.argv[1]
    except:
        print("Error! No prompt provided! Please provide a prompt a try again!")
        sys.exit(1)

    additional_args = []
    try:
        for i in range(2, len(sys.argv)):
            additional_args.append(sys.argv[i])
    except:
        additional_args = []

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
       model="gemini-2.0-flash-001", 
       contents=messages,
       config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    if "--verbose" in additional_args:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response: ")
    print(response.text)


if __name__ == "__main__":
    main()
