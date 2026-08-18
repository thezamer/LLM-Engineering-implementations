import requests
from bs4 import BeautifulSoup


def scrape_webpage(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text(separator=" ", strip=True)

    return text