from django.urls import path

from .views import *

urlpatterns = [
    path('file/<str:username>/<str:repo>/<str:branch_or_tag>/<str:file_name>', FileView.as_view()),
]
