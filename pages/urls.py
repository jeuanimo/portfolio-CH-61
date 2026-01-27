# Import path for URL pattern matching
from django.urls import path
# Import views from pages app
from pages import views

# URL patterns for pages app
urlpatterns = [
        # Root URL - displays About Me page
        path('', views.about_me_view, name='about_me'),
        # Experience page URL
        path('experience/', views.experience_view, name='experience'),
        # Skills page URL with dynamic skill list
        path('skills/', views.skills_view, name='skills'),
        # User registration URL
        path('register/', views.register_view, name='register'),
        # User login URL
        path('login/', views.login_view, name='login'),
        # User logout URL
        path('logout/', views.logout_view, name='logout'),    ]