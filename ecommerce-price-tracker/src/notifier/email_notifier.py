from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_price_drop_notification(to_email, product_name, old_price, new_price):
    subject = f"Price Drop Alert for {product_name}"
    body = f"The price for {product_name} has dropped from {old_price} to {new_price}!"

    msg = MIMEMultipart()
    msg['From'] = 'your_email@example.com'
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)
            print(f"Notification sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")