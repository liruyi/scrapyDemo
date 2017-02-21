# -*- coding: utf-8 -*-

import scrapy
from jiandan.items import JiandanItem
from scrapy.crawler import CrawlerProcess


class jiandanSpider(scrapy.Spider):
    name = "jiandan"
    allowed_domains = []
    # start_urls = ["http://jandan.net/ooxx"]
    start_urls = ["http://www.topit.me/"]
    def parse(self, response):
        item = JiandanItem()
        url = response.xpath('//img//@src').extract()  # 提取图片链接
        item['image_urls'] = url
        # item['image_urls'] = response.xpath('//img//@src').extract()  # 提取图片链接
        print 'image_urls', item['image_urls']
        yield item
        #new_url = response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()  # 翻页
        new_url = response.xpath('//*[@id="page-next"]//@href').extract_first()
        print 'new_url', new_url
        if new_url:
            yield scrapy.Request(new_url,callback=self.parse)