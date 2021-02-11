from django.contrib import admin

# Register your models here.

from django.contrib import admin
from rango.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_Fields = {'slug':('name',)}
    
class UserProfileAdmin(admin.ModelAdmin):
    prepopulated_Fields = ('website','picture')
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
