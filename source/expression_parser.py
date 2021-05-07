"""Program that reads a .txt file containing s-expressions and turns them into regexps. 

Author: Youthan Irigoyen"""
import re
import stack


# Keywords
keywords = {"def": "def",
            "if": "if",
            "for": "for",
            "else": "else",
            "break": "break",
            "continue": "continue",
            "while": "while",
            "import": "import",
            "from": "from",
            "is": "is",
            "and": "and",
            "or": "or",
            "as": "as",
            "assert": "assert",
            "class": "class",
            "del": "del",
            "elif": "elif",
            "except": "except",
            "False": "false",
            "True": "True",
            "finally": "finally",
            "global": "global",
            "in": "in",
            "lambda": "lambda",
            "None": "None",
            "nonlocal": "nonlocal",
            "not": "not",
            "raise": "raise",
            "return": "return",
            "try": "try",
            "with": "with",
            "yield": "yield",
            "pass": "pass"}

# Replaceable elements
key_elems = {'$': r'0-9',
             '?': r'a-zA-Z',
             '%': r'a-zA-Z0-9',
             '-': r'\s',
             'L': r'\(',
             'R': r'\)',
             '4': r'{4}',
             ':': r'\*',
             '~': r'\+',
             '°': r'\.',
             ';': r'\S'
            }

# Operators
operators = ['*', '+', '4', '|', '¬']


# Rewrite symbols in regex notation
def to_regex_notation(sexp: str):
    new_line = r""
    for c in sexp:
        if c != ')' and c != '(':
            try:
                new_line += key_elems[c]
            except KeyError:
                new_line += c
    return new_line


# Convert list elements to a string
def to_string(l: list):
    string = ""
    for elem in l:
        string += elem
    return string


# Test function
def test_func(s: stack.Stack):
    # Variable list
    variables = []
    # If stack is still not empty
    while not s.is_empty():
        # Get top element from stack
        p = s.pop()
        # If top element is an operator
        if p in operators:
            # If operator is *
            if p == '*':
                variables.extend(p)
            break
        else:
            variables.extend(p)
    print(variables)


# Process line by word
def process_line(line: str):
    # Create empty stack
    curr_stack = stack.Stack()
    # Iterate over line
    for word in re.split(r'\(| ', line):
        # If word is a keyword
        if word.strip() in keywords:
            # Add full word to stack
            curr_stack.push(word)
        elif ')' not in word.strip():
            # Add full word to stack
            curr_stack.push(word)
        print(curr_stack)


# Read file
def read_file(filename: str):
    # Open file
    f = open(filename)
    # Get lines
    lines = f.readlines()
    # Evaluate lines
    for line in lines:
        line = line.replace('Â', '')
        process_line(line)


# Main execution
read_file(r"PythonLexicon\source\expressions.txt")