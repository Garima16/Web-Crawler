from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector

from scrapy.item import Item, Field


class PlayGroundItem(Item):
    title = Field()
    url = Field()
    download_url = Field()


class PlayGroundLoader(XPathItemLoader):
    default_output_processor = TakeFirst()


class PlayGroundSpider(CrawlSpider):
    name = "playground_spider"
    allowed_domains = ["www.playground.ru"]
    start_urls = ["http://www.playground.ru/files/stalker_clear_sky/"]
    rules = (
        Rule(SgmlLinkExtractor(allow=('/files/s_t_a_l_k_e_r_chistoe_nebo')), follow=True, callback='parse_item'),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        l = PlayGroundLoader(PlayGroundItem(), hxs)
        l.add_value('url', response.url)
        l.add_xpath('title', "//div[@class='downloads-container clearfix']/h1/text()")
        l.add_xpath('download_url', "//div[@class='files-download-holder']/div/a/@href")

        return l.load_item()
