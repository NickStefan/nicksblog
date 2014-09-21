# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    imgfile = forms.FileField(
        label='Select an image file',
        help_text='media/img/'
    )
    jsfile = forms.FileField(
        label='Select a js file',
        help_text='media/js/'
    )
    docfile = forms.FileField(
        label='Select other doc file',
        help_text='media/doc/'
    )