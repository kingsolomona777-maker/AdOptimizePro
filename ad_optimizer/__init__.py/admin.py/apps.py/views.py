from django.views.generic import ListView
from .models import Ad
class AdListView(ListView):
    model = Ad
    template_name = 'ad_optimizer/ad_list.html
