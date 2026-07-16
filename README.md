# AI Coding Agent

A small command-line AI agent built on the Anthropic (Claude) API. It takes a
natural-language prompt, plans out tool calls, and uses a set of file-system
and code-execution functions to explore and modify a sandboxed working
directory in order to satisfy the request.

## How it works

`main.py` sends the user's prompt to Claude along with a system prompt and a
set of available tools. Claude responds with either a text answer or one or
more tool calls. Tool calls are dispatched by `call_function.py` to the
matching function in `functions/`, and their results are fed back to Claude.
This loop repeats (up to 20 iterations) until Claude replies with a final
text answer instead of a tool call.

All file operations are sandboxed to a single working directory (currently
`calculator/`, set in `call_function.py`) — any path that resolves outside of
it is rejected.

## Available tools

- **get_files_info** — list files/directories in a given directory, with size and type.
- **get_file_content** — read a file's contents (truncated to `MAX_CHARS`, see `config.py`).
- **write_file** — create or overwrite a file, creating parent directories as needed.
- **run_python_file** — run a `.py` file with `python3`, optionally passing CLI arguments.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency
management.

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Create a `.env` file in the project root with your Anthropic API key:
   ```
   CLAUDE_API_KEY=your-api-key-here
   ```

## Usage

```bash
uv run main.py "your prompt here"
```

Add `--verbose` to also print prompt/response token usage:

```bash
uv run main.py "your prompt here" --verbose
```

## Project structure

```
main.py              # entry point: runs the Claude agent loop
call_function.py     # dispatches Claude tool calls to the functions/ implementations
config.py            # shared config (e.g. MAX_CHARS for file reads)
functions/            # tool implementations + their Claude schemas
tests.py              # manual/ad-hoc tests for the functions
calculator/           # sample sandboxed project the agent operates on
```
