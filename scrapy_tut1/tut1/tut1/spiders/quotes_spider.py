from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # async def start(self):
    #     urls = [
    #         "https://quotes.toscrape.com/page/1/",
    #         "https://quotes.toscrape.com/page/2/",
    #         "https://quotes.toscrape.com/page/3/",
    #         "https://quotes.toscrape.com/page/4/",
    #         "https://quotes.toscrape.com/page/5/",
    #         "https://quotes.toscrape.com/page/6/",
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    start_urls = [
        "https://quotes.toscrape.com/",
    ]

    def parse(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            yield {
                "text": text,
                "author": author,
                "tags": tags,
            }

        self.log("######## Parsed " + response.url)
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            yield response.follow(next_page, callback=self.parse)

        self.log("### ended parsing all pages")
