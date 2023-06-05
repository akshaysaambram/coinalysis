from django import forms
from .models import Order


class BuyForm(forms.ModelForm):

    quantity = forms.IntegerField(min_value=1, required=True)

    class Meta:

        model = Order
        fields = ['quantity']
