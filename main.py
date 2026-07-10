import os
from dotenv import load_dotenv
import sys
import anthropic
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file 
from call_function import call_function 

def main():
    load_dotenv()
    api_key = os.environ.get("CLAUDE_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read the contents of a file
    - Write to a file (create or update)
    - Run a Python file with optional arguments 

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    if len(sys.argv) < 2:
        print("Please provide a prompt as a command-line argument.")
        return
    
    verbose_mode = False
    if len(sys.argv) == 3 and sys.argv[2]=="--verbose":
        verbose_mode = True
        
    prompt = sys.argv[1] # sys.argv is a list of command-line arguments

    messages=[
            {"role": "user", "content": prompt}
        ]
    
    max_iters = 20

    for i in range(0, max_iters): 

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=system_prompt,
            tools=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file ],
            messages=messages
        )

        if response is None or response.usage is None:
            print("Response or usage metadata is None. Response is malformed.")
            return 
        
        if verbose_mode:
            print(f"Prompt: {prompt}")
            print(f"Prompt tokens: {response.usage.input_tokens}")
            print(f"Response tokens: {response.usage.output_tokens}")

        tool_calls = [block for block in response.content if block.type == "tool_use"]
        if tool_calls:
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for tool_call in tool_calls:
                result = call_function(function_call_part=tool_call)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tool_call.id,
                    "content": result
                })
            messages.append({"role": "user", "content": tool_results})

        else:
            print(response.content[0].text)
            return  # Exit the loop if no tool calls are made
    
main()