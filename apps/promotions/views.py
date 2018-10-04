from django.shortcuts import get_object_or_404,render
from oscar.core.loading import get_model

ConditionalOffer = get_model('offer', 'ConditionalOffer')
Range = get_model('offer', 'Range')
Product = get_model('catalogue', 'Product')

from oscar.apps.promotions.views import HomeView as CoreHomeView

class HomeView(CoreHomeView):
    template_name = 'promotions/home.html'
    """
    This is the home page and will typically live at /
    """
    template_name = 'promotions/home.html'

    #context_object_name = 'products'

    # def dispatch(self, request, *args, **kwargs):
    #     self.range = get_object_or_404(
    #         Range, pk=1, is_public=True)
    #     return super().dispatch(
    #         request, *args, **kwargs)

    # def get_queryset(self):
    #     products = self.range.all_products()
    #     return products.order_by('rangeproduct__display_order')

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     ctx['range'] = self.range
    #     ctx['me'] = "hello"
    #     print('working?')
    #     return ctx

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['me'] = "hello"
    #     print('working?')
    #     return context


# def HomeView(request):
#     context = {}
#     return render(request, 'promotions/home2.html', context)
