# Import Django shortcuts for rendering and redirecting
from django.shortcuts import render, redirect
# Import User model for account creation
from django.contrib.auth.models import User
# Import authenticate and login functions for user authentication
from django.contrib.auth import authenticate, login, logout
# Import messages for user feedback
from django.contrib import messages
# Import Skill model from projects app
from projects.models import Skill
# Import SkillForm for adding new skills
from projects.forms import SkillForm

# Create your views here.

# View for the About Me page
def  about_me_view(request):
    # Render the about me template
    return render(request, 'pages/about_me.html')

# View for the Experience page
def  experience_view(request):
    # Render the experience template
    return render(request, 'pages/experience.html')

# View for the Skills page with dynamic skill list and form handling
def  skills_view(request):
    # Check if form was submitted via POST
    if request.method == 'POST':
        # Create form instance with submitted data
        form = SkillForm(request.POST)
        # Validate form data
        if form.is_valid():
            # Save new skill to database
            form.save()
            # Redirect to skills page to prevent duplicate submissions
            return redirect('skills')
    else:
        # GET request - create empty form
        form = SkillForm()
    # Fetch all skills from database (ordered alphabetically)
    skills = Skill.objects.all()
    # Prepare context with skills and form
    context = {'skills': skills, 'form': form}
    # Render skills template with context
    return render(request, 'pages/skills.html', context)

# View for user registration/signup
def register_view(request):
    # Handle POST request for form submission
    if request.method == 'POST':
        # Get form data from request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        # Validate that passwords match
        if password != password_confirm:
            # Display error message
            messages.error(request, 'Passwords do not match.')
            # Re-render registration form
            return redirect('register')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            # Display error message
            messages.error(request, 'Username already exists.')
            # Re-render registration form
            return redirect('register')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            # Display error message
            messages.error(request, 'Email already exists.')
            # Re-render registration form
            return redirect('register')
        
        # Create new user account
        user = User.objects.create_user(username=username, email=email, password=password)
        # Display success message
        messages.success(request, 'Account created successfully! You can now log in.')
        # Redirect to login page
        return redirect('login')
    
    # GET request - render registration form
    return render(request, 'auth/register.html')

# View for user login
def login_view(request):
    # Handle POST request for form submission
    if request.method == 'POST':
        # Get form data from request
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user with provided credentials
        user = authenticate(request, username=username, password=password)
        
        # Check if authentication was successful
        if user is not None:
            # Log user in to session
            login(request, user)
            # Display welcome message
            messages.success(request, f'Welcome back, {username}!')
            # Redirect to next page or projects list
            next_url = request.GET.get('next', 'projects_list')
            return redirect(next_url)
        else:
            # Display error message for invalid credentials
            messages.error(request, 'Invalid username or password.')
    
    # GET request - render login form
    return render(request, 'auth/login.html')

# View for user logout
def logout_view(request):
    # Log user out of session
    logout(request)
    # Display goodbye message
    messages.success(request, 'You have been logged out successfully.')
    # Redirect to about me page
    return redirect('about_me')

# Custom 404 error handler - redirects to home page
def page_not_found(request, exception=None):
    # Display error message
    messages.error(request, 'Page not found. You have been redirected to the home page.')
    # Redirect to about me (home) page
    return redirect('about_me')