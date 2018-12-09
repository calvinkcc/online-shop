from oscar.apps.shipping import repository
from .methods import *


class Repository(repository.Repository):

    def get_available_shipping_methods(
            self, basket, user=None, shipping_addr=None,
            request=None, **kwargs):
        methods = (USPSFC(),USPSP(), USPSE(),UPSG(),FEDEXG(),FEDEX2D(),FEDEXO(),NoShippingRequired())
        print("\n\nFetch availble shipping methods")
        if shipping_addr:
            # Express is only available in the UK
            methods = (USPSFC(),USPSP(), USPSE(),UPSG(),FEDEXG(),FEDEX2D(),FEDEXO(),NoShippingRequired())

        return methods
