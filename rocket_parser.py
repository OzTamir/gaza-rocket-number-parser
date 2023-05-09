import csv
import re
import requests
from bs4 import BeautifulSoup

# Replace the URL below with the URL of the website containing the tables
url = "https://www.jewishvirtuallibrary.org/palestinian-rocket-and-mortar-attacks-against-israel"

# Download the website content
response = requests.get(url)
content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all the tables preceded by an h3 tag
h3_tags = soup.find_all('h3')

# Create a unified CSV file
with open('unified.csv', 'w', newline='', encoding='utf-8') as unified_csvfile:
    unified_writer = csv.writer(unified_csvfile)

    for h3 in h3_tags:
        h3_text = h3.get_text(strip=True)

        # Check if the h3 tag contains a four-digit number
        if re.fullmatch(r'\d{4}', h3_text):
            table = h3.find_next('table')
            if table:
                # Get the table title from the h3 tag
                title = h3_text

                # Create a CSV file for each table
                file_name = f"{title}.csv"
                with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)

                    # Extract table header and rows
                    header = []
                    rows = table.find_all('tr')
                    for row in rows:
                        cells = row.find_all(['th', 'td'])
                        data_row = [title] + [cell.get_text(strip=True) for cell in cells]
                        writer.writerow(data_row)
                        unified_writer.writerow(data_row)
                print(f"Created CSV file: {file_name}")

print("Created unified CSV file: unified.csv")
