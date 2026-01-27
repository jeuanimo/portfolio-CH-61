"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import Django admin site for administrative interface
from django.contrib import admin
# Import path and include for URL routing
from django.urls import path, include
# Import settings and static for serving media files during development
from django.conf import settings
from django.conf.urls.static import static
# Import custom error handler from pages app
from pages.views import page_not_found


# Main URL configuration for the entire project
urlpatterns = [
    # Admin interface route - accessible at /admin/
    path('admin/', admin.site.urls),
    # Include all pages app URLs at root level
    path('', include('pages.urls')),
    # Include all projects app URLs under /projects/ prefix
    path('projects/', include('projects.urls')),

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handler for 404 page not found errors
handler404 = page_not_found
