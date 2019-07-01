# -*- coding: utf-8 -*-

# Usage:
# scrapy crawl BBC_Responder -a chapter=sport -a news=12
# scrapy crawl BBC_Responder -a chapter=sport -a news=12 -s LOG_FILE=BBC.log >> BBC.txt
# scrapy crawl BBC_Responder -a chapter=travel -a news=12 -s LOG_FILE=BBC.log >> BBC.txt

import scrapy
import logging
from scrapy.exceptions import CloseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime
import scrapy, json, sys
from w3lib.html import remove_tags



class BBC_ResponderSpider(CrawlSpider):

# Set spider name
    name = 'BBC_Responder'
#    postfix='sport'

# set domain for parsing
    allowed_domains = ['bbc.com']



# Init constructor    
    def __init__(self, category=None, *args, **kwargs):


# Set parameters
      self.chapter = kwargs['chapter']

# Set start path for grabing
      self.start_urls = ['http://www.bbc.com/'+self.chapter+'/']

# Setup maximum allowed urls for download from page
      self.maxAllowedURL=int(kwargs['news'])

# Init links counter
      self.linksCounter=0

# Set allow path
      allowPath=r'/'+self.chapter

# Create rule for parsing links on page
      self.rules = (
#        Rule(LinkExtractor(allow=r'/'+postfix), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=allowPath), callback='parse_item', follow=True),

    )
# Call native constructor
      super(BBC_ResponderSpider, self).__init__(*args, **kwargs)




# Parse scraped items
    def parse_item(self, response):
        i={}
# Extract all titles and urls  for page and print it 
        extractor = LinkExtractor(deny_domains=self.allowed_domains[0])

# Get title values
        i['title']=remove_tags(str(response.css('title').get()).encode("utf-8"))

# Setup variable for returning
        i['url']=response.url
# Finish spider if maximum download maxAllowedURL is achived
        if (self.linksCounter >= self.maxAllowedURL ):
# Finish application      
          raise CloseSpider('maxAllowedURL is achived linksCounter='+str(self.linksCounter))
# increment link counter
        self.linksCounter+=1
# Output grabed content
        print(i)
#        print(self.ArticlesBuffer)
        return i
