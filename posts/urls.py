from django.urls import path
from . import views

urlpatterns = [
    path("tags/", views.tag_list, name="tag_list"),
]
