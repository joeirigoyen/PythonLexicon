import os


# Initialize html file
def init_file(filename):
    # Get absolute directory for test files
    file_dir = os.path.abspath("test_files")
    # Open file in write mode
    f = open(filename, "w+")
    # Close file
    f.close()
    # Write initial html tags
    init_html(file_dir + "\\" + filename)
    return f


# Write initial html tags including css stylesheet linking
def init_html(filename):
    # Open file in write mode
    f = open(filename, "w+")
    # Set initial tags
    init_tags = '''<html>
    <head>
        <link rel=\"stylesheet\" href=\"styles.css\">
    </head>'''
    # Write initial tags to file
    f.write(init_tags)
    # Close file
    f.close()


# Read input file
def read_file(filename):
    pass


test_file = init_file("test.html")
