# Calculator App

A command-line calculator application that evaluates mathematical expressions with support for basic arithmetic operations (+, -, *, /) and proper operator precedence.

## Features

- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), and Division (/)
- **Operator Precedence**: Correctly handles operator precedence (multiplication and division before addition and subtraction)
- **Infix Expression Evaluation**: Evaluates expressions written in standard infix notation
- **JSON Output**: Returns results in a clean JSON format
- **Error Handling**: Provides clear error messages for invalid expressions

## Installation

No external dependencies required. This project uses only Python's built-in libraries.

### Requirements
- Python 3.7+

## Usage

Run the calculator from the command line:

```bash
python main.py "<expression>"
```

### Examples

```bash
# Simple addition
python main.py "3 + 5"
# Output: {"expression": "3 + 5", "result": 8}

# With operator precedence
python main.py "2 * 3 + 5"
# Output: {"expression": "2 * 3 + 5", "result": 11}

# Complex expression
python main.py "2 * 3 - 8 / 2 + 5"
# Output: {"expression": "2 * 3 - 8 / 2 + 5", "result": 7}

# Decimal results
python main.py "10 / 3"
# Output: {"expression": "10 / 3", "result": 3.3333333333333335}
```

### Expression Format

- Numbers must be separated by spaces
- Operators must be separated by spaces
- Supported operators: `+`, `-`, `*`, `/`

Example valid expression: `3 + 5 * 2` (evaluates to 13, not 16)

## Project Structure

```
.
├── main.py              # Entry point for the calculator application
├── tests.py             # Unit tests for the calculator
├── pkg/
│   ├── calculator.py    # Core Calculator class implementing expression evaluation
│   └── render.py        # JSON output formatting utilities
└── README.md            # This file
```

## How It Works

The calculator uses the **Shunting Yard Algorithm** to evaluate infix expressions:

1. **Tokenization**: Splits the input expression by spaces
2. **Operator Precedence Handling**: Uses a stack-based approach to respect operator precedence
3. **Expression Evaluation**: Applies operators to operands in the correct order
4. **Result Formatting**: Converts the result to JSON format

### Algorithm Details

- Maintains two stacks: one for values and one for operators
- Processes each token from left to right
- Applies operators when a lower-precedence operator is encountered
- Ensures all remaining operators are applied after all tokens are processed

## Testing

Run the test suite using:

```bash
python -m unittest tests.py -v
```

### Test Coverage

The test suite includes:
- Basic operations (addition, subtraction, multiplication, division)
- Nested expressions with mixed operators
- Complex multi-operation expressions
- Edge cases (empty expressions)
- Error cases (invalid operators, insufficient operands)

## Error Handling

The calculator provides clear error messages for:
- **Invalid tokens**: Non-numeric, non-operator values
- **Invalid operators**: Unsupported operator symbols
- **Insufficient operands**: Not enough numbers for an operation
- **Empty expressions**: Missing or whitespace-only input

## License

This project is open source and available for educational purposes.
