def compare_prices(new_price, old_price):
    if new_price < old_price:
        return True  # Price drop detected
    return False

def trigger_notification(product_name, old_price, new_price):
    if compare_prices(new_price, old_price):
        # Logic to trigger email notification
        print(f"Price drop alert for {product_name}: from {old_price} to {new_price}") 

def compare_and_notify(product_name, new_price, old_price):
    if compare_prices(new_price, old_price):
        trigger_notification(product_name, old_price, new_price)