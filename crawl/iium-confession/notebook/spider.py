import scrapy

class BlogSpider(scrapy.Spider):
    name = 'uuim'
    start_urls = ['https://iiumc.com/']
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'iium.csv'
    }

    def parse(self, response):
        for title in response.css('article'):
            yield {'title': title.get()}
        for next_page in response.css('a.page-numbers'):
            yield response.follow(next_page, self.parse)