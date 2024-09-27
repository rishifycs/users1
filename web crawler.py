import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin
import time

# Step 1: Define the HTML parser to extract links
class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':  # We are interested in <a> tags
            for attr, value in attrs:
                if attr == 'href':  # Extract the href attribute
                    self.links.append(value)

    def get_links(self):
        return self.links

# Step 2: Function to fetch a webpage
def fetch_page(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Failed to retrieve the URL: {url} due to {e}")
        return None

# Step 3: Function to crawl webpages
def web_crawler(start_url, max_depth=2, max_urls=10):
    visited_urls = set()  # Keep track of visited URLs
    urls_to_visit = [(start_url, 0)]  # URLs to visit, along with their depth
    count = 0

    while urls_to_visit and count < max_urls:
        current_url, depth = urls_to_visit.pop(0)

        if current_url in visited_urls or depth > max_depth:
            continue

        print(f"Visiting: {current_url} at depth {depth}")
        visited_urls.add(current_url)
        count += 1

        # Fetch the page
        page_content = fetch_page(current_url)
        if page_content is None:
            continue

        # Parse the page and extract links
        parser = LinkParser()
        parser.feed(page_content)
        links = parser.get_links()

        # Convert relative URLs to absolute URLs and queue them
        for link in links:
            absolute_url = urljoin(current_url, link)
            if absolute_url not in visited_urls:
                urls_to_visit.append((absolute_url, depth + 1))

        time.sleep(1)
start_url = "http://www.github.com" 
web_crawler(start_url)
