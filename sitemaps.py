from django.contrib.sitemaps import Sitemap
from myproject.python.models import Posts, Categories

class PostsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Posts.objects.all()

    def lastmod(self, obj):
        return obj.post_pubdate

class CategoriesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Categories.objects.all()

#    def lastmod(self, obj):
#        return obj.post_pubdate

