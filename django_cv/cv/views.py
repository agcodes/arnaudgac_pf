from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Profile, Experience, Skill
import json
import os

class HomeView(TemplateView):
    template_name = 'cv/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get profile
        profile = Profile.objects.first()
        
        # Get experiences
        experiences = Experience.objects.all().order_by('-start_date')
        
        # Get skills grouped by category
        skills_by_category = {}
        for skill in Skill.objects.all().order_by('category', 'name'):
            if skill.category not in skills_by_category:
                skills_by_category[skill.category] = []
            skills_by_category[skill.category].append(skill.name)
        
        context.update({
            'profile': profile,
            'experiences': experiences,
            'skills_by_category': skills_by_category,
        })
        return context

def home(request):
    return HomeView.as_view()(request)

def load_projects():
    """Charge les projets depuis le fichier JSON"""
    try:
        # Chemin vers le fichier JSON
        json_path = os.path.join(os.path.dirname(__file__), 'data', 'projects.json')
        
        with open(json_path, 'r', encoding='utf-8') as f:
            projects = json.load(f)
        
        # Ajouter le chemin STATIC_URL aux images
        from django.conf import settings
        for project in projects:
            # Si le chemin ne commence pas déjà par http ou /static, ajouter le préfixe
            if project.get('thumbnail'):
                if not project['thumbnail'].startswith(('http', '/static', '/')):
                    project['thumbnail'] = f"{settings.STATIC_URL}{project['thumbnail']}"
            if project.get('largeImage'):
                if not project['largeImage'].startswith(('http', '/static', '/')):
                    project['largeImage'] = f"{settings.STATIC_URL}{project['largeImage']}"
        
        return projects
    except Exception as e:
        print(f"Erreur lors du chargement des projets: {e}")
        return []

def portfolio(request):
    """Vue pour afficher le portfolio"""
    projects = load_projects()
    return render(request, 'cv/portfolio.html', {
        'projects': projects,
    })
