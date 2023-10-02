from django.shortcuts import render
from .models import Profile
from portfolio.models import Skill, Category, Project

# Create your views here.
def home(request):
    profile = Profile.objects.all()[0]
    front = Skill.objects.filter(category__slug = 'frontend')
    back = Skill.objects.filter(category__slug = 'backend')
    projects = Project.objects.all()
    return render(request, "core/home.html", {'profile':profile, 'front':front, 'back':back, 'projects':projects} )

