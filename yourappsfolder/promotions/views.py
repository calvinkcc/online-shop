from django.shortcuts import get_object_or_404
from oscar.core.loading import get_model
from django.forms.models import model_to_dict
import json
from django.core import serializers

ConditionalOffer = get_model('offer', 'ConditionalOffer')
Range = get_model('offer', 'Range')
Product = get_model('catalogue', 'Product')

from oscar.apps.promotions.views import HomeView as CoreHomeView

class HomeView(CoreHomeView):
    """
    This is the home page and will typically live at /
    """
    template_name = 'promotions/home.html'
    context_object_name = 'products'

    def dispatch(self, request, *args, **kwargs):
        self.range = get_object_or_404(
            Range, pk=1, is_public=True)
        return super().dispatch(
            request, *args, **kwargs)

    def get_queryset(self):
        products = self.range.all_products()
        return products.order_by('rangeproduct__display_order')

# managed to start getting data out of this, but I'm going to have to write whole classes to get a lot of this functionality working
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['range'] = self.range
        ctx['me'] = "hello"
        bob = get_object_or_404(Range, pk=1, is_public=True)
        ctx['bob'] = model_to_dict(bob)
        # print(json.dumps(model_to_dict(bob)))
        print(model_to_dict(bob))

        return ctx

# def HomeView(request):
#     context = {}
#     return render(request, 'promotions/home2.html', context)

