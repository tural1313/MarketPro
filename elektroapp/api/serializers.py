from rest_framework import serializers
from elektroapp.models import ( SiteSettings, Banner, TopItem, Category, Collection, Market, Items, DoubleItem,
  ItemHere, Author, Wishlist, CurrentPrices, SingerItems, Create 
  
)



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
        

class TopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopItem
        fields = "__all__"
        
        
class TopItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopItem
        fields = "__all__"
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
        
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"
        
        
class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = "__all__"
        
        
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"
        
        
class DoubleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubleItem
        fields = "__all__"
        
        
        
class ItemHereSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemHere
        fields = "__all__"
        
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        
        
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"
        
        
class CurrentPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentPrices
        fields = "__all__"
        
        
class SingerItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingerItems
        fields = "__all__"
        
        
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Create
        fields = "__all__"
        
        
           
class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"