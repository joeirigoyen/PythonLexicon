"""
Author: Raúl Youthan Irigoyen Osorio
"""
import os
import os.path
import re

curr_state = 0
curr_line = ""

file_directory  = ""
source_directory = os.path.abspath("C:\\Users\\Joe\\Documents\\TEC\\Materias\\4to\\IMC\\PythonHighlighter\\PythonLexicon\\source\\source.txt")

# Tokens
function_token = r"\s([a-zA-Z_][\w]*)\([\w\W]*\):"
call_token = r"([a-zA-Z_][\w]*)\([\w\W]*\)"
arg_token = r"[\(](\w+[,]*[\s\S][\w]+)\)"
string_token = r"([\"][^\"]*\")"
number_token = r"(^[0-9]*[\.]{0,1}[0-9]*)"
comment_token = r"(#.*)"
declare_token = r"(^[^0-9][\w]+)[\s\S]="
decorator_token = r"(@[\S]*)"


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
            <h3>By: Youthan Irigoyen</h3>
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

def write_to_file(line):
    f = open(file_directory, "a")
    f.write(line)
    f.close()


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


# Read file
def read_file():
    # Call global curr_str variable
    global curr_line
    # Open reading file
    rf = open(source_directory, "r")
    # Get lines
    lines = rf.readlines()
    for line in lines:
        curr_line = "<p>"
        # Look for comments
        com_sub = re.findall(comment_token, line)
        if len(com_sub) != 0:
            for i in range(len(com_sub)):
                curr_line += "<span class=\"comment\">" + com_sub[i] + "</span>"
            write_to_file(curr_line)
            continue
        # Look for function declarations
        fun_sub = re.search(function_token, line)
        if (fun_sub is not None):
            for i in range(len(fun_sub.groups())):
                curr_line += "<span class=\"function\">" + fun_sub.groups()[i] + "</span>"
            curr_line += "</p>"
        write_to_file(curr_line)


    # Close file
    rf.close()


# Run full program
if __name__ == '__main__':
    init_file("test.html")
    read_file()
    end_file()
