import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    working_file_path = os.path.join(working_directory, file_path)

    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(working_file_path)
    if not abs_file_path.startswith(abs_working_directory):
        return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    
    if os.path.exists(working_file_path):
        pass
    else:
        return(f'Error: File "{file_path}" not found.')
    
    if file_path.endswith('.py'):
        pass
    else:
        return(f'Error: "{file_path}" is not a Python file.')
    
    python_file_stdout = ""
    python_file_stderr = ""
    python_file_args = ["python", abs_file_path]  
    for arg in args:
        python_file_args.append(arg)
    result = subprocess.run(
        python_file_args,
        capture_output=True,
        text=True,
        timeout=30,
        cwd=abs_working_directory
    )  

    python_file_output = []
    if result.stdout:
        python_file_output.append(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        python_file_output.append(f"STDERR:\n{result.stderr}")

    if result.returncode != 0:
        python_file_output.append(f"Process exited with code {result.returncode}")

    return "\n".join(python_file_output) if python_file_output else "No output produced."

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file or outputs an error, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the python file to be run relative to the working directory.",
            ),
        },
    ),
)
