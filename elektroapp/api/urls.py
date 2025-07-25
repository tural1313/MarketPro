from django.urls import path
from elektroapp.api import views


urlpatterns = [
   
    path('banner-list/', views.BannerListAPIView.as_view()),
    
    path('top-item-list/', views.TopItemListAPIView.as_view()),
    path('top-item-create/', views.TopItemCreateListAPIView.as_view()),
    path('top-item-update/<int:id>/', views.TopItemUpdateListAPIView.as_view()),
    
    path('category-list/',views.CategoryListAPIView.as_view()),
    
    path('collection-list/', views.CollectionListAPIView.as_view()),
    path('collection-update/<int:id>/', views.CollectionUpdateListAPIView.as_view()), 
    
    path('market-list/',views.MarketListAPIView.as_view()),
    
    path('items-list/', views.ItemsListAPIView.as_view()),   
    path('items-update/<int:id>/', views.ItemsUpdateListAPIView.as_view()), 
    
    path('double-item-list/', views.DoubleItemListAPIView.as_view()),
    
    path('item-here-list/', views.ItemHereListAPIView.as_view()), 
    
    path('Author-list/', views.AuthorListAPIView.as_view()),
    
    path('wishlist-list/', views.WishlistListAPIView.as_view()),
    
    path('current-prices-list/', views.CurrentPricesListAPIView.as_view()),
    
    path('singer-items-list/', views.SingerItemsListAPIView.as_view()),
    
    path('create-list/', views.CreateListAPIView.as_view()),
    path('create-update/', views.CreateUpdateAPIView.as_view()),
    path('create-retrieve/', views.CreateRetrieveAPIView.as_view()),
    
    path('settings/', views.SiteSettingsListAPIView.as_view()),  
]