from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from elektroapp.models import SiteSettings,Banner, TopItem, Category, Collection, Market, Wishlist, Create, SingerItems, Author, CurrentPrices, Items, DoubleItem, ItemHere
from elektroapp.api.serializers import (BannerSerializer, TopItemSerializer, CategorySerializer, 
    CollectionSerializer, MarketSerializer, ItemsSerializer, DoubleItemSerializer, ItemHereSerializer, AuthorSerializer,
    WishlistSerializer, CurrentPricesSerializer, SingerItemsSerializer, CreateSerializer,  SiteSettingsSerializer, 
)



class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    
    
class TopItemListAPIView(ListAPIView):
    queryset = TopItem.objects.all()
    serializer_class = TopItemSerializer
    
    
class TopItemCreateListAPIView(CreateAPIView):
    queryset = TopItem.objects.all()
    serializer_class = TopItemSerializer
    
    
class TopItemUpdateListAPIView(UpdateAPIView):
    queryset = TopItem.objects.all()
    serializer_class = TopItemSerializer
    lookup_field = "id"
    
    
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class CollectionListAPIView(ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
    
class CollectionUpdateListAPIView(UpdateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = "id"
    
    
class MarketListAPIView(ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    
    
class ItemsListAPIView(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    
    
class ItemsUpdateListAPIView(UpdateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    lookup_field = "id"
    
    
class DoubleItemListAPIView(ListAPIView):
    queryset = DoubleItem.objects.all()
    serializer_class = DoubleItemSerializer
    
    
class ItemHereListAPIView(ListAPIView):
    queryset = ItemHere.objects.all()
    serializer_class = ItemHereSerializer
    
    
class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class WishlistListAPIView(ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    
    
class CurrentPricesListAPIView(ListAPIView):
    queryset = CurrentPrices.objects.all()
    serializer_class = CurrentPricesSerializer
    
    
class SingerItemsListAPIView(ListAPIView):
    queryset = SingerItems.objects.all()
    serializer_class = SingerItemsSerializer
    
    
class CreateListAPIView(ListAPIView):
    queryset = Create.objects.all()
    serializer_class = CreateSerializer
    
    
class CreateUpdateAPIView(UpdateAPIView):
    queryset = Create.objects.all()
    serializer_class = CreateSerializer
    lookup_field = "id"
    
    
class CreateRetrieveAPIView(RetrieveAPIView):
    queryset = Create.objects.all()
    serializer_class = CreateSerializer
    lookup_field = "id"
    

class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer