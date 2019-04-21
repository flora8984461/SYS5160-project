# -*- coding: utf-8 -*-

from django import forms


class MatrixForm(forms.Form):
    matrix = forms.CharField(required = False, max_length= 1000, widget=forms.Textarea)
    #matrix = forms.FloatField(required = False, max_value=100, widget=forms.Textarea)
