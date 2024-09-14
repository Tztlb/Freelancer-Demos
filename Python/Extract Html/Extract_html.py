import requests
from bs4 import BeautifulSoup

# Function to extract, clean, and save HTML
def save_cleaned_webpage_html(url, file_name):
    try:
        # Send a GET request to fetch the HTML content of the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Prettify (clean/format) the HTML content
        cleaned_html = soup.prettify()

        # Write the cleaned HTML content to a file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(cleaned_html)
        print(f"Cleaned HTML content saved to {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

# Example usage
url = 'https://example.com/'  # Replace with your desired URL
file_name = 'cleaned_webpage.html'  # Replace with your desired file name
save_cleaned_webpage_html(url, file_name)
