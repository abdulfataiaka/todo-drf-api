from django.urls import path
from ..views.sample import sample_view

urlpatterns = [
    path('sample', sample_view)
]
