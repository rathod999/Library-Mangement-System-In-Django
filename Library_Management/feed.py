from django.contrib.syndication.views import Feed
from django.urls import reverse
from Management.models import Book

class LatestEntriesFeed(Feed):
    title="E-Library"
    link="/feed/"
    description= "Following are Latest Book Available."
    
    def items(self):
        return Book.objects.order_by('-id')[:2]
    
    def items_title(self, item):
        return item.title
    
    def items_summary(self, item):
        return item.summary
    #link to url of news book.
    def item_link(self, item):
        return item.get_absolute_url()
