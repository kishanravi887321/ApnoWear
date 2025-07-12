from django.urls import path
from .views import MyPurchasesView

urlpatterns = [
    path('my-purchases/', MyPurchasesView.as_view(), name='my-purchases'),
]
  