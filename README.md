This project is a web scraper that extracts product details from Amazon using BeautifulSoup (BS4). It fetches titles, reviews, prices, and URLs from multiple pages and saves the data in a CSV file.

🔹 Features
✅ Scrapes product information from Amazon search results
✅ Extracts Title, Reviews, Price, and Product URL
✅ Saves data in CSV format (amazon_products_updated.csv)
✅ Implements random delays to prevent getting blocked
✅ Uses CSS selectors instead of XPath for better efficiency

📌 Dependencies
Make sure you have the following installed:

Python 3.7+
BeautifulSoup4 (pip install beautifulsoup4)
Requests (pip install requests)
Pandas (pip install pandas)

Usage Notes
The script scrapes data from Amazon search results (default: "cleaning tools").
It loops through multiple pages and extracts product details.
The extracted data is saved in amazon_products_updated.csv.
To modify search keywords, update the BASE_URL in bs.py and range depend on your desired pages.

📧 Contact
For any questions, reach out at:
📩 amadansari89@gmail.com
🚀 Happy Scraping! 🎯
