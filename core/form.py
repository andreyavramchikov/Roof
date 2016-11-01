from django import forms


class RequestEstimateForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your phone'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your address'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message', 'rows': 4}))
