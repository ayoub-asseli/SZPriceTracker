from ItemScraper import *
from articles_urls import *
import EmailSender as ES

shop1 = SnipesTracker(list_articles_snipes)
shop2 = ZalandoTracker(list_articles_zal)

list_brands = shop1.get_models_articles()[0] + shop2.get_models_articles()[0]
list_desc = shop1.get_models_articles()[1] + shop2.get_models_articles()[1]
list_prices = shop1.get_prices_articles()[0] + shop2.get_prices_articles()[0]
list_promos = shop1.get_prices_articles()[1] + shop2.get_prices_articles()[1]
list_urls_items = list_articles_snipes + list_articles_zal
items = list(zip(list_brands, list_desc, list_prices, list_promos, list_urls_items))

sender = 'pythonista924@gmail.com'
receiver = 'pythonista924@gmail.com'
message = ES.EmailSender(sender, receiver)

for item in items:
    if 'None' not in item and 'zalando' in item[len(item)-1]:
        receiver_name = 'Pythonista'
        model = item[0] + ' ' + item[1]
        initial_price = item[2]
        new_price = item[3]
        url = item[4]
        message.email_sender_Zalando(receiver_name, model, initial_price, new_price, url)
    elif 'None' not in item and 'snipes' in item[len(item)-1]:
        receiver_name = 'Pythonista'
        model = item[0] + ' ' + item[1]
        initial_price = item[2]
        new_price = item[3]
        url = item[4]
        message.email_sender_Snipes(receiver_name, model, initial_price, new_price, url)