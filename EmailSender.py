import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender():
    def __init__(self, sender_email, receiver_email):
        self.receiver_email = receiver_email
        self.sender_email = sender_email


    def email_sender_Zalando(self, receiver_name, model, initial_price, new_price, url):
        email_password = "maxiPrepa92"
        message = MIMEMultipart("alternative")
        message["Subject"] = "Zalando Price Tracker"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email
        rate = 100 - int((float(new_price[:-1].strip().replace(",", '.'))*100)/float(initial_price[:-1].strip().replace(",", '.')))
        html = """\
        <html>
          <body>
            <h3>{receiver_name} be aware !</h3>
            <p> One of your items was placed on sale immediately: 
            <strong>{model}</strong>
            <br>
            The price of the item has changed from {initial_price} to {new_price}, 
            so that's a {discount}% discount.
            <br>
            To buy it now, click <a href="{url}" style="color: red; font-weight: bold"> here</a>.
            </p>
          </body>
        </html>
        """.format(receiver_name=receiver_name, model=model, initial_price=initial_price, new_price=new_price,
                   discount=rate, url=url)
        message.attach(MIMEText(html, "html"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(self.sender_email, email_password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            server.close()
            print('successfully sent the mail')

    def email_sender_Snipes(self, receiver_name, model, initial_price, new_price, url):
        email_password = "maxiPrepa92"
        message = MIMEMultipart("alternative")
        message["Subject"] = "Snipes Price Tracker"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email
        rate = 100 - int((float(new_price[:-1].strip().replace(",", '.'))*100)/float(initial_price[:-1].strip().replace(",", '.')))
        html = """\
        <html>
          <body>
            <h3>{receiver_name} be aware !</h3>
            <p> One of your items was placed on sale immediately: 
            <strong>{model}</strong>
            <br>
            The price of the item has changed from {initial_price} to {new_price} 
            so that's a {discount}% discount.
            <br>
            To buy it now, click <a href="{url}" style="color: red; font-weight: bold"> here</a>.
            </p>
          </body>
        </html>
        """.format(receiver_name=receiver_name, model=model, initial_price=initial_price, new_price=new_price,
                   discount=rate, url=url)
        message.attach(MIMEText(html, "html"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(self.sender_email, email_password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            server.close()
            print('successfully sent the mail')