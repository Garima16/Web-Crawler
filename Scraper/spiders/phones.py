# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.crawler import CrawlerProcess
import json


class AmazonPhonesSpider(scrapy.Spider):
    browser = webdriver.Chrome()
    browser.get('http://www.amazon.in/')
    try:
        search_element = browser.find_element_by_id('twotabsearchtextbox')
        phone_name = 'Moto G4 Plus'
        search_element.send_keys(phone_name)
        search_element.submit()
        next_url = browser.current_url
    except:
        print 'No such element'

    name = "amazon_phones"
    allowed_domains = ["http://www.amazon.in/"] # ['https://www.flipkart.com/']
    start_urls = (
        next_url,
    )

    def parse(self, response):
        next_url = response.xpath('//a[@class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/@href').extract_first()
        price = response.xpath('//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()').extract()
        # model_name = response.xpath('//h2[@class="a-size-base s-inline  s-access-title  a-text-normal"]/text()').extract()
        yield {'price at Amazon': price}
        yield scrapy.Request(next_url, callback=self.next_url_parse, dont_filter=True)

    def next_url_parse(self, response):
        # price = response.xpath('//span[@class="a-size-medium a-color-price"]/text()').extract()[-1]
        model_name = response.xpath('//span[@class="a-size-large"]/text()').extract_first()
        yield {'Amazon model_name': model_name}


class FlipkartPhonesSpider(scrapy.Spider):
    browser = webdriver.Chrome()
    browser.get('https://www.flipkart.com/')
    try:
        search_element = browser.find_element_by_class_name('LM6RPg')
        phone_name = 'Moto G4 Plus'
        search_element.send_keys(phone_name)
        search_element.submit()
        next_url = browser.current_url
    except:
        print 'No such element'

    name = "flipkart_phones"
    allowed_domains = ["https://www.flipkart.com/"] # ['https://www.flipkart.com/']
    start_urls = (
        next_url,
    )

    def parse(self, response):
        data = json.loads(response.body)
        html = data['html']
        selector = scrapy.Selector(text=data['html'], type="html")
        relative_url = selector.xpath('//a[@class="_2cLu-l"]/@href').extract_first()
        print "relative url is %s" % relative_url
        # model_name = response.xpath('//a[@class="_2cLu-l"]/text()').extract()
        # price = response.xpath('//div[@class="_1vC4OE"]/text()').extract()
        absolute_url = response.urljoin(relative_url)
        print "absolute url is %s" % absolute_url
        yield scrapy.Request(absolute_url, callback=self.next_url_parse, dont_filter=True)

    def next_url_parse(self, response):
        model_name = response.xpath('//h1[@class="_3eAQiD"]/text()').extract()
        price = response.xpath('//div[@class="_1vC4OE _37U4_g"]/text()').extract()
        yield {'price at flipkart': price, 'model_name': model_name}
        # specs = response.xpath('//li[@class="_2-riNZ"]/text()').extract()

process = CrawlerProcess()
process.crawl(AmazonPhonesSpider)
process.crawl(FlipkartPhonesSpider)
process.start()
