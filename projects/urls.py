# Import path for URL pattern matching
from django.urls import path
# Import views from projects app
from projects import views

# URL patterns for projects app (prefixed with /projects/ from main urls.py)
urlpatterns = [
    # Main projects list at /projects/
    path('', views.projects_list, name='projects_list'),
    # Legacy route alias for backward compatibility at /projects/list/
    path('list/', views.projects_list, name='projects_list_legacy'),
    # Add new project at /projects/add/
    path('add/', views.add_project, name='add_project'),
    # Edit project at /projects/<id>/edit/
    path('<int:project_id>/edit/', views.edit_project, name='edit_project'),
    # Delete project at /projects/<id>/delete/
    path('<int:project_id>/delete/', views.delete_project, name='delete_project'),]