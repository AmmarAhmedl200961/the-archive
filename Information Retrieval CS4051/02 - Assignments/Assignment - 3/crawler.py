import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from urllib.robotparser import RobotFileParser

start_url = "http://www.mit.edu"
domain = "mit.edu"
max_pages = 100

visited = set()
to_visit = [start_url]
output_file = open("crawler_output.txt", "w")

# Create a RobotFileParser instance and set its URL
rp = RobotFileParser()
rp.set_url(urljoin(start_url, "/robots.txt"))
rp.read()

while len(visited) < max_pages and to_visit:
    url = to_visit.pop(0)
    if url in visited:
        continue

    # Check if the URL is allowed by robots.txt
    if not rp.can_fetch("*", url):
        continue

    response = requests.get(url)
    visited.add(url)

    content_type = response.headers.get("Content-Type")
    if "text/html" in content_type:
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href:
                parsed_href = urlparse(href)
                if parsed_href.netloc.endswith(domain):
                    canonical_href = urljoin(href, parsed_href.path)
                    to_visit.append(canonical_href)
                    output_file.write(f"{url} {canonical_href}\n")

output_file.close()