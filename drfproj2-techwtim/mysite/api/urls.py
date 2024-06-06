from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/", views.BlogPostListCreate.as_view(), name="blogpost-view-create view"),
    path("blogpost/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update")
    
]
