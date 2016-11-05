from django import forms


class RequestEstimateForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your phone'}), max_length=10)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your email'}), max_length=30)
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your address'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message', 'rows': 4}))


class ContactUsForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}), max_length=10)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), max_length=30)
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': 4}))
