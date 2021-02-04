from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
max_length_field = 128
max_length_URL = 200

class Category(models.Model):
    name = models.CharField(max_length=max_length_field, unique=True)    
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    #SlugField : Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)
    
    class Meta: #this will help to fix if singular form of word is entered
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
    

    
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=max_length_field)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title