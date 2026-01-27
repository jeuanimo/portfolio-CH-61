# Import Django forms module for form creation
from django import forms
# Import Skill and Project models for form binding
from .models import Skill, Project


# ModelForm for creating and editing Skill instances
class SkillForm(forms.ModelForm):
    # Meta class defines form configuration
    class Meta:
        # Bind form to Skill model
        model = Skill
        # Include only the 'name' field in the form
        fields = ['name']
        # Custom widget configuration for form fields
        widgets = {
            # TextInput widget for name field with custom attributes
            'name': forms.TextInput(attrs={
                # CSS class for styling
                'class': 'form-input',
                # Placeholder text hint
                'placeholder': 'Enter a new skill',
                # Make field required
                'required': True,
            })
        }

# ModelForm for creating and editing Project instances
class ProjectForm(forms.ModelForm):
    # Meta class defines form configuration
    class Meta:
        # Bind form to Project model
        model = Project
        # Include all fields for project creation/editing
        fields = ['name', 'description', 'year', 'image', 'repository', 'skills']
        # Custom widget configuration for form fields
        widgets = {
            # Text input for project name
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Project name',
            }),
            # Textarea for project description
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Project description',
                'rows': 4,
            }),
            # Number input for year
            'year': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Year completed',
            }),
            # File input for project image
            'image': forms.FileInput(attrs={
                'class': 'form-input',
            }),
            # URL input for repository link
            'repository': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'https://github.com/...',
            }),
            # Multiple select for skills
            'skills': forms.CheckboxSelectMultiple(),        }