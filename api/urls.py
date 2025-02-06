from django.urls import path, re_path
from .views import NumberClassifierView


urlpatterns = [
    path("classify-number/", NumberClassifierView.as_view(), name="classify_numbers")
]