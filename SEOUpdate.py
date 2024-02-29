import requests 
from bs4 import BeautifulSoup 
from collections import Counter 
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords') 

#Fetching Page Content
def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    
#Extracting Text from HTML
def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text

#Analyzing Keyword Frequency
def keyword_frequency(text):
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in text.split() if word.lower() not in stop_words]
    word_counts = Counter(words)
    return word_counts

#Checking for Keyword Stuffing
def keyword_stuffing(url, limit=5): #limit 5
    page_content = get_page_content(url)
    
    if page_content:
        text_content = extract_text_from_html(page_content)
        word_counts = keyword_frequency(text_content)

        for word,count in word_counts.items():
            if count > limit:
                print(f"Potential keyword stuffing: '{word}' -- {count} times.")
                

if __name__ == "__main__":
    website_url = "https://www.ibm.com/topics/supercomputing"
    keyword_stuffing(website_url)
