from django.urls import path
from projects.views import ProjectListView
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<slug:slug>/', ProjectDetailView.as_view()),
]