import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

# Website URL
BASE_URL = "https://books.toscrape.com/"
url = BASE_URL

# CSV file name
CSV_FILE = "products.csv"

# CSV columns
fields = ["Book Name", "Price", "Availability", "Rating"]

print("=" * 60)
print("       📚 BOOK STORE - PRODUCT SCRAPER")
print("=" * 60)

# Create CSV file
with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as file:

    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()

    book_count = 0
    page_count = 0

    # Scrape all pages
    while url:

        page_count += 1
        print(f"\n📄 Scraping Page {page_count}...")

        # Request website
        response = requests.get(url)

        if response.status_code != 200:
            print("❌ Unable to access the website.")
            break

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all books
        books = soup.select("article.product_pod")

        # Extract book information
        for book in books:

            # Book name
            book_name = book.h3.a["title"]

            # Price
            price = book.select_one(".price_color").get_text(strip=True)

            # Fix currency encoding
            price = price.replace("Â£", "£")

            # Availability
            availability = book.select_one(
                ".availability"
            ).get_text(" ", strip=True)

            # Rating
            rating = book.select_one("p.star-rating")["class"][1]

            # Save data to CSV
            writer.writerow({
                "Book Name": book_name,
                "Price": price,
                "Availability": availability,
                "Rating": rating
            })

            book_count += 1

        print(f"   ✓ Books found: {len(books)}")

        # Find next page
        next_button = soup.select_one("li.next a")

        if next_button:
            next_page = next_button["href"]
            url = urljoin(url, next_page)
        else:
            url = None

print("\n" + "=" * 60)
print("              ✅ SCRAPING COMPLETED")
print("=" * 60)
print(f"📄 Total Pages Scraped : {page_count}")
print(f"📚 Total Books Scraped : {book_count}")
print(f"💾 CSV File Created    : {CSV_FILE}")
print("=" * 60)

