from django.forms import ModelForm
from .models import Comments

"""Forma commentariev na site"""
class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text', )
        widgets = {
            #'foo' = SummernoteWidget()
            'text' = SummernoteInplaceWidget()
        }
