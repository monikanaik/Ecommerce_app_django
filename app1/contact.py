from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    Message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )