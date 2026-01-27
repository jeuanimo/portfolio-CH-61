# Import Django shortcut for rendering templates and HTTP responses
from django.shortcuts import render, redirect, get_object_or_404
# Import login_required decorator to protect views
from django.contrib.auth.decorators import login_required
# Import Project model for database queries
from .models import Project
# Import forms for handling project creation/editing
from .forms import ProjectForm

# Create your views here.

# View for the basic projects page (legacy)
def projects_view(request):
    # Render the basic projects template
    return render(request, 'projects/projects.html')

# View for displaying all projects in a list format
def projects_list(request):
    # Fetch all projects from database (ordered by year descending)
    projects = Project.objects.all().order_by('-year')
    # Pass user authentication status for conditional UI rendering
    context = {'projects': projects, 'is_authenticated': request.user.is_authenticated}
    return render(request, 'projects/projects_list.html', context)

# View for creating a new project - requires login
@login_required(login_url='login')
def add_project(request):
    # Handle POST request for form submission
    if request.method == 'POST':
        # Create form instance with POST data
        form = ProjectForm(request.POST, request.FILES)
        # Validate form data
        if form.is_valid():
            # Save form to database
            form.save()
            # Redirect to projects list after creation
            return redirect('projects_list')
    else:
        # Create empty form for GET request
        form = ProjectForm()
    # Render form template with context
    context = {'form': form, 'title': 'Add New Project'}
    return render(request, 'projects/project_form.html', context)

# View for editing an existing project - requires login
@login_required(login_url='login')
def edit_project(request, project_id):
    # Get project by ID or return 404
    project = get_object_or_404(Project, id=project_id)
    # Handle POST request for form submission
    if request.method == 'POST':
        # Create form instance with POST data and current project instance
        form = ProjectForm(request.POST, request.FILES, instance=project)
        # Validate form data
        if form.is_valid():
            # Save updated form to database
            form.save()
            # Redirect to projects list after update
            return redirect('projects_list')
    else:
        # Create form pre-populated with project data for GET request
        form = ProjectForm(instance=project)
    # Render form template with context
    context = {'form': form, 'title': 'Edit Project', 'project': project}
    return render(request, 'projects/project_form.html', context)

# View for deleting a project - requires login
@login_required(login_url='login')
def delete_project(request, project_id):
    # Get project by ID or return 404
    project = get_object_or_404(Project, id=project_id)
    # Delete project from database
    project.delete()
    # Redirect to projects list after deletion
    return redirect('projects_list')