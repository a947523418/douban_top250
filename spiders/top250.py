# -*- coding: utf-8 -*-
import scrapy
from film.items import FilmItem

class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['https://movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        films = response.css('.item')
        for film in films:
            item = FilmItem()
            #item['ranking'] = film.xpath(".//div[@class='item']//em/text()").extract_first()
            item['ranking'] = film.css('em::text').extract_first()
            item['title'] = film.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            item['rating'] = film.css('.rating_num::text').extract_first()
            content = film.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            # 数据的处理
            for i_content in content:
                content_s = "".join(i_content.split())
                item['introduce'] = content_s
            yield item
            #title = film.css('.title::text').extract()
            #rating = film.css('.rating_num::text').extract_first()
        
        next = response.css('.paginator .next a::attr("href")').extract_first()
        if next:
            url = response.urljoin(next)
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)

