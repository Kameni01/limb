from django.contrib import admin
from home.models import News, Category, Tag, Comments
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class NewsAdmin(SummernoteModelAdmin):
    list_display = ("title", "user", "created")
    list_editable = ("user", )
    list_filter = ("user", "created")
    search_fields = ("title", "user__username")
    summer_note_fields = ('text_min', 'text')


admin.site.register(News, NewsAdmin)

admin.site.register(Category)
admin.site.register(Tag)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')

admin.site.register(Comments, CommentAdmin)
