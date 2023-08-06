from django import forms
from .models import Book


class BookUpdateForm(forms.ModelForm):
    author= forms.CharField(required=False)
    title= forms.CharField(required=False)
    summary = forms.CharField(widget=forms.Textarea(attrs={"rows":3 }),required=False)
    class Meta:
        model=Book
        fields=['title','author','genre','store_url','is_visible','summary']

class BookCreationForm(forms.ModelForm):
    title= forms.CharField(required=False)
    class Meta:
        model=Book
        fields=['title','store_url','is_visible','pdf']

