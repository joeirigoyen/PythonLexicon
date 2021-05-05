# Author: Raúl Youthan Irigoyen Osorio
import os

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


# Write line into file
def write_to_file(line):
    f = open(file_directory, "a")
    f.write(line)
    f.close()