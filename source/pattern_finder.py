# Author: Raúl Youthan Irigoyen Osorio
import re

# Tokens
function_token = r"\s([a-zA-Z_][\w]*)\(.*\):"
call_token = r"([a-zA-Z_][\w]*)\([\w\W]*\)"
arg_token = r"[\(](\w+[,]*[\s\S][\w]+)\)"
string_token = r"([\"][^\"]*\")"
number_token = r"(^[0-9]*[\.]{0,1}[0-9]*)"
comment_token = r"(#.*)"
declare_token = r"(^[^0-9][\w]+)[\s\S]="
decorator_token = r"(@\S*)"
tab_token = r"(\s{4})"
escape_token = r"(\\[a-zA-Z])"

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


def found_regex(line, start, end, spanclass, token):
    return re.sub(token, "<span class=\"" + spanclass + "\">" + line[start:end] + "</span>", line)


def find_matches(line: str, token, spanclass):
    des_match = re.findall(token, line)
    if (des_match is not None):
        for i in des_match:
            line = found_regex(line, line.index(i), line.index(i) + len(i), spanclass, i)
    return line


def find_in_word(line, word: str, spanclass):
    
    return line