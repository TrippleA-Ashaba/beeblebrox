import scrapy


class WwrSpiderSpider(scrapy.Spider):
    name = "wwr_spider"
    allowed_domains = ["weworkremotely.com"]
    start_urls = ["https://weworkremotely.com"]

    def parse(self, response):
        pass
