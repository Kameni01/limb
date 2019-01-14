from django.forms import ModelForm
from .models import Comments, News
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

"""Forma commentariev na site"""
class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text', )
        widgets = {
            'text' : SummernoteWidget(),
            #'text' : SummernoteInplaceWidget()
        }

class PostForm(ModelForm):
    class Meta:
        model = News
        fields = ('category', 'title', 'text_min', 'text', 'tags', 'description', 'keywords')
        widgets = {
            'text' : SummernoteWidget(),
            #'text' : SummernoteInplaceWidget()
        }
