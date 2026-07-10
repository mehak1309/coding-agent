import os
from dotenv import load_dotenv
import sys
import anthropic
from functions.get_files_info import get_files_info
from functions.get_files_info import schema_get_files_info

def main():
    load_dotenv()
    api_key = os.environ.get("CLAUDE_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

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

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=system_prompt,
        tools=[schema_get_files_info],
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
        for tool_call in tool_calls:
            print(f"Calling function: {tool_call.name}({tool_call.input})")
    else:
        print(response.content[0].text)
    
main()
# print(get_files_info("calculator", "pkg"))