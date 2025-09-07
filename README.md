# E-commerce Price Tracker

This project is an E-commerce Price Tracker that monitors product prices from Amazon and Flipkart. It utilizes web scraping techniques to fetch prices, compares them, and sends email notifications when price drops are detected. The project also includes data storage functionalities to keep track of historical prices.

# Features

- **Web Scraping**: Scrapes product prices from Amazon and Flipkart using `requests` and `BeautifulSoup`.
- **Price Comparison**: Compares current prices with previously stored prices to detect changes.
- **Email Notifications**: Sends notifications via email when a price drop is detected.
- **Data Storage**: Stores product prices in JSON or CSV formats for easy retrieval and analysis.

# Installation

1. Clone the repository:
   
   git clone <repository-url>
   cd ecommerce-price-tracker
   

2. Install the required dependencies:
   pip install -r requirements.txt

# Usage

1. Update the configuration in `src/main.py` with the products you want to track.
2. Run the application:
   python src/main.py

# Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

