# My Data Analyst task — Run Instructions

## Setup (one time)
```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn
```

## Run in order
```bash
python task1_scraping.py       # -> creates books_data.csv
python task2_eda.py            # -> prints EDA findings in terminal
python task3_visualization.py  # -> creates dashboard.png
```

## What each task does
- **Task 1 (Scraping):** Pulls title, price, rating, and stock status for
  every book on books.toscrape.com using `requests` + `BeautifulSoup`,
  paginating automatically until it hits the last page. Saves to CSV.

- **Task 2 (EDA):** Loads the CSV, checks structure/types/missing values,
  answers a few concrete questions (price range, price-vs-rating
  correlation, stock split), and flags price outliers with the IQR method.

- **Task 3 (Visualization):** Builds a 2x2 dashboard — price distribution,
  books per rating, average price by rating, and stock availability —
  saved as `dashboard.png` for your portfolio/submission.

## Adapting to a different website
If your company wants a specific site scraped instead, the same structure
works — just swap `BASE_URL` and the CSS selectors in `task1_scraping.py`
to match that site's HTML (right-click → Inspect on the page to find the
right class names). Everything downstream (Task 2 and 3) will still work
as long as the CSV has similar columns.
