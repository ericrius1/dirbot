from scrapy.item import Item, Field


class Website(Item):

    postId = Field()
    postContent = Field()
    description = Field()
	
    def __str__(self):
        return "Website: name=%s url=%s" % (self.get('name'), self.get('url'))
