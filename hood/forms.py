from django import forms
from .models import Businesses, Posts, Profile, NeighbourHood

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['profile','pub_date', 'poster_id']


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'userId']


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Businesses
        exclude = ['user']