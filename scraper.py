import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = "https://www.delhisldc.org/Resources/generation.htm"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the specific table(s) you need
    tables = soup.find_all('table')  # Find all tables
    
    # Example: Let's extract the first table
    if tables:
        table = tables[0]  # Select the table you want to scrape
        rows = []
        
        # Extract data from rows and columns
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            rows.append([col.text.strip() for col in columns])
        
        # Convert to DataFrame for easy manipulation
        df = pd.DataFrame(rows)
        
        # Display the first few rows of the DataFrame
        print(df.head())
        
        # Optionally, save the data to a CSV file
        df.to_csv('scraped_data.csv', index=False)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")




"""import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = "https://www.delhisldc.org/Resources/generation.htm"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table(s) on the webpage
    tables = soup.find_all('table')
    
    if tables:
        table = tables[0]
        
        # Extract table rows
        rows = []
        for row in table.find_all('tr'):
            columns = row.find_all(['td', 'th'])
            rows.append([col.text.strip() for col in columns])
        
        # Inspect the first row to check if it contains headers
        print("First row (possible headers):", rows[0])
        
        # If headers are not correct or available, define them manually
        manual_headers = ['Column1', 'Column2', 'Column3', 'Column4']  # Define based on your understanding
        
        # Print the first few rows for inspection
        for i, row in enumerate(rows[:5]):  # Print first 5 rows
            print(f"Row {i}: {row}")
        
        # Check if headers match the number of columns in rows
        if len(rows[0]) != len(rows[1]):
            headers = manual_headers  # Use manual headers
            data = rows  # Keep all rows as data
        else:
            headers = rows[0]  # Use the first row as headers
            data = rows[1:]  # Remaining rows are data
        
        # Create DataFrame with manually defined headers if necessary
        df = pd.DataFrame(data, columns=headers)
        
        # Display the DataFrame
        print(df.head())
        
        # Optionally save the data to a CSV file
        df.to_csv('delhi_generation_data.csv', index=False)
        
    else:
        print("No tables found on the webpage.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
"""