import os

import scrapy
from dotenv import load_dotenv
from jobcrawler.items import JobcrawlerItem as R

load_dotenv()


class RemoteioSpiderSpider(scrapy.Spider):
    name = "remoteio_spider"
    allowed_domains = os.environ.get("REMOTEIO_DOMAIN").split(",")
    start_urls = os.environ.get("REMOTEIO_URLS", "").split(",")

    custom_settings = {
        "FEEDS": {
            "remoteio_listings.json": {
                "format": "json",
                "encoding": "utf8",
                "overwrite": True,
            }
        }
    }

    # def parse(self, response):
    #     for title in response.css('div.flex-grow a[data-title="true"]::text').getall():
    #         yield {"title": title}
    def parse(self, response):
        JOB = R()
        for listing in response.css("div.w-full")[1:]:
            JOB["title"] = listing.css(
                'a.text-lg.text-black[data-title="true"]::text'
            ).get()
            JOB["company"] = listing.css("p[data-text]::text").get()
            JOB["region"] = listing.css('a.px-2[data-tag="true"]::text').get()
            JOB["urls"] = [
                response.urljoin(
                    listing.css(
                        'a.text-lg.text-black[data-title="true"]::attr(href)'
                    ).get()
                )
            ]

            yield JOB
