from django.forms import ModelForm
from .models import Comments
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
