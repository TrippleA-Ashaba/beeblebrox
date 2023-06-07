import scrapy


class BrightermondaySpiderSpider(scrapy.Spider):
    name = "brightermonday_spider"
    allowed_domains = ["www.brightermonday.co.ug"]
    start_urls = ["https://www.brightermonday.co.ug/"]

    def parse(self, response):
        pass
