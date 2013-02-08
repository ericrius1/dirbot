from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from dirbot.items import Website

class ValveReplacementSpider(CrawlSpider):
    name = 'valvereplacement'
    allowed_domains = ['valvereplacement.org']
    start_urls = ['http://www.valvereplacement.org/forums/forum.php'
                ]
                  


    def parse(self, response):

        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//li/text()')
        strings = []
        items = []
        file = open('test.txt', 'w')
        for site in sites:
            file.write(site.extract())
        file.close()
            
            
        
