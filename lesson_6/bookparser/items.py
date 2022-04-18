import scrapy


class BookparserItem(scrapy.Item):
    link = scrapy.Field()
    name = scrapy.Field()
    authors = scrapy.Field()
    price = scrapy.Field()
    discount_price = scrapy.Field()
    rating = scrapy.Field()
    _id = scrapy.Field()