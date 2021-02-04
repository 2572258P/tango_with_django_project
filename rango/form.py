# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:17:06 2021

@author: JungshicPark
"""


from django import forms
from rango.models import Page, Category,max_length_field,max_length_URL

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=max_length_field,
                          help_text = "Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta: #a class to provide additional information on the form
        model = Category #a reference for Category model
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=max_length_field,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length = max_length_URL,
                         help_text="Please enter URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    
    class Meta:
        model = Page #a reference for page model
        exclude = ('category',)
        
        
    def clean(self): #this is how we can clean data before being stored
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data  
        
        
        
        
        