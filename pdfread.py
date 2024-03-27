import pdfplumber

# Open the PDF file
with pdfplumber.open("/Users/hridayjain/Desktop/bin/placements.pdf") as pdf:
    # Extract text from the first page
    first_page = pdf.pages[0]
    table = first_page.extract_table()

    # Filter the table to keep only rows containing "IT" or similar keywords
    it_students = [row for row in table if "Information Technology" in row]

    # Print the filtered table
    for row in it_students:
        print(row)
