import requests
from bs4 import BeautifulSoup

def get_flipkart_price(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(product_url, headers=headers)
    
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    price_tag = soup.find('div', {'class': '_30jeq3 _16Jk6d'})
    
    if price_tag:
        price = price_tag.text.replace('₹', '').replace(',', '').strip()
        return float(price)
    
    return None

def get_flipkart_product_title(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(product_url, headers=headers)
    
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title_tag = soup.find('span', {'class': 'B_NuCI'})
    
    if title_tag:
        return title_tag.text.strip()
    
    return None