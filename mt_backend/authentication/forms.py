from allauth.account.forms import SignupForm
from django import forms
from authentication.models import Customer

orgs = (("1", "Meta"), ("2", "Apple"), ("3", "Amazon"),)


class CustomSignupForm(SignupForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    organization = forms.ChoiceField(choices=orgs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        return user
