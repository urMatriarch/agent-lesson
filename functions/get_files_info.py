import os

def get_files_info(working_directory, directory="."):
    working_path = os.path.join(working_directory, directory)
    
    try:
        test_path = os.path.abspath(working_path)
    except:
        return(f"Error: Cannot create an absolute path using {working_path}. Please check inputs and try again.")
    if working_directory in test_path:
        pass
    else:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if os.path.isdir(working_path) == False:
        return(f'Error: "{directory}" is not a directory')
    
    try:
        directory_list = os.listdir(working_path)
    except:
        return(f"Error: Cannot list the contents of the following directory: {working_path}. Please check inputs and try again.")
    string_list = []
    for item in directory_list:
        item_path = os.path.join(working_path, item)
        string_list.append(f'- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}')
    
    return ("\n".join(string_list))