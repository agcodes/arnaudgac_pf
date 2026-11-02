# Django CV

Projet Django avec HTMX pour afficher le CV

## 🚀 Démarrage rapide

### 1. Installation

```bash
# Se placer dans le dossier du projet
cd django_cv

# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement (Linux/Mac)
source .venv/bin/activate
# Sur Windows: .\.venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer l'environnement
cp .env.example .env
# Éditer .env et configurer DJANGO_SECRET_KEY

# Appliquer les migrations
python manage.py migrate

# Charger les données initiales
python manage.py loaddata cv/fixtures/initial_data.json

# Démarrer le serveur
python manage.py runserver
```

### 2. Accéder à l'application

Ouvrez votre navigateur à : [http://localhost:8000](http://localhost:8000)

## 📁 Structure du projet

```
django_cv/
├── django_cv/
│   ├── settings.py      # Configuration Django
│   ├── urls.py          # Routage URL
│   └── ...
├── cv/
│   ├── models.py        # Modèles (Profile, Experience, Skill)
│   ├── views.py         # Vues
│   ├── admin.py         # Admin Django
│   └── fixtures/        # Données initiales
├── templates/
│   ├── base.html        # Template de base
│   └── cv/
│       └── home.html    # Page d'accueil
├── static/
│   ├── css/
│   │   └── style.css    # Styles personnalisés
│   └── js/
│       └── main.js      # JavaScript principal
├── manage.py            # Gestion Django
├── requirements.txt     # Dépendances Python
└── README.md
```

## ✨ Fonctionnalités

- **Django** : Backend robuste en Python
- **HTMX** : Interactions dynamiques sans JavaScript complexe
- **Tailwind CSS** : Design moderne et responsive
- **WhiteNoise** : Gestion des fichiers statiques
- **Admin Django** : Interface d'administration pour gérer le CV

## 🎨 Personnalisation

### Modifier le contenu du CV

1. **Via l'interface admin** (recommandé) :

    ```bash
    python manage.py createsuperuser
    python manage.py runserver
    # Accéder à http://localhost:8000/admin
    ```

2. **Modifier les fixtures** :
    - Éditer `cv/fixtures/initial_data.json`

### Modifier le design

- Éditer `templates/cv/home.html` pour modifier la structure
- Éditer `static/css/style.css` pour les styles personnalisés
- Utiliser Tailwind CSS pour un design rapide

## 📊 Modèles de données

### Profile

- Nom, titre, description
- Années d'expérience, rôle actuel, nombre de projets

### Experience

- Entreprise, poste, dates
- Niveau (Junior, Confirmé, Expert, Tech Lead)
- Description et compétences

### Skill

- Nom de la compétence
- Catégorie (Backend, Frontend, Database, DevOps, Enterprise)

## 🔧 Configuration avancée

### Pour la production

```bash
# Installer Gunicorn
pip install gunicorn

# Collecter les fichiers statiques
python manage.py collectstatic

# Démarrer avec Gunicorn
gunicorn django_cv.wsgi:application --bind 0.0.0.0:8000
```

### Variables d'environnement

| Variable               | Description        | Default   |
| ---------------------- | ------------------ | --------- |
| `DJANGO_SECRET_KEY`    | Clé secrète Django | requis    |
| `DJANGO_DEBUG`         | Mode debug         | True      |
| `DJANGO_ALLOWED_HOSTS` | Hosts autorisés    | localhost |

## 🎯 Technologies utilisées

- **Backend**: Django, Python
- **Frontend**: HTMX, Tailwind CSS, Vanilla JavaScript
- **Déploiement**: WhiteNoise, Gunicorn

## 📝 Notes

Ce projet est conçu pour être simple à déployer et à maintenir. L'utilisation de HTMX permet d'ajouter des interactions dynamiques sans la complexité d'un framework JavaScript complet.

Pour ajouter des fonctionnalités supplémentaires :

- Créer de nouvelles vues Django
- Utiliser les attributs HTMX pour des interactions AJAX
- Personnaliser les templates avec Tailwind CSS

## 🔗 Liens utiles

- [Django Documentation](https://docs.djangoproject.com/)
- [HTMX Documentation](https://htmx.org/)
- [Tailwind CSS](https://tailwindcss.com/)
