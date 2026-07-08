import requests
from bs4 import BeautifulSoup


def extract_content(url):

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        paragraphs = soup.find_all("p")

        text = ""

        for p in paragraphs:

            text += p.get_text() + "\n"

        return text[:5000]

    except Exception as e:

        print("Scraper Error:", e)

        return ""