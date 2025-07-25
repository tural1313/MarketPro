from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='banner_imgs/')
    link = models.URLField(max_length=256)
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name
    
    
class TopItem(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    image_1 = models.ImageField(upload_to='topitem_imgs/')
    image_2 = models.ImageField(upload_to='topitem_imgs/')
    link = models.URLField(max_length=256)
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name='topitem')
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name
    
    
        
class Category(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name
    
    
class Collection(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='collection_imgs/')
    items_collection = models.IntegerField(default=0)
    collection_category = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name
    
    
class Market(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    logo = models.CharField(max_length=50)
    link = models.URLField(max_length=256)
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name
    
    
class Items(models.Model):
    name = models.CharField(max_length=50)
    image_1 = models.ImageField(upload_to='items_imgs/')
    image_2 = models.ImageField(upload_to='items_imgs/')
    link = models.URLField(max_length=256)
    current_bid = models.BooleanField(default=0)
    price = models.BooleanField(default=0)
    data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Items"
        
    def __str__(self):
        return self.name
    
    
class DoubleItem(models.Model):
    name = models.CharField(max_length=50)
    image_1 = models.ImageField(upload_to='doubleitem_imgs/')
    image_2 = models.ImageField(upload_to='doubleitem_imgs/')
    current_bid = models.BooleanField(default=0)
    category = models.CharField(max_length=50)
    collection = models.IntegerField(default=0)
    data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name
    
    
class ItemHere(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    image_1 = models.ImageField(upload_to='itemhere_imgs/')
    image_2 = models.ImageField(upload_to='itemhere_imgs/')
    link = models.URLField(max_length=256)
    price = models.BooleanField(default=0)
    midle_name = models.CharField(60)
    data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=256)
    image = models.ImageField(upload_to='author_imgs/')
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name
    
    
class Wishlist(models.Model):
    like = models.IntegerField(default=0)
    follower = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='wishlist')
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name
    
    
class CurrentPrices(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='currentprices_imgs/')
    link = models.URLField(max_length=256)
    data = models.DateTimeField(default=0)
    price = models.BooleanField(default=0)
    
    class Meta:
        verbose_name_plural = "CurrentPrices"
        
    def __str__(self):
        return self.name
    
    
    
class SingerItems(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='singeritem_imgs/')
    fon_image = models.ImageField(upload_to='singeritem_imgs/')
    price = models.BooleanField(default=0)
    data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "SingerItems"
        
    def __str__(self):
        return self.name
    
    
class Create(models.Model):
    ttle = models.CharField(max_length=200)
    content = models.TextField()
    username = models.CharField(max_length=70)
    price = models.BooleanField(default=0)
    interest = models.BooleanField(default=0)
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name
    
    
class SiteSettings(models.Model):
    logo = models.TextField(blank=True, null=True)
    
    midle_name_category = models.TextField(blank=True, null=True)
    midle_name_collection = models.TextField(blank=True, null=True)
    
    midle_name_items = models.TextField(blank=True, null=True)
    midle_content_items = models.TextField(blank=True, null=True)
    
    midle_name_our = models.TextField(blank=True, null=True)
    our_name = models.TextField(blank=True, null=True)
    our_image = models.ImageField(upload_to='settings_imgs/', blank=True, null=True)
    oure_price = models.BooleanField(default=0, blank=True, null=True)
    our_data = models.DateTimeField(default=0, blank=True, null=True)
    
    detail_name = models.TextField(blank=True, null=True)
    detail_content = models.TextField(blank=True, null=True)
        
    midle_name_detail = models.TextField(blank=True, null=True)
    midle_name_market = models.TextField(blank=True, null=True)
    midle_name_author = models.TextField(blank=True, null=True)
    
    midle_content_author = models.TextField(blank=True, null=True)
    
    midle_name_create = models.TextField(blank=True, null=True)
    midle_content_create = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"  
        
    def __str__(self):
        return "Settings"
    
    
    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            return None
        return super(SiteSettings,self).save(*args,**kwargs)
        
    
    
    
    
    
    
    
    
    
    
    