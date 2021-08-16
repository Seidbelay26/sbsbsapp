from django import forms
from django.forms import fields, widgets
from books.models import Review
#class ReviewForm(forms.Form):
    #body=forms.CharField(widget=forms.Textarea(attrs={'class':'border round p-2 w-full', 'placeholder':'write your review here'}))
    #images=forms.ImageField(required=False)

class ReviewForm(forms.ModelForm):
    body=forms.CharField(widget=forms.Textarea(attrs={'class':'border round p-2 w-full', 'placeholder':'write your review here'}))
    images=forms.ImageField(required=False)
    class Meta:
        model = Review
        fields=['body', 'images']
