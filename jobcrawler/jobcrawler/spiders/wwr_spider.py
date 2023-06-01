import os

import scrapy
from dotenv import load_dotenv

load_dotenv()


class WwrSpiderSpider(scrapy.Spider):
    name = "wwr_spider"
    allowed_domains = os.environ.get("WWR_DOMAIN").split(",")
    start_urls = os.environ.get("WWR_URLS", "").split(",")

    custom_settings = {
        "FEEDS": {
            "wwr_listings.json": {
                "format": "json",
                "encoding": "utf8",
                "overwrite": True,
            }
        }
    }

    def parse(self, response):
        for listing in response.css("section.jobs article ul li")[1:-1]:
            region = listing.css("span.region::text").get(default="N/A")
            desired_region = "Anywhere in the World"

            if region == desired_region:
                title = listing.css("span.title::text").get(default="N/A")
                company = listing.css("span.company::text").get(default="N/A")
                urls = [
                    response.urljoin(url)
                    for url in listing.css("a::attr(href)").getall()
                ]

                yield {
                    "title": title,
                    "company": company,
                    "region": region,
                    "urls": urls,
                }
