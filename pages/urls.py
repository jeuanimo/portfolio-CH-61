from django.urls import path
from pages import views

urlpatterns = [
        path('', views.about_me_view, name='about_me'),
        path('experience/', views.experience_view, name='experience'),
        path('skills/', views.skills_view, name='skills'),
    ]
