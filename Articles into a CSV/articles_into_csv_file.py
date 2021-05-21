from ItemScraper import *
from articles_urls import *
import pandas as pd

shop1 = SnipesTracker(list_articles_snipes)
shop2 = ZalandoTracker(list_articles_zal)

list_brands = shop1.get_models_articles()[0] + shop2.get_models_articles()[0]
list_desc = shop1.get_models_articles()[1] + shop2.get_models_articles()[1]
list_prices = shop1.get_prices_articles()[0] + shop2.get_prices_articles()[0]
list_promos = shop1.get_prices_articles()[1] + shop2.get_prices_articles()[1]
list_urls_items = list_articles_snipes + list_articles_zal

table = list(zip(list_brands, list_desc, list_prices, list_promos, list_urls_items))
data_articles = pd.DataFrame(table, columns=['Brand', 'Description', 'Prices', 'Promos', 'Urls'])
data_articles.to_csv('MyArticles.csv')