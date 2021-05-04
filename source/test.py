"""
Author: Raúl Youthan Irigoyen Osorio
"""
import os
import os.path
import re

# Directories
file_directory  = ""
source_directory = os.path.abspath("C:\\Users\\Joe\\Documents\\TEC\\Materias\\4to\\IMC\\PythonHighlighter\\PythonLexicon\\source\\source.txt")

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

# Write initial html tags including css stylesheet linking
def init_html(file_dir):
    # Open file in write mode
    f = open(file_dir, "w+")
    # Set initial tags
    init_tags = '''<html>
    <head>
        <link rel=\"stylesheet\" href=\"styles.css\">
    </head>
    <body>
        <div class="container">
            <h1 class="neon">PYTHON SYNTAX HIGHLIGHTER</h1>
            <h3>By Youthan Irigoyen and Jorge Penagos</h3>
        </div>
        <div class="window">
            <div class="titlebar">
                <div class="buttons">
                    <div class="close">
                        <a class="closebutton" href="#"><span><strong>x</strong></span></a>
                        <!-- close button link -->
                    </div>
                    <div class="minimize">
                        <a class="minimizebutton" href="#"><span><strong>&ndash;</strong></span></a>
                        <!-- minimize button link -->
                    </div>
                    <div class="zoom">
                        <a class="zoombutton" href="#"><span><strong>+</strong></span></a>
                        <!-- zoom button link -->
                    </div>
                </div>
                Your python code
                <!-- window title -->
            </div>
            <div class="content">
                <!-- window content -->
            '''
    # Write initial tags to file
    f.write(init_tags)
    # Close file
    f.close()


# Initialize html file
def init_file(filename):
    # Get absolute directory for html file
    global file_directory
    file_directory = os.path.abspath("PythonLexicon\\test_files\\" + filename)
    file_dir = os.path.abspath("PythonLexicon\\test_files\\" + filename)
    # Open file in write mode
    f = open(file_dir, "w+")
    # Close file
    f.close()
    # Write initial html tags
    init_html(file_dir)


# Write final html tags
def end_file():
    # Get absolute directory for html files
    file_dir = file_directory
    # Open file in write mode
    f = open(file_dir, "a")
    # Write tags
    final_tags = '''</div>\n\t\t</div>\n\t</body>\n</html>'''
    f.write(final_tags)
    # Close file
    f.close()


def found_regex(line, start, end, spanclass, token):
    return re.sub(token, "<span class=\"" + spanclass + "\">" + line[start:end] + "</span>", line)


def find_matches(line: str, token, spanclass):
    des_match = re.findall(token, line)
    if (des_match is not None):
        for i in des_match:
            line = found_regex(line, line.index(i), line.index(i) + len(i), spanclass, i)
    return line

def find_in_word(line, word: str, spanclass):
    curr_word = ""
    for char in word:
        curr_word += char
    if curr_word.isnumeric():
        line = find_matches(line, char, spanclass)
    return line


# Read full file by char
def read_file():
    counter = 0
    # Open file
    f = open(source_directory, "r")
    # Get lines
    lines = f.readlines()
    # Read lines by character
    for line in lines:
        counter += 1
        # Add html paragraph
        write_to_file("\t<p>")
        # Find regexps in line
        # Comments
        line = find_matches(line, comment_token, "comment")
        #com_match = re.search(comment_token, line)
        #if (com_match is not None):
            #line = found_regex(line, com_match.start(), com_match.end(), "comment", comment_token)
        # Decorators
        line = find_matches(line, decorator_token, "decorator")
        # Functions
        line = find_matches(line, function_token, "function")
        # Arguments
        line = find_matches(line, arg_token, "argument")
        # Find tabs
        line = find_matches(line, tab_token, "tab")
        # Find function calls
        line = find_matches(line, call_token, "function")
        # Find string
        # line = find_matches(line, string_token, "string")
        # Find numbers
        for word in line:
            line = find_in_word(line, word, "number")
        # End html paragraph
        write_to_file(line)
        write_to_file("</p>\n\t\t\t")


# Write line into file
def write_to_file(line):
    f = open(file_directory, "a")
    f.write(line)
    f.close()


# Run full program
if __name__ == '__main__':
    init_file("test.html")
    read_file()
    end_file()
