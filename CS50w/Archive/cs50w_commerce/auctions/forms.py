from django import forms
from django.forms import ModelForm

from .models import Listing

class newListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'start_bid', 'image_url', 'category']

#         def form_valid(self, form):
            # form.instance.author = self.request.user
            # return form_valid(form)


    # title = forms.CharField(max_length=254)
    # description = forms.CharField(widget=forms.Textarea)
    # start_bid = forms.FloatField()
    # image_url = forms.URLField()
    # category = forms.CharField(widget=forms.Select(choices=Listings.category_choices))
