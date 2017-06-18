from django import forms

class TweetForm(forms.Form):

    msg = forms.CharField()
