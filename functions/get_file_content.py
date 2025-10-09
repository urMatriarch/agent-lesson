import os
from config import MAX_CHARS
from google import genai
from google.genai import types

def get_file_content(working_directory, file_path):
    working_path = os.path.join(working_directory, file_path)

    file_path_abs = os.path.abspath(working_path)
    if working_directory in file_path_abs:
        pass
    else:
        return(f"Error: Cannot read '{file_path}' as it is outsde the permitted working directory.")
    
    if os.path.isfile(working_path):
        pass
    else:
        return(f'Error: File not found or is not a regular file: "{file_path}"')
    
    try:
        with open(working_path) as f:
            content_string = f.read(MAX_CHARS)
            if len(content_string) >= 10000:
                content_string = content_string + f'[...File "{file_path}" truncated at 10000 characters]'
    except:
        return(f'Error: Unable to open and read the file: "{file_path}"')
    
    return content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Displays the content of files, truncated to a configurable number of characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be read, relative to the working directory.",
            ),
        },
    ),
)