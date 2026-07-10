from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file  

working_directory = "calculator"

def call_function(function_call_part):
    print(f"Calling function: {function_call_part.name}({function_call_part.input})")

    result = ""
    if function_call_part.name == "get_files_info":
        result = get_files_info(working_directory, **function_call_part.input)
    elif function_call_part.name == "get_file_content":
        result = get_file_content(working_directory, **function_call_part.input)
    elif function_call_part.name == "write_file":
        result = write_file(working_directory, **function_call_part.input)
    elif function_call_part.name == "run_python_file":
        result = run_python_file(working_directory, **function_call_part.input)
    if result == "":
        return f"Unknown function '{function_call_part.name}' called with arguments: {function_call_part.input} "
    return f"Function '{function_call_part.name}' returned:\n{result}"