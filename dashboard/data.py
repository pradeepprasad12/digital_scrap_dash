import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_data():
    # URL of the page to scrape
    url = 'https://www.checkpoint.com/support-services/support-life-cycle-policy/'

    # Send a GET request to the webpage
    response = requests.get(url)

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize a list to store the table data
    table_data = []

    # Find the table with the specific class
    table = soup.find('table', class_='table table-striped table-bordered')

    # Check if the table is found
    if table:
        # Find all the rows in the table
        rows = table.find_all('tr')

        # Extract header row if available
        headers = [header.get_text(strip=True) for header in rows[0].find_all('th')]

        # Add the 'ID' column to headers
        headers.insert(0, 'ID')

        # Replace spaces with underscores in column names
        headers = [header.replace(' ', '_') for header in headers]

        # Extract data rows
        for idx, row in enumerate(rows[1:], start=1):  # Start index from 1
            cols = row.find_all('td')
            if cols:
                row_data = [col.get_text(strip=True) for col in cols]
                table_data.append([idx] + row_data)  # Prepend index to row data

        # Create a DataFrame
        df = pd.DataFrame(table_data, columns=headers)

        # Optionally save the DataFrame to a CSV file
        df.to_csv('table_data.csv', index=False)

        return df  # Return the DataFrame for use
    else:
        print("Table not found.")
        return None
