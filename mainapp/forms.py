from django import forms
from .models import Order


class BuyForm(forms.ModelForm):

    class Meta:

        model = Order
        fields = ['quantity']