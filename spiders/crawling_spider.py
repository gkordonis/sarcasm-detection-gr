# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:00:54 2023

@author: tairo
"""

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
 
class CrawlingSpider(CrawlSpider):
    name = 'peterparker'
    allowed_domains = ['tokoulouri.com']
    start_urls = ['https://www.tokoulouri.com/']
    
    
    rules = (
        #Rule(LinkExtractor(allow="politics/"), callback='parse_item', follow=True)
        #,Rule(LinkExtractor(allow="international/"), callback='parse_item', follow=True)
        #,Rule(LinkExtractor(allow="science/"), callback='parse_item', follow=True)
        #,Rule(LinkExtractor(allow="economy/"), callback='parse_item', follow=True)
        #,Rule(LinkExtractor(allow="culture/"), callback='parse_item', follow=True)
        #,Rule(LinkExtractor(allow="sports/"), callback='parse_item', follow=True)
        #,Rule(LinkExtractor(allow="opinions/"), callback='parse_item', follow=True)
        Rule(LinkExtractor(allow="society/"), callback='parse_item', follow=True),
        )
    
    def parse_item(self, response):
        yield {
            'title':response.css('.single-post article header h1::text').get(),
            'date':response.css('.post-meta time::text').get()
            }