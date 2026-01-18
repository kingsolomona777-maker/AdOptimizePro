from django.views.generic import ListView
from .models import Ad
class AdListView(ListView):
    model = Ad
    template_name = 'ad_optimizer/ad_list.html'
```
Then in `ad_optimizer/urls.py`:
```
from django.urls import path
from .views import AdListView
urlpatterns = [
    path('', AdListView.as_view(), name='ad_list'),
]
