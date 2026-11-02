# Vérification du projet Django CV

## ⚡ Installation rapide (sans environnement virtuel pour test)

```bash
cd django_cv

# Installer Django et les dépendances globalement (pour test rapide)
pip install django django-htmx whitenoise python-dotenv

# Configurer la clé secrète (optionnel pour le test)
export DJANGO_SECRET_KEY="test-secret-key"

# Vérifier la configuration
python manage.py check

# Appliquer les migrations
python manage.py migrate

# Charger les données
python manage.py loaddata cv/fixtures/initial_data.json

# Démarrer le serveur
python manage.py runserver
```

## 📋 Liste de vérification

- [x] Structure Django créée
- [x] Configuration Django (settings.py)
- [x] Modèles créés (Profile, Experience, Skill)
- [x] Admin Django configuré
- [x] Vues créées
- [x] Templates (base.html, home.html)
- [x] HTMX intégré
- [x] Tailwind CSS via CDN
- [x] Fichiers statiques (CSS, JS)
- [x] Fixtures de données initiales
- [x] Migrations créées
- [x] Routes configurées
- [x] Documentation (README.md, INSTALL.md)

## 🎯 Contenu du CV inclus

### Profil

### Expériences

### Compétences

## 🔍 Vérification manuelle

1. **Structure des fichiers** : Vérifiez que tous les fichiers sont présents
2. **Configuration Django** : Vérifiez settings.py
3. **Modèles** : Vérifiez models.py
4. **Templates** : Vérifiez les fichiers HTML
5. **Fichiers statiques** : Vérifiez CSS et JS

## 💡 Conseils pour le déploiement

### Local

```bash
cd django_cv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata cv/fixtures/initial_data.json
python manage.py runserver
```

### Production (avec Gunicorn)

```bash
pip install gunicorn
python manage.py collectstatic
DJANGO_SECRET_KEY=votre-cle gunicorn django_cv.wsgi:application --bind 0.0.0.0:8000
```

## 🚨 Résolution des problèmes

### Problème: Django non trouvé

```bash
# Activer l'environnement virtuel
source .venv/bin/activate
# Puis réessayer
```

### Problème: Module manquant

```bash
pip install nom-du-module
```

### Problème: Base de données non créée

```bash
python manage.py migrate
```

### Problème: Données non chargées

```bash
python manage.py loaddata cv/fixtures/initial_data.json
```

## ✅ Le projet est prêt !

Accédez à http://localhost:8000 pour voir votre CV.
