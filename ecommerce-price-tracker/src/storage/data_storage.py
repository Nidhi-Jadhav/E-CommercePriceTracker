import json
import os

class DataStorage:
    def __init__(self, filename='prices.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def update_price(self, product_id, price):
        self.data[product_id] = price
        self.save_data()

    def get_price(self, product_id):
        return self.data.get(product_id, None)

    def get_all_prices(self):
        return self.data