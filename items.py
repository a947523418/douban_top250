# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmItem(scrapy.Item):
    ranking = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    introduce = scrapy.Field()


