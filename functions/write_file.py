import os

def write_file(working_directory, file_path, content):
    working_file_path = os.path.join(working_directory, file_path)

    abs_file_path = os.path.abspath(working_file_path)
    if working_directory in abs_file_path:
        pass
    else:
        return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    if os.path.exists(os.path.split(working_file_path)[0]):
        pass
    else:
        try:
            os.makedirs(os.path.split(working_file_path)[0])
        except:
            return(f'Error: Unable to make path at "{file_path}" due to unknown error. Please check inputs and try again.')

    try:
        with open(working_file_path, "w") as f:
            f.write(content)
        return(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    except:
        return(f'Error: unable to write to "{file_path}" due to unknown error. Please check inputs and try again.')