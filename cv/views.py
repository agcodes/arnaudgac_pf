from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import json
import os


def load_cv_data():
    """Charge les données du CV depuis initial_data.json"""
    try:
        json_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'initial_data.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        profile = None
        experiences = []
        skills = []
        
        for item in data:
            model = item.get('model', '')
            fields = item.get('fields', {})
            
            if model == 'cv.profile':
                profile = fields
            elif model == 'cv.experience':
                experiences.append(fields)
            elif model == 'cv.skill':
                skills.append(fields)
        
        # Regrouper les compétences par catégorie
        skills_by_category = {}
        for skill in sorted(skills, key=lambda x: (x.get('category', ''), x.get('name', ''))):
            category = skill.get('category', 'Autres')
            if category not in skills_by_category:
                skills_by_category[category] = []
            skills_by_category[category].append(skill.get('name', ''))
        
        # Trier les expériences par date (descendant)
        experiences_sorted = sorted(experiences, key=lambda x: x.get('start_date', ''), reverse=True)
        
        return profile, experiences_sorted, skills_by_category
    except Exception as e:
        print(f"Erreur lors du chargement des données CV: {e}")
        return None, [], {}


class HomeView(TemplateView):
    template_name = 'cv/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        profile, experiences, skills_by_category = load_cv_data()
        
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


def health_check(request):
    """Endpoint de santé pour les checks Fly.io"""
    return HttpResponse("OK", status=200)


def handler404(request, exception):
    """Handler personnalisé pour les erreurs 404"""
    return render(request, '404.html', status=404)
