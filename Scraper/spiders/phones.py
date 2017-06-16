# -*- coding: utf-8 -*-
import scrapy
prices = []


class PhonesSpider(scrapy.Spider):
    name = "phones"
    allowed_domains = ['https://www.flipkart.com/'] # ["http://www.amazon.in/"]
    start_urls = (
        # 'http://www.amazon.in/Moto-Plus-4th-Gen-Black/dp/B01DDP87N0/ref=sr_1_1?s=electronics/',
        # 'http://www.amazon.in/Moto-Play-4th-Gen-Black/dp/B01FM7GIR4/ref=sr_1_1?s=electronics/',
        'https://www.flipkart.com/moto-x-style-black-16-gb/p/itmeuyd8zfrgkdkz?pid=MOBEAJTQ4QEAJZ2H&srno=s_1_3&otracker=search&lid=LSTMOBEAJTQ4QEAJZ2HXQE1E0&qH=baf47101454208af',
    )

    def parse(self, response):
        # try:
        #     price = response.xpath('//span[@class="a-size-medium a-color-price"]/text()').extract()[6]
        # except IndexError:
        #     price = response.xpath('//span[@class="a-size-medium a-color-price"]/text()').extract()[0]
        # prices.append(price)
        # print "Prices of phones:%s" % prices
        # # print price
        # price = response.xpath('//div[@class="_1vC4OE _37U4_g"]/text()').extract()[1]
        specs = response.xpath('//li[@class="_2-riNZ"]/text()').extract()
        print "specs=%s" % specs
