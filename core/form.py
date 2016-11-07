from django import forms


class RequestEstimateForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your phone'}), max_length=10, required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your email'}), max_length=30, required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your address'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message', 'rows': 4}), required=True)


class ContactUsForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}), required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}), max_length=10, required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), max_length=30, required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': 4}), required=False)
