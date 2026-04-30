from django.urls import path
from .views import AccountView

urlpatterns = [
    path('me/', AccountView.as_view()),
]