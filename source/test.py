"""
Author: Raúl Youthan Irigoyen Osorio
"""
import os
import os.path
import re
import html_writer as hw
import pattern_finder as pf

# Directories
file_directory  = ""
source_directory = os.path.abspath("C:\\Users\\Joe\\Documents\\TEC\\Materias\\4to\\IMC\\PythonHighlighter\\PythonLexicon\\source\\source.txt")


# Read full file by char
def read_file():
    # Open file
    f = open(source_directory, "r")
    # Get lines
    lines = f.readlines()
    # Read lines by character
    for line in lines:
        # Add html paragraph
        hw.write_to_file("\t<p>")
        # Find regexps in line
        # Comments
        line = pf.find_matches(line, pf.comment_token, "comment")
        # Decorators
        line = pf.find_matches(line, pf.decorator_token, "decorator")
        # Functions
        line = pf.find_matches(line, pf.function_token, "function")
        # Arguments
        line = pf.find_matches(line, pf.arg_token, "argument")
        # Find tabs
        line = pf.find_matches(line, pf.tab_token, "tab")
        # Find function calls
        line = pf.find_matches(line, pf.call_token, "function")
        # Find escape characters
        line = pf.find_matches(line, pf.escape_token, "escape")
        # Find special elements
        for word in line.split():
            # Keywords
            if word.replace("</span>", "") in pf.keywords:
                line = pf.find_matches(line, word.replace("</span>", ""), "keyword")
            # Strings
            if "class=" not in word and "\"" in word:
                line = re.sub(word, "<span class=\"string\">" + word + "</span>", line)
 

        # End html paragraph
        hw.write_to_file(line)
        hw.write_to_file("</p>\n\t\t\t")


# Run full program
if __name__ == '__main__':
    hw.init_file("test.html")
    read_file()
    hw.end_file()
