
from django.urls import path
#from rest_framework.routers import DefaultRouter
from app.views import TestView

# Create a router and register our viewsets with it.
# router = DefaultRouter()

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('v1/test/', TestView.as_view(), name='test'),
]