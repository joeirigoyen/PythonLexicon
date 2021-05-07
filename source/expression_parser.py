"""Program that reads a .txt file containing s-expressions and turns them into regexps. 

Author: Youthan Irigoyen"""
import re
import stack


# Create empty stack
curr_stack = stack.Stack()

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
key_elems = {'$': r'[0-9]',
             '?': r'[a-zA-Z]',
             '%': r'[a-zA-Z0-9]',
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
    if sexp != None:
        new_line = r""
        for c in sexp:
            if c != ')' and c != '(':
                try:
                    new_line += key_elems[c]
                except KeyError:
                    new_line += c
        print(new_line)
        return new_line


# Pass list to string
def to_string(l: list):
    string = ""
    for elem in l:
        string += elem
    return string


# Group by or
def group_or(args):
    string = ""
    for i in range(len(args)):
        if i + 1 != len(args):
            string += args[i] + '|'
        else:
            string += args[i]
    return string


# Group arguments
def group_args(args: list):
    string = "("
    args.reverse()
    for arg in args:
        string += arg
    string += ")"
    return string


def get_sequence(args: list):
    string = ""
    args.reverse()
    for arg in args:
        string += arg
    return string


def operate():
    global curr_stack
    arguments = []
    while True:
        if not curr_stack.is_empty():
            p = curr_stack.pop()
        else:
            break
        if p == '*' or p == '+':
            arguments.append(p)
            curr_stack.push("".join(arguments))
            break
        if p == '¬':
            curr_stack.push(group_args(arguments))
            break
        if p == '&':
            curr_stack.push(get_sequence(arguments))
            break
        if p == '|':
            curr_stack.push(group_or(arguments))
            break
        else:
            arguments.append(p)


# Process line by word
def read_line(line: str):
    global curr_stack
    curr_stack.flush()
    # Iterate over line
    for word in re.split(r'\(| ', line):
        word = word.strip()
        # If word is a keyword
        if ')' not in word and len(word) > 0:
            # Add full word to stack
            curr_stack.push(word)
        # If word contains ')'
        elif ')' in word:
            # Pop from stack until operator is found
            operate()
    return curr_stack.peek()


# Read file
def get_regexs(filename: str):
    regexs = []
    # Open file
    f = open(filename)
    # Get lines
    lines = f.readlines()
    # Evaluate lines
    for line in lines:
        line = line.replace('Â', '')
        new_line = read_line(line)
        new_regex = to_regex_notation(new_line)
        regexs.append(new_regex)
    return regexs
