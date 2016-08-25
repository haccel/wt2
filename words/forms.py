from django import forms

class WordsForm(forms.Form):
    native_word = forms.CharField(label='Native word', max_length=100)