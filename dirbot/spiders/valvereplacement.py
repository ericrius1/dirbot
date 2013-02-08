from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from dirbot.items import Website
import csv

class ValveReplacementSpider(CrawlSpider):
    name = 'valvereplacement'
    allowed_domains = ['valvereplacement.org']
    start_urls = [
                  #"http://www.valvereplacement.org/forums/showthread.php?39209-Replacement-valve-failing-why",
                  #"http://www.valvereplacement.org/forums/showthread.php?41238-BUMMED-OUT-Juicing-Vitamin-K-etc",
                  #"http://www.valvereplacement.org/forums/showthread.php?27126-Coumadin-amp-Teeth"
                  "http://www.valvereplacement.org/forums/forumdisplay.php?12-Post-Surgery",
                  "http://www.valvereplacement.org/forums/forum.php"
                ]
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=('forumdisplay\.php', )), callback='parse_metapage' ),

        Rule(SgmlLinkExtractor(allow=('showthread\.php', )), callback = 'parse_metapage' ),
     
    )

 
        
   

    def parse_metapage(self, response):
        hxs = HtmlXPathSelector(response)
        print ("JUST FOLLOWED A PAGE")
        

    def parse(self, response):
        print "ShNUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUR"
        hxs = HtmlXPathSelector(response)
        items = []
        posts = hxs.select('//div[contains(@id, "post_message")]')
        for post in posts:
            item = Website()
            item['postId']= post.select('@id').extract()
            item['postContent'] = post.select('.//blockquote[contains(@class, "postcontent restore")]/text()').extract()
            item['description'] = "shnur"
            items.append(item)
        return items


         
