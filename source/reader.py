"""
Author: Raúl Youthan Irigoyen Osorio
"""
import time
import os
import os.path
import re
import html_writer as hw
import pattern_finder as pf


# Directories
curr_state = 0
file_directory  = ""
source_directory = os.path.abspath("C:\\Users\\Joe\\Documents\\TEC\\Materias\\4to\\IMC\\PythonHighlighter\\PythonLexicon\\source\\source.txt")


# Read full file by char
def read_file():
    global curr_state
    # Open file
    f = open(source_directory, "r")
    # Get lines
    lines = f.readlines()
    # Read lines by character
    for line in lines:
        # Add html paragraph
        hw.write_to_file("\t<p>")
        # Set state to 0
        curr_state = 0
        # Find regexps in line
        # Comments
        line = pf.find_matches(line, pf.comment_token, "comment")
        # Decorators
        line = pf.find_matches(line, pf.decorator_token, "decorator")
        # Arguments
        line = pf.find_matches(line, pf.arg_token, "argument")
        # Find tabs
        line = pf.find_matches(line, pf.tab_token, "tab")
        # Find function calls
        line = pf.find_matches(line, pf.function_token, "function")
        # Find numbers
        line = pf.find_matches(line, pf.number_token, "number")
        # Find special elements
        for word in line.split():
            # Keywords
            if word.replace("</span>", "") in pf.keywords:
                line = pf.find_matches(line, word.replace("</span>", ""), "keyword")
            # Strings
            if "class=" not in word: 
                if "\"" in word or "\'" in word:
                    line = re.sub(word, "<span class=\"string\">" + word + "</span>", line)

        # End html paragraph
        if line != None:
            hw.write_to_file(line)
        hw.write_to_file("</p>\n\t\t\t")


# Run full program
if __name__ == '__main__':
    init_time = time.time()
    hw.init_file("test.html")
    pf.assign_regex()
    read_file()
    hw.end_file()
    finish_time = time.time() - init_time
    print("Runtime: " + str(finish_time))