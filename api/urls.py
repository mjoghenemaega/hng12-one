from django.urls import path
from .views import NumberClassificationAPI

urlpatterns = [
    path('api/classify-number', NumberClassificationAPI.as_view(), name='classify_number'),
]
