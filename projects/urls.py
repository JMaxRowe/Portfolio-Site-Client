from django.urls import path
from projects.views import ProjectListView
from .views import ProjectListView, ProjectDetailView, TagListView, RoleListView

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<slug:slug>/', ProjectDetailView.as_view()),
    path('tags/', TagListView.as_view()),
    path('roles/', RoleListView.as_view()),
]