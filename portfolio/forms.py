from django import forms
from .models import Portfolio

class PortfolioPost(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name', 'image', 'description']

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['image'].required = False