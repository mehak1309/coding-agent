import os
from dotenv import load_dotenv
import sys
import anthropic
from functions.get_files_info import get_files_info

def main():
    load_dotenv()
    api_key = os.environ.get("CLAUDE_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)

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
        messages=messages
    )

    print(response.content[0].text)
    if response is None or response.usage is None:
        print("Response or usage metadata is None. Response is malformed.")
        return 
    
    if verbose_mode:
        print(f"Prompt: {prompt}")
        print(f"Prompt tokens: {response.usage.input_tokens}")
        print(f"Response tokens: {response.usage.output_tokens}")

main()
# print(get_files_info("calculator", "pkg"))