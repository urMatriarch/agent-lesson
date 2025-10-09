import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from config import system_prompt
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

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

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
       model="gemini-2.0-flash-001", 
       contents=messages,
       config=types.GenerateContentConfig(
           tools=[available_functions],
           system_instruction=system_prompt),
    )
    
    if "--verbose" in additional_args:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")


if __name__ == "__main__":
    main()
