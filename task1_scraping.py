import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {"User-Agent": "Mozilla/5.0 (educational scraping project)"}

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def scrape_page(page_num: int):
    """Scrape a single listing page and return a list of book dicts."""
    url = BASE_URL.format(page_num)
    response = requests.get(url, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        return None  # signals "no more pages" or an error

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")

    page_data = []
    for book in books:
        title = book.h3.a["title"]

        price_text = book.select_one(".price_color").text
        price = float(price_text.replace("£", "").replace("Â", "").strip())

        rating_class = book.select_one("p.star-rating")["class"][1]
        rating = RATING_MAP.get(rating_class, None)

        availability = book.select_one(".availability").text.strip()
        in_stock = "In stock" in availability

        page_data.append({
            "title": title,
            "price_gbp": price,
            "rating": rating,
            "in_stock": in_stock,
        })

    return page_data


def scrape_all(max_pages: int = 50):
    """Loop through pages until a 404 (end of catalogue) is hit."""
    all_books = []
    page = 1

    while page <= max_pages:
        print(f"Scraping page {page}...")
        page_data = scrape_page(page)

        if page_data is None:
            print("No more pages found. Stopping.")
            break

        all_books.extend(page_data)
        page += 1
        time.sleep(0.5)  # be polite to the server

    return all_books


if __name__ == "__main__":
    data = scrape_all()
    df = pd.DataFrame(data)
    df.to_csv("books_data.csv", index=False)
    print(f"\nDone. Scraped {len(df)} books -> saved to books_data.csv")
    print(df.head())
