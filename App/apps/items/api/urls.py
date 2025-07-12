from django.urls import path
from .views import ItemCreateView

urlpatterns = [
    path('create/', ItemCreateView.as_view(), name='item-create'),
]
