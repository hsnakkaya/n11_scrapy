# -*- coding: utf-8 -*-
import scrapy
from ..items import Product
from bs4 import BeautifulSoup


class ProductScraperSpider(scrapy.Spider):
    name = 'product_scraper'
    allowed_domains = ['n11.com']
    start_urls = ['http://n11.com/']

    def start_requests(self):
        url = 'https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?pg='
        for page in range(49):
            print(page)
            yield scrapy.Request(url=url + str(page+1), callback=self.parse)

    def parse(self, response):
        raw = response.body
        soup = BeautifulSoup(raw, 'html.parser')
        product = Product()

        items = soup.select("#view .column")
        print(len(items))

        for item in items:

            try:
                name = item.select("#view .productName")[0]
                name = name.text.strip()
                product['name'] = name
            except:
                pass

            try:
                note = item.select(".proSubTitle")[0]
                note = note.text.strip()
                product['note'] = note
            except:
                pass

            try:
                price = item.select("ins")[0]
                price = price.text.split(",")[0].replace('.', '')
                product['price'] = price
            except:
                pass

            try:
                url = item.find('a')['href']
                product['url'] = url
            except:
                pass

            try:
                seller_info = item.select(".sallerInfo")[0]
            except:
                pass

            try:
                seller_name = seller_info.select('.sallerName')[0]
                seller_name = seller_name.text.strip()
                product['seller_name'] = seller_name
            except:
                pass

            try:
                seller_rating = seller_info.select('.point')[0]
                seller_rating = seller_rating.text.strip().split("%")[1]
                product['seller_rating'] = seller_rating
            except:
                pass

            try:
                seller_url = seller_info['href']
                product['seller_url'] = seller_url
            except:
                pass

            yield product



