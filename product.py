from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from fuzzywuzzy import fuzz
from itertools import combinations
import json


class Product:
    def __init__(self, search):
        self.driver = 0
        self.search = search

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, var):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self._driver = webdriver.Chrome(options=options)
        self._driver.maximize_window()

        self._driver.get('https://www.mercadolivre.com.br/')
    

    def search_ml(self):
        input = self.driver.find_element(By.ID, 'cb1-edit')
        input.clear()
        input.send_keys(self.search + Keys.ENTER)

    def parse(self, soup):
        listaProduto = []
        results = soup.find_all('div', {'class':'ui-search-result__content-wrapper shops-custom-secondary-font'})
        for item in results:
            try:
                product = {
                    'titulo': item.find('h2', {'class':'ui-search-item__title'}).text,
                    'valor': float(item.find('span', {'class':'price-tag-fraction'}).text.replace('R$ ','').replace('.','')),
                    'qtd_pedidos' : int(item.find('span', {'class':'ui-search-reviews__amount'}).text),
                    'link' : item.find('a', href=True).get('href')
                }
            except:
                pass
            listaProduto.append(product)
        return listaProduto
    
    def best_product(self):
        
        self.search_ml()

        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        produtos = self.parse(soup)
        
        dados = pd.DataFrame(produtos)
        dados['titulo'] = dados['titulo'].str.lower()

        for index,row in dados.iterrows():
            dados.loc[index, "Score"] =  fuzz.token_set_ratio(self.search.lower(),dados.loc[index,"titulo"])
        
        dados.drop(index = dados[dados['Score'] < 60].index, axis = 1, inplace = True)

        media_valor = int(dados['valor'].mean())

        media_pedidos = int(dados['qtd_pedidos'].mean())

        dados['best'] = (dados['valor'] - media_valor) + (dados['qtd_pedidos'] - media_pedidos)

        best = dados.iloc[0].to_dict()

        best = json.dumps(best)

        self.driver.quit()

        return best