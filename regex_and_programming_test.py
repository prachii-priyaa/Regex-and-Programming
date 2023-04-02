

#To extract the required information from the PDF file, I would use the following tools:

#Python - to write the script to extract the information from the PDF file
#PyPDF2 - a Python library to read and manipulate PDF files
#Regular expressions - to extract specific patterns of text from the PDF file

pip install PyPDF2

import re
import PyPDF2
import json

# Open the PDF file
pdf_file = open('AWS Lambda Pricing.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the first page of the PDF file
page = pdf_reader.pages[0]

# Extract the text from the page
text = page.extract_text()

# Define the regex pattern to extract the information
pattern = r'(\d+)\s+(.*)\s+(.*)\s+(.*)'

# Find all matches of the pattern in the text
matches = re.findall(pattern, text)

# Create a list of dictionaries to store the extracted information
output = []
for match in matches:
    output.append({
        "id": match[0],
        "Architecture": match[1],
        "Duration": match[2],
        "Requests": match[3]
    })

# Print the output
print({"output": output})
