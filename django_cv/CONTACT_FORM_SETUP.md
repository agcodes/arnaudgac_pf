# Configuration du Formulaire de Contact

Ce document explique comment configurer l'envoi d'emails pour le formulaire de contact.

## Structure Implémentée

1. **Page de contact** : `templates/cv/contact.html`
    - Formulaire avec champs : Nom, Email, Message
    - Design cohérent avec le reste du site

2. **Vue** : `cv/views.py` - fonction `contact()`
    - Gère l'affichage et la soumission du formulaire
    - Envoie les données par email

3. **URL** : `django_cv/urls.py`
    - URL : `/contact/` avec nom `contact`

4. **Backend email** : `cv/email_backends.py`
    - Backend personnalisé pour l'API Infomaniak avec OAuth2
    - Gestion automatique des tokens d'accès

5. **Configuration email** : `django_cv/settings.py`
    - Paramètres de base configurés
    - En développement : utilise `console.EmailBackend` (affiche les emails dans la console)

---

## Configuration SMTP

Pour que les emails soient réellement envoyés, vous devez configurer un backend SMTP.

### Option 1: Gmail

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre-email@gmail.com'
EMAIL_HOST_PASSWORD = 'votre-app-password'
CONTACT_EMAIL = 'arnaudgac@ik.me'
```

> **Note**: Pour Gmail, activez l'authentification à 2 facteurs et créez un "App Password" sur https://myaccount.google.com/apppasswords

### Option 2: Mailgun

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'postmaster@votre-domaine.com'
EMAIL_HOST_PASSWORD = 'votre-mailgun-password'
CONTACT_EMAIL = 'arnaudgac@ik.me'
```

### Option 3: SendGrid

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'votre-sendgrid-api-key'
CONTACT_EMAIL = 'arnaudgac@ik.me'
```

### Option 4: Infomaniak SMTP

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.infomaniak.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'arnaudgac@ik.me'
EMAIL_HOST_PASSWORD = 'votre-mot-de-passe'
CONTACT_EMAIL = 'arnaudgac@ik.me'
```

---

## 🚀 Utiliser l'API Infomaniak avec OAuth2 (méthode recommandée)

Infomaniak propose une API REST pour envoyer des emails avec authentification OAuth2,
offrant une meilleure traçabilité et deliverabilité.

### Prérequis

1. **Créer une application OAuth2 chez Infomaniak** :
    - Connectez-vous à votre compte Infomaniak
    - Allez dans : **Compte → Développeurs → Applications**
    - Cliquez sur **"Créer une application"** ou sélectionnez votre application existante
    - Notez votre **Client ID** et **Client Secret**

2. **Trouvez votre Product ID** :
    - Allez dans **Mail → Gestion des emails**
    - Sélectionnez votre service Mail
    - L'ID du produit est visible dans l'URL ou les paramètres du service

### Configuration

#### Via settings.py

```python
# Utiliser le backend Infomaniak API avec OAuth2
EMAIL_BACKEND = 'cv.email_backends.InfomaniakEmailBackend'

# Identifiants OAuth2 Infomaniak
INFOMANIAK_CLIENT_ID = 'votre-client-id'
INFOMANIAK_CLIENT_SECRET = 'votre-client-secret'

# ID du produit Mail Infomaniak
INFOMANIAK_PRODUCT_ID = '123456'  # À remplacer par votre ID

# URL de l'API (optionnel, par défaut: https://api.infomaniak.com/2)
INFOMANIAK_API_URL = 'https://api.infomaniak.com/2'
INFOMANIAK_TOKEN_URL = 'https://api.infomaniak.com/1/oauth2/token'

# Email de destination
CONTACT_EMAIL = 'arnaudgac@ik.me'
```

#### Via fichier .env

```bash
EMAIL_BACKEND=cv.email_backends.InfomaniakEmailBackend
INFOMANIAK_CLIENT_ID=votre-client-id
INFOMANIAK_CLIENT_SECRET=votre-client-secret
INFOMANIAK_PRODUCT_ID=1440440
INFOMANIAK_API_URL=https://api.infomaniak.com/2
INFOMANIAK_TOKEN_URL=https://api.infomaniak.com/1/oauth2/token
CONTACT_EMAIL=arnaudgac@ik.me
```

### Fonctionnement du backend OAuth2

Le backend `InfomaniakEmailBackend` gère automatiquement :

1. **Obtention du token** : Utilise `client_credentials` grant pour obtenir un access_token
2. **Cache du token** : Le token est mis en cache et rafraîchi automatiquement avant expiration
3. **Authentification** : Utilise `Bearer <token>` dans les headers des requêtes
4. **Gestion des erreurs** : Re-essaye si le token a expiré

### Avantages de l'API Infomaniak

✅ Meilleure deliverabilité (moins de risques de spam)  
✅ Traçabilité complète des emails envoyés  
✅ Pas besoin de gérer l'authentification SMTP manuellement  
✅ Intégration native avec votre hébergement Infomaniak  
✅ Support des scopes spécifiques (mail, etc.)

---

## Variables d'environnement

Vous pouvez aussi configurer via le fichier `.env` :

```bash
# SMTP
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=mail.infomaniak.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=arnaudgac@ik.me
EMAIL_HOST_PASSWORD=votre-mot-de-passe
CONTACT_EMAIL=arnaudgac@ik.me

# ou API OAuth2
EMAIL_BACKEND=cv.email_backends.InfomaniakEmailBackend
INFOMANIAK_CLIENT_ID=votre-client-id
INFOMANIAK_CLIENT_SECRET=votre-client-secret
INFOMANIAK_PRODUCT_ID=1440440
CONTACT_EMAIL=arnaudgac@ik.me
```

---

## Test en développement

En mode `DEBUG=True`, les emails sont affichés dans la console :

```bash
python manage.py runserver
```

Lorsque vous soumettez le formulaire, vous verrez l'email dans votre terminal.

---

## Personnalisation

Vous pouvez modifier :

- Le sujet de l'email dans `cv/views.py` (variable `subject`)
- Le format du message dans la même vue (variable `email_body`)
- Le style du formulaire dans `templates/cv/contact.html`
- Les champs du formulaire dans `cv/views.py` (classe `ContactForm`)

---

## 📚 Documentation officielle

- [Infomaniak API Documentation](https://developer.infomaniak.com/docs/api)
- [Infomaniak OAuth2 Documentation](https://developer.infomaniak.com/docs/oauth2)
- Endpoint Mail API : `POST /mail/{product_id}/message`
- Endpoint OAuth2 Token : `POST /1/oauth2/token`

---

## ⚠️ Notes importantes

1. **Sécurité** : Ne commitez jamais vos `CLIENT_SECRET` ou mots de passe en clair dans le code
2. **Production** : Utilisez toujours des variables d'environnement en production
3. **Scope** : Assurez-vous que votre application OAuth2 a le scope `mail`
4. **Product ID** : Doit correspondre à votre service Mail Infomaniak
5. **Test** : Testez toujours en développement avec le console backend avant de passer en production

---

## Lien vers la page contact

Un bouton "Contactez-moi" a été ajouté dans le footer de la page d'accueil.
Vous pouvez aussi ajouter un lien dans le menu de navigation si vous en avez un.

URL de la page contact : `/contact/`
Nom de l'URL : `contact`

---

**Votre formulaire de contact est prêt à l'emploi !** 🎉
