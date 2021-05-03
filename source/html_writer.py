"""
Author: Raúl Youthan Irigoyen Osorio
"""
import os
import re


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
                <span class="keyword">print</span>(<span class="string">"Super Joe Cool"</span>)
            '''
    # Write initial tags to file
    f.write(init_tags)
    # Close file
    f.close()


# Initialize html file
def init_file(filename):
    # Get absolute directory for html files
    file_dir = os.path.abspath("PythonLexicon\\test_files\\" + filename)
    # Open file in write mode
    f = open(file_dir, "w+")
    # Close file
    f.close()
    # Write initial html tags
    init_html(file_dir)


# Write final html tags
def end_file(filename):
    # Get absolute directory for html files
    file_dir = os.path.abspath("PythonLexicon\\test_files\\" + filename)
    # Open file in write mode
    f = open(file_dir, "a")
    # Write tags
    final_tags = '''</div>\n\t\t</div>\n\t</body>\n</html>'''
    f.write(final_tags)
    # Close file
    f.close()


# Search for functions/classnames in file
def find_fun(string):
    match_str = r"([a-zA-Z]+\(\))"
    result = re.search(match_str, string)
    if (result is not None):
        return result.group()[:-2]
    else:
        return ""


# Find function call
def find_call(string):
    match_str = r"\.([^)]+\(\))"
    result = re.search(match_str, string)
    if (result is not None):
        return result.group()[1:-2]
    else:
        return ""


# Find arguments inside a function
def find_arg(string):
    match_str = r"\(([^)]+\))"
    result = re.search(match_str, string)
    if result is not None:
        return result.group()[1:-1]
    else:
        return ""


# Find string
def find_string(string):
    match_str = r"([\"\'])(?:(?=(\\?))\2.)*?\1"
    result = re.search(match_str, string)
    if result is not None:
        return result.group()[1:-1]
    else:
        return ""


init_file("test.html")
print(find_fun("def hello():"))
print(find_arg("def print(integer):"))
print(find_call("hello.__main__()"))
print(find_string("\"poop\""))
end_file("test.html")