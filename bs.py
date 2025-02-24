import requests
from bs4 import BeautifulSoup
import random
import time
import pandas as pd

# Set headers to mimic a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Base URL
BASE_URL = "https://www.amazon.com/s?k=cleaning%20tools&ref=glow_cls&refresh=1&page="

# List to store scraped data
all_products = []

# Loop through the first 5 pages
for page in range(1, 6):
    url = BASE_URL + str(page)
    print(f"Scraping page {page}: {url}")

    # Make request
    response = requests.get(url, headers=HEADERS)
    
    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to load page {page}, status code: {response.status_code}")
        continue
    
    # Parse the page content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all product containers
    products = soup.select('div.s-main-slot div.s-result-item')

    print(f"Found {len(products)} products on page {page}")

    # Loop through each product
    for product in products:
        # Extract Data Using New CSS Selectors
        title_elem = product.select_one("div.a-section.a-spacing-none.a-spacing-top-small.s-title-instructions-style > a > h2")
        reviews_elem = product.select_one("div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small > div:nth-child(2)")
        price_elem = product.select_one("div.a-section.a-spacing-none.a-spacing-top-small.s-price-instructions-style")
        link_elem = product.select_one("div.a-section.a-spacing-none.a-spacing-top-small.s-title-instructions-style > a")

        product_data = {
            "title": title_elem.text.strip() if title_elem else "N/A",
            "reviews": reviews_elem.text.strip() if reviews_elem else "N/A",
            "price": price_elem.text.strip() if price_elem else "N/A",
            "url": f"https://www.amazon.com{link_elem['href']}" if link_elem else "N/A",
        }
        
        all_products.append(product_data)

    # Add random delay to avoid detection
    time.sleep(random.randint(2, 5))

# Print results
for idx, product in enumerate(all_products, 1):
    print(f"Product {idx}: {product}")

# Save to CSV
df = pd.DataFrame(all_products)
df.to_csv("amazon_products_updated2.csv", index=False)
print("Data saved to amazon_products_updated2.csv")
