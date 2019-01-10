from django.contrib import admin
from home.models import News, Category, Tag
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class NewsAdmin(SummernoteModelAdmin):
    summer_note_fields = ('text_min', 'text')


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tag)
