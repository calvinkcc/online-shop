from oscar.apps.dashboard.views import IndexView
from yourappsfolder.checkout.models import Contact

from django.views.generic import TemplateView

class IndexView(IndexView):
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context

class ContactListView(TemplateView):
    template_name = 'dashboard/contacts/contact_list.html'

    def get_context_data(self,**kwargs):
        context = {
            'contact_details':Contact.objects.all()
        }
        return context