from django.urls import path
from .views import ItemCreateView,MylistItemsView

urlpatterns = [
    path('create/', ItemCreateView.as_view(), name='item-create'),
    path('my-items/', MylistItemsView.as_view(), name='my-items'),
]
