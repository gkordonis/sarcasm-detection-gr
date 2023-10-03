# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 09:29:57 2023

@author: tairo
"""


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#from fake_useragent import UserAgent

 
class CrawlingSpider(CrawlSpider):
    name = 'milesmorales'
    allowed_domains = ['tovatraxi.com']
    start_urls = ['https://tovatraxi.com/']
    DOWNLOAD_DELAY = 2.5
#    USER_AGENT = 'foititis-lulilo'

    
    
    rules = (
        Rule(LinkExtractor(allow="politics"), callback='parse_item', follow=True)
        ,Rule(LinkExtractor(allow="social"), callback='parse_item', follow=True)
        ,Rule(LinkExtractor(allow="world"), callback='parse_item', follow=True)
        ,Rule(LinkExtractor(allow="science"), callback='parse_item', follow=True)
        ,Rule(LinkExtractor(allow="art"), callback='parse_item', follow=True)
        ,Rule(LinkExtractor(allow="entertainment"), callback='parse_item', follow=True)
        ,Rule(LinkExtractor(allow="specials"), callback='parse_item', follow=True)
        ,Rule(LinkExtractor(allow="business"), callback='parse_item',follow=True),
        )
    
    def parse_item(self, response):
        yield {
            #'title':response.css('.post article header h1::text').get(),
            'title':response.css('.post header h1::text').get(),
            'date':response.css('.post-meta time::text').get()
            }