from django import forms
from oscar.core.loading import get_class, get_model
CoreBillingAddressForm = get_class('payment.forms', 'BillingAddressForm')


class StripeTokenForm(forms.Form):
    stripeEmail = forms.EmailField(widget=forms.HiddenInput())
    stripeToken = forms.CharField(widget=forms.HiddenInput())


class BillingAddressForm(CoreBillingAddressForm):
    class Meta(CoreBillingAddressForm.Meta):
        fields = [
            'title', 'first_name', 'last_name',
            'line1', 'line2', 'line3', 'line4',
            'state', 'postcode', 'country',
            'phone_number',
        ]