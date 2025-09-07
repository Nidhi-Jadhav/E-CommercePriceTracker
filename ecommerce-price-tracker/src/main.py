# filepath: ecommerce-price-tracker/src/main.py

import time
from scraper.amazon_scraper import scrape_amazon_price
from scraper.flipkart_scraper import scrape_flipkart_price
from comparator.price_comparator import compare_prices
from notifier.email_notifier import send_email_notification
from storage.data_storage import load_prices, save_prices

# Set your email credentials here
EMAIL_USER = "your_email@example.com"
EMAIL_PASS = "your_password"

def main():
    # Load previously stored prices
    stored_prices = load_prices()

    # Scrape prices from Amazon and Flipkart
    amazon_price = scrape_amazon_price("product_url_here")
    flipkart_price = scrape_flipkart_price("product_url_here")

    # Compare prices and check for drops
    if compare_prices(stored_prices, amazon_price, "Amazon"):
        send_email_notification("Amazon", amazon_price)
    if compare_prices(stored_prices, flipkart_price, "Flipkart"):
        send_email_notification("Flipkart", flipkart_price)

    # Save the new prices
    save_prices({"Amazon": amazon_price, "Flipkart": flipkart_price})

if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)  # Check every hour

# Install dependencies
pip install -r requirements.txt

# To run the script
# RUN: python src\main.py

cd "c:\Users\jadha\OneDrive\Desktop\Price Tracker\ecommerce-price-tracker"