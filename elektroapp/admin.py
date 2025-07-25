from django.contrib import admin
from elektroapp.models import ( Banner, TopItem, Category, Collection, Market, Wishlist, Create, SingerItems,
Author, CurrentPrices, Items, DoubleItem, ItemHere,  SiteSettings,
)

admin.site.register(Banner)
admin.site.register(TopItem)
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Market)
admin.site.register(Wishlist)
admin.site.register(Create)
admin.site.register(SingerItems)
admin.site.register(Author)
admin.site.register(CurrentPrices)
admin.site.register(Items)
admin.site.register(DoubleItem)
admin.site.register(ItemHere)
admin.site.register(SiteSettings)
