import requests
import os


from bs4 import BeautifulSoup
os.environ['REQUESTS_CA_BUNDLE'] = '/path/to/certificate.pem'

# Function to scrape data from tourism websites
def scrape_tourism_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url, verify=False)
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text content from the HTML
        text = soup.get_text(separator=' ')
        return text
    except Exception as e:
        print("Error:", e)
        return None

# Function to count occurrences of keywords and calculate total score
def calculate_score(text):
    # Keywords related to Environmental Impact, Community Empowerment, and Cultural Preservation
    environmental_keywords = ['environment', 'sustainable', 'ecotourism', 'conservation']
    community_keywords = ['community', 'empowerment', 'local', 'participation']
    cultural_keywords = ['culture', 'heritage', 'tradition', 'cultural']

    # Count occurrences of keywords
    environmental_count = sum(text.lower().count(keyword) for keyword in environmental_keywords)
    community_count = sum(text.lower().count(keyword) for keyword in community_keywords)
    cultural_count = sum(text.lower().count(keyword) for keyword in cultural_keywords)

    # Calculate total score
    total_score = environmental_count + community_count + cultural_count
    return total_score

# Main function
def main():
    # URL of the tourism website to scrape
    url = "https://uttarakhandtourism.gov.in/index.php/destination/auli"

    # Scrape data from the tourism website
    text_data = scrape_tourism_website(url)

    if text_data:
        # Calculate the score based on the scraped data
        total_score = calculate_score(text_data)
        print("Total Score:", total_score)
    else:
        print("Failed to scrape data from the website.")

if __name__ == "__main__":
    main()
