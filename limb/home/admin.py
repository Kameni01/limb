from django.contrib import admin
from home.models import News, Category, Tag

# Register your models here.
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)