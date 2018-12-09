from oscar.apps.checkout.app import CheckoutApplication as CoreCheckoutApplication
from django.conf.urls import url
from oscar.core.loading import get_class
from django.contrib.auth.decorators import login_required


class CheckoutApplication(CoreCheckoutApplication):
    billing_address = get_class("checkout.views", "BillingAddressView")

    def get_urls(self):
        new_urls = [
            url(r'^billing-address/$', login_required(self.billing_address.as_view(), login_url='/accounts/login/'), name="billing-address"),
        ]
        old_urls = super(CheckoutApplication, self).get_urls()
        return self.post_process_urls(new_urls + old_urls)


application = CheckoutApplication()
