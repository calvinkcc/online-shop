from django.conf import settings
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views import generic

from oscar.core.loading import get_model, get_class
from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView
from oscar.apps.checkout.views import ShippingAddressView as CoreShippingAddressView
from oscar.apps.checkout.views import IndexView as CoreIndexView

from yourappsfolder.checkout.facade import Facade
from yourappsfolder.checkout import forms

from . import PAYMENT_METHOD_STRIPE, PAYMENT_EVENT_PURCHASE, STRIPE_EMAIL, STRIPE_TOKEN
from .models import Contact

SourceType = get_model('payment', 'SourceType')
Source = get_model('payment', 'Source')
UserAddress = get_model('address', 'UserAddress')


CheckoutSessionMixin = get_class('checkout.session', 'CheckoutSessionMixin')
CodeIndexView = get_class('checkout.views', 'IndexView')
BillingAddressForm = get_class("checkout.forms", "BillingAddressForm")


class PaymentDetailsView(CorePaymentDetailsView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PaymentDetailsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(PaymentDetailsView, self).get_context_data(**kwargs)
        if self.preview:
            ctx['stripe_token_form'] = forms.StripeTokenForm(self.request.POST)
            ctx['order_total_incl_tax_cents'] = (
                ctx['order_total'].incl_tax * 100
            ).to_integral_value()
        else:
            ctx['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return ctx

    def handle_payment(self, order_number, total, **kwargs):
        stripe_ref = Facade().charge(
            order_number,
            total,
            card=self.request.POST[STRIPE_TOKEN],
            description=self.payment_description(order_number, total, **kwargs),
            metadata=self.payment_metadata(order_number, total, **kwargs))

        source_type, __ = SourceType.objects.get_or_create(name=PAYMENT_METHOD_STRIPE)
        source = Source(
            source_type=source_type,
            currency=settings.STRIPE_CURRENCY,
            amount_allocated=total.incl_tax,
            amount_debited=total.incl_tax,
            reference=stripe_ref)
        self.add_payment_source(source)

        self.add_payment_event(PAYMENT_EVENT_PURCHASE, total.incl_tax)

    def payment_description(self, order_number, total, **kwargs):
        return self.request.POST[STRIPE_EMAIL]

    def payment_metadata(self, order_number, total, **kwargs):
        return {'order_number': order_number}


class IndexView(CoreIndexView):
    success_url = reverse_lazy('checkout:billing-address')


class BillingAddressView(CheckoutSessionMixin, generic.FormView):
    template_name = "checkout/billing_address.html"
    form_class = BillingAddressForm
    pre_conditions = ['check_basket_is_not_empty',
                      'check_basket_is_valid',
                      'check_user_email_is_captured']
    success_url = reverse_lazy('checkout:shipping-address')

    def get_initial(self):
        try:
            billing_address = UserAddress.objects.get(user=self.request.user, is_default_for_billing=True)
        except UserAddress.DoesNotExist:
            return super(BillingAddressView, self).get_initial()
        else:
            return {key: value for key, value in billing_address.__dict__.items()}

    def form_valid(self, form):
        # first the form is saved
        form.save()
        billing_address = {key: value for key, value in form.instance.__dict__.items() if not key.startswith('_')}
        # adding new billing address to session
        self.checkout_session.bill_to_new_address(billing_address)

        action = self.request.POST.get('action', None)
        is_default_for_billing = self.request.POST.get('default_for_billing', None)

        if is_default_for_billing:
            try:
                user_address = UserAddress(
                    user=self.request.user,
                    is_default_for_billing=True,
                    phone_number=form.instance.phone_number,
                    title=form.instance.title,
                    first_name=form.instance.first_name,
                    last_name=form.instance.last_name,
                    line1=form.instance.line1,
                    line2=form.instance.line2,
                    line3=form.instance.line3,
                    line4=form.instance.line4,
                    state=form.instance.state,
                    postcode=form.instance.postcode,
                    country=form.instance.country)
                user_address.save()
            except:
                pass

        if action == 'ship_to':
            # adding new shipping address to sesssion
            self.checkout_session.ship_to_new_address(billing_address)
            return redirect(reverse_lazy('checkout:shipping-method'))
        else:
            return redirect(self.success_url)


def save_contact_form(request):
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('comment'):
                post = Contact()
                post.name = request.POST.get('name')
                post.email = request.POST.get('email')
                post.phone = request.POST.get('phone')
                post.comment = request.POST.get('comment')
                post.save()
                return redirect('/contact-us/')
        else:
                return render(request, '/contact-us/')
