"""
Author: Raúl Youthan Irigoyen Osorio
"""
import os
from os.path import curdir
import re

curr_state = 0
curr_str = ""

file_directory  = ""
source_directory = os.path.abspath("C:\\Users\\Joe\\Documents\\TEC\\Materias\\4to\\IMC\\PythonHighlighter\\PythonLexicon\\source\\source.txt")

keywords = {"def": 1,
            "if": 2,
            "for": 3,
            "else": 4,
            "break": 5,
            "continue": 6,
            "while": 7,
            "import": 8,
            "from": 9,
            "is": 10,
            "and": 11,
            "or": 12,
            "as": 13,
            "assert": 14,
            "class": 15,
            "del": 16,
            "elif": 17,
            "except": 18,
            "False": 19,
            "True": 20,
            "finally": 21,
            "global": 22,
            "in": 23,
            "lambda": 24,
            "None": 25,
            "nonlocal": 26,
            "not": 27,
            "raise": 28,
            "return": 29,
            "try": 30,
            "with": 31,
            "yield": 32}

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


# Search for function declarations in file
def find_fun(line):
    # Open file
    f = open(file_directory, "a")
    # Look for matching substring in line
    match_str = r"([a-zA-Z_-]+\(\):)"
    result = re.search(match_str, line)
    if result is not None:
        # Write initial tag in file
        f.write("\t<span class=\"function\">")
        f.write(f"{result.group()[:-3]}</span>")
        f.write(f"{result.group()[-3:-1]}</span>")
        # Close program
        f.close()


# Find string
def find_string(string):
    match_str = r"([\"\'])(?:(?=(\\?))\2.)*?\1"
    result = re.search(match_str, string)
    if result is not None:
        return result.group()[1:-1]
    else:
        return ""


# Add keyword html tags
def found_keyword(keyword):
    f = open(file_directory, "a")
    f.write("\t<span class=\"keyword\">" + keyword + "</span>")
    f.close()


# Write 
def write_br():
    f = open(file_directory, "a")
    f.write("<br>")
    f.close()

# Read file
def read_file():
    # Call global curr_str variable
    global curr_state, curr_str
    # Open reading file
    rf = open(source_directory, "r")
    # Get lines
    lines = rf.read().splitlines(True)
    # Scan every line
    for line in lines:
        for char in line:
            # Add char to current string
            curr_str += char
            # If char is newline, reset current string
            if char == "\n":
                curr_state = 0
                curr_str = ""
                write_br()
            # If char is # set as comment
            if char == "#":
                curr_state = 1
            
            

            
    rf.close()


# Run full program
if __name__ == '__main__':
    init_file("test.html")
    read_file()
    end_file()
