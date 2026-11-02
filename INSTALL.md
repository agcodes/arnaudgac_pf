# Django CV - Installation Guide

## Prérequis
- Python 3.10+
- pip (gestionnaire de packages Python)
- (Optionnel) Virtualenv ou venv

## Installation

### 1. Créer un environnement virtuel
```bash
cd django_cv
python -m venv .venv
source .venv/bin/activate  # Sur Linux/Mac
# .\.venv\Scripts\activate  # Sur Windows
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configurer l'environnement
Copiez le fichier .env.example en .env :
```bash
cp .env.example .env
```

Éditez le fichier .env et configurez vos variables :
```
DJANGO_SECRET_KEY=votre-cle-secrete
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Charger les données initiales
```bash
python manage.py loaddata cv/fixtures/initial_data.json
```

### 6. Créer un superutilisateur (optionnel pour l'admin)
```bash
python manage.py createsuperuser
```

### 7. Démarrer le serveur de développement
```bash
python manage.py runserver
```

### 8. Accéder à l'application
Ouvrez votre navigateur et allez sur :
```
http://localhost:8000
```

## Pour la production

### Installer les dépendances de production
```bash
pip install -r requirements.txt gunicorn whitenoise
```

### Configurer .env pour la production
```
DJANGO_SECRET_KEY=votre-cle-secrete-prod
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=votre-domaine.com
```

### Collecter les fichiers statiques
```bash
python manage.py collectstatic
```

### Démarrer avec Gunicorn
```bash
gunicorn django_cv.wsgi:application --bind 0.0.0.0:8000
```

## Fonctionnalités HTMX

Ce projet utilise HTMX pour :
- Les interactions dynamiques sans rechargement de page
- Les animations fluides
- Le chargement progressif du contenu

Les cartes d'expérience sont interactives et peuvent être étendues avec des détails supplémentaires.
