import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: '{file_path}' is not in the working directory."
    
    if not os.path.isfile(abs_file_path):
        return f"Error: '{file_path}' is not a file."
    
    if not file_path.endswith(".py"): 
        return f"Error: '{file_path}' is not a Python file."
    
    try:
        final_args = ["python3", file_path]
        final_args.extend(args)
        output = subprocess.run(final_args, timeout=30, capture_output=True, cwd=abs_working_dir)
        final_string = f"""
        STDOUT: {output.stdout}
        STDERR: {output.stderr}
        """

        if output.stdout == "" and output.stderr == "":
            final_string += "No output was produced by the Python file.\n"

        if output.returncode != 0:
            final_string += f"Process exited with code {output.returncode}"
        
        return final_string
    except Exception as e:
        return f"Error running Python file '{file_path}': {e}"
 

schema_run_python_file = {
    "name": "run_python_file",
    "description": "Runs a python file with the python3 interpreter. Accepts additional CLI args as an optional array. ",
    "input_schema": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The file to run, relative to the working directory. "
            },
            "args": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "An optional array of strings to be used as the CLI arguments for the Python file. "
            }
        },
        "required": ["file_path"]
    }
}