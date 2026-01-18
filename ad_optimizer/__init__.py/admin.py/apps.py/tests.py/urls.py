from django.urls import path
from .views import ad_list  # Change this line
urlpatterns = [
    path('', ad_list, name='ad_list'),  # Change this line
]
