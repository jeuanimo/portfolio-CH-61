# Import Django's ORM models module for database modeling
from django.db import models

# Create your models here.

# Skill model - represents individual technical skills that can be tagged to projects
class Skill(models.Model):
    # Skill name field with max 100 characters
    name = models.CharField(max_length=100)

    # String representation returns the skill name for display
    def __str__(self):
        return self.name
    
    # Meta configuration for database ordering and behavior
    class Meta:
        # Order skills alphabetically by name
        ordering = ['name']

    
# Project model - represents portfolio projects with details and images
class Project(models.Model):
    # Project name field with max 50 characters
    name = models.CharField(max_length=50)
    # Detailed project description field (unlimited text)
    description = models.TextField()
    # Year project was completed (positive integers only)
    year = models.PositiveIntegerField()
    # Optional project image uploaded to 'projects/' directory
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    # Optional repository URL (e.g., GitHub link)
    repository = models.URLField(blank=True, null=True)
    # Many-to-many relationship with skills - projects can have multiple skills
    skills = models.ManyToManyField('Skill', related_name='projects')

    # String representation returns the project name and year for display
    def __str__(self):
        return f'{self.name} -- {self.year}' 

    # Meta configuration for database ordering
    class Meta:
        # Order projects by year descending (newest first)
        ordering = ['-year']
