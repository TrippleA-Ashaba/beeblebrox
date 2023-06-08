import os

import scrapy
from dotenv import load_dotenv

load_dotenv()


class BrightermondaySpiderSpider(scrapy.Spider):
    name = "brightermonday_spider"
    allowed_domains = os.environ.get("BRIGHTERMON_DOMAIN").split(",")
    start_urls = os.environ.get("BRIGHTERMON_URLS", "").split(",")

    custom_settings = {
        "FEEDS": {
            "brightermon_listings.json": {
                "format": "json",
                "encoding": "utf8",
                "overwrite": True,
            }
        }
    }

    def parse(self, response):
        for listing in response.css('div[data-cy="listing-cards-components"]'):
            title = listing.css("a::attr(title)").get()
            company = listing.css("p.text-sm.text-link-500::text").get()

            if company is not None:
                company = company.strip()
            else:
                company = "Brighter Monday"

            region = listing.css("div span::text").get().strip()
            urls = [listing.css("a::attr(href)").get()]

            yield {
                "title": title,
                "company": company,
                "region": region,
                "urls": urls,
            }
