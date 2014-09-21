# -*- coding: utf-8 -*-
from django import forms

class ImageDocumentForm(forms.Form):
    imgfile = forms.FileField(
        label='Select an image file',
        help_text='media/img/'
    )

class DocDocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select an doc file',
        help_text='media/doc/'
    )