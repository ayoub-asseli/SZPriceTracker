from requests_html import HTMLSession
from bs4 import BeautifulSoup

##### Scraping part #####
scraper = HTMLSession()

def get_data_page(url):
    return BeautifulSoup(scraper.get(url).text, 'html.parser')

class SnipesTracker():

    def __init__(self,list_articles):
        self.list_articles = list_articles

    def get_models_articles(self):
        list_brands = []
        list_desc = []
        for url in self.list_articles:
            soup = get_data_page(url)
            model = soup.find('div', {'class': 'js-target'})
            brand = model.find('a', {'class': 'b-pdp-brand'}).text.strip()
            list_brands.append(brand.replace('\n', ' '))
            list_desc.append(model.getText().replace('\n', ' ').replace(brand, '').strip())
        return list_brands, list_desc


    def get_prices_articles(self):
        list_prices =[]
        list_promos = []
        for url in self.list_articles:
            soup = get_data_page(url)
            div = soup.find('div', {'class': 'b-price-section'})
            spans = div.find_all('span', {'class': 'b-product-tile-price-item'})
            initial_price = spans[0].text.replace('\n', '')
            try:
                new_price = spans[1].text.replace('\n', '')
                list_prices.append(initial_price)
                list_promos.append(new_price)
            except:
                list_prices.append(initial_price)
                list_promos.append('None')
        return list_prices,list_promos


class ZalandoTracker():

    def __init__(self, list_articles):
        self.list_articles = list_articles

    def get_models_articles(self):
        list_brands= []
        list_desc = []
        for url in self.list_articles:
            soup = get_data_page(url)
            brand = soup.find('a', {'class': '_5Yd-hZ g88eG_ oHRBzn LyRfpJ pVrzNP sW9qW7 g88eG_ oHRBzn LyRfpJ'})
            descr = soup.find('h1', {'class': 'OEhtt9 ka2E9k uMhVZi z-oVg8 pVrzNP w5w9i_ _1PY7tW _9YcI4f'})
            list_brands.append(brand.text)
            list_desc.append(descr.text)
        return list_brands, list_desc

    def get_prices_articles(self):
        list_prices = []
        list_promos = []
        for url in self.list_articles:
            soup = get_data_page(url)
            div = soup.find('div', {'class': '_0xLoFW vSgP6A _7ckuOK'})
            #Article with no discount
            span_price = div.find('span', {'class': 'uqkIZw ka2E9k uMhVZi FxZV-M z-oVg8 pVrzNP'})
            #Article on discount
            span_new_price = div.find('span', {'class': 'uqkIZw ka2E9k uMhVZi dgII7d z-oVg8 _88STHx cMfkVL'})
            span_initial_price = div.find('span', {'class': 'uqkIZw ka2E9k uMhVZi FxZV-M z-oVg8 weHhRC ZiDB59'})
            try:
                initial_price = span_initial_price.text.replace('\xa0', ' ')
                new_price = span_new_price.text.replace('\xa0', ' ')
                list_prices.append(initial_price)
                list_promos.append(new_price)
            except:
                list_prices.append(span_price.text.replace('\xa0', ' '))
                list_promos.append('None')
        return list_prices, list_promos