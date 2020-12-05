import scrapy


class SogouspiderSpider(scrapy.Spider):
    name = 'sogouspider'
    allowed_domains = ['weixin.sogou.com']
    # start_urls = ['http://weixin.sogou.com/']
    start_urls = ['https://weixin.sogou.com/weixin?type=2&query=篮球']

    def parse(self, response):
        pass
