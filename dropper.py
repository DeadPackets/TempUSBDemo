import webbrowser
import os

HTML_FILE = """
<html><head><title>Malware Demo</title></head><body><h1>USB Malware PoC</h1></body></html>
"""

# First, save the HTML file in the same directory
file = open('dropped.html', 'w')
file.write(HTML_FILE)
file.flush()
file.close()

# Second, launch the webbrowser with our file
FILE_LOC = os.getcwd() + "\\dropped.html"
webbrowser.open(FILE_LOC)