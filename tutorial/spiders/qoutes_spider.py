import scrapy


class QoutesSpiderSpider(scrapy.Spider):
    name = "qoutes_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        pass
