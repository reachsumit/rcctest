from django import forms
from rccproj.webapp.models import Bikes

class bikeForm(forms.ModelForm):
    SKU = forms.CharField(max_length=17,help_text="Please enter a unique SKU id.",required=True)
    name = forms.CharField(max_length=50,help_text="Name of the bike;",required=True)
    description = forms.CharField(max_length=180,help_text="Description for the bike",initial="No description available.")
    rating = forms.DecimalField(max_digits=4,help_text="Ratings",decimal_places=2,initial=0.0)
    price = forms.DecimalField(max_digits=5,decimal_places=2,help_text="Price",initial=0.0,required=True)
    quantity = forms.IntegerField(initial=0,help_text="Quantity")
    type = forms.CharField(max_length=25,help_text="Type of bike")
    image = forms.URLField(max_length=250,help_text="URL of image")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bikes
        fields = '__all__'

