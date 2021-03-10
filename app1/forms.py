from django import forms


class DetailsForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    city=forms.CharField()
    address=forms.CharField(widget=forms.Textarea)