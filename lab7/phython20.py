import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://news.ycombinator.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=10)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    print("HACKER NEWS HEADLINES")
    print("=" * 70)

    stories = soup.select("span.titleline > a")

    for i, story in enumerate(stories, start=1):

        headline = story.get_text(strip=True)
        link = story.get("href")

        # Convert relative links to absolute URLs
        link = urljoin(url, link)

        print(f"{i}. {headline}")
        print(f"   Link: {link}")
        print()

else:
    print("Failed to retrieve webpage.")
    print("Status code:", response.status_code)

