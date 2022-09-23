from socket import fromshare
from django import forms
class API(forms.Form):
    required_field=forms.CharField(max_length=100)