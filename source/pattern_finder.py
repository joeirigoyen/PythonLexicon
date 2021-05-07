# Author: Raúl Youthan Irigoyen Osorio
import re
import reader as rd
import expression_parser as ep


# Tokens
comment_token = r"(#.*)"
decorator_token = r"(@\S*)"
string_token = r"([\"].*[\"]|[\'].*[\'])"
number_token = r"[\s\(=\+\*/]([0-9]*\.*[0-9]+)"
function_token = r"([a-zA-Z_][\w]*)\(.*\)"
arg_token = r"\(([\s\w_,]+)\)"
tab_token = r"(\s{4})"
tokens = [comment_token, decorator_token, string_token, number_token, function_token, arg_token, tab_token]


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
    return re.sub(token, "<span class=\"" + spanclass + "\" >" + line[start:end] + "</span>", line)


def find_matches(line: str, token, spanclass):
    des_match = re.findall(token, line)
    if (des_match is not None):
        for i in des_match:
            line = found_regex(line, line.index(i), line.index(i) + len(i), spanclass, i)
    return line


def assign_regex():
    regexs = ep.get_regexs(r"PythonLexicon\source\expressions.txt")
    for i in range(len(tokens)):
        if regexs[i] != None:
            tokens[i] = regexs[i]
