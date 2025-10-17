from pathlib import Path
from scrapy.loader import ItemLoader
from tut1.items import Book
import scrapy
from itemloaders.processors import TakeFirst


class QuotesSpider(scrapy.Spider):
    name = "books"
    images_folder_path = Path("images")

    start_urls = [
        "https://books.toscrape.com/",
    ]

    def parse(self, response):
        books = response.css(".product_pod")
        for book in books:
            l = ItemLoader(item=Book(), selector=book)
            l.default_output_processor = TakeFirst()
            l.add_css("name", "h3 a::attr(title)")
            l.add_css("price", "p.price_color::text")
            l.add_css("rating", ".star-rating::attr(class)")
            l.add_css("image_url", ".thumbnail::attr(src)")
            yield l.load_item()

        # book_name = book.css("h3 a").attrib["title"]
        # book_price = book.css("p.price_color::text").get()
        # book_rating = book.css(".star-rating").attrib["class"].split()[-1]
        # image_url = book.css(".thumbnail").attrib["src"]
        # image_full_url = response.urljoin(image_url)

        # yield scrapy.Request(
        #     image_full_url,
        #     callback=self.save_image,
        #     cb_kwargs={"book_name": book_name},
        # )
        # book = Book(
        #     name=book_name,
        #     price=book_price,
        #     rating=book_rating,
        #     image_url=image_full_url,
        # )

        # yield book

    # def save_image(self, response, book_name):
    #     self.log("Saving image " + book_name)
    #     file_ext = response.url.split(".")[-1]  # //meidan/asedakflekl.png
    #     with open(
    #         f"{QuotesSpider.images_folder_path}/{book_name}.{file_ext}",
    #         "wb",
    #     ) as f:
    #         f.write(response.body)
