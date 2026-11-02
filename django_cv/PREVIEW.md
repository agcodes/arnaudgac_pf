# Aperçu du CV - Arnaud Gac

## 🎨 Design et Mise en page

### En-tête (Hero Section)
```
┌─────────────────────────────────────────────────────────┐
│  [Gradient: Bleu à Violet]                             │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Arnaud Gac                                        │  │
│  │  Des défis, du code, des résultats.               │  │
│  │                                                       │  │
│  │  15 ans de projets, une même exigence : des       │  │
│  │  solutions qui produisent de la valeur...         │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Carte de Profil
```
┌─────────────────────────────────────────────────────────┐
│  [Background Blanc avec ombre]                           │
│  ┌──────┬──────────┬──────────┬──────────────────────┐ │
│  │ 15   │ Expert    │ 50+      │ Stack:                │ │
│  │ ans  │          │ projets  │ [C#][.NET][JS]...    │ │
│  │ exp. │          │          │                      │ │
│  └──────┴──────────┴──────────┴──────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

### Expériences Professionnelles

#### Carte ZF Group
```
┌─────────────────────────────────────────────────────────┐
│  [Border gauche: Bleu]                                  │
│  ZF Group · Ingénieur développeur full-stack           │
│  2021 - 2026                                             │
│  ┌───────────────────────────────────────────────────┐  │
│  │ Niveau : Tech Lead                                │  │
│  │ Conception et évolution d'architectures SI...     │  │
│  │ Leadership, Environnement international           │  │
│  └───────────────────────────────────────────────────┘  │
│  [En savoir plus →]                                    │
└─────────────────────────────────────────────────────────┘
```

#### Carte Versa
```
┌─────────────────────────────────────────────────────────┐
│  [Border gauche: Bleu]                                  │
│  Versa · Développeur full-stack, chargé de projet        │
│  2016 - 2021                                             │
│  ┌───────────────────────────────────────────────────┐  │
│  │ Niveau : Confirmé                                  │  │
│  │ Développement et intégration de solutions...       │  │
│  │ Innovation, Multi-clients                          │  │
│  └───────────────────────────────────────────────────┘  │
│  [En savoir plus →]                                    │
└─────────────────────────────────────────────────────────┘
```

#### Carte Jean Caby
```
┌─────────────────────────────────────────────────────────┐
│  [Border gauche: Bleu]                                  │
│  Jean Caby · Développeur d'applications                 │
│  2011 - 2016                                             │
│  ┌───────────────────────────────────────────────────┐  │
│  │ Niveau : Junior                                     │  │
│  │ Développement d'applications pour le suivi...     │  │
│  │ Proche des utilisateurs                            │  │
│  └───────────────────────────────────────────────────┘  │
│  [En savoir plus →]                                    │
└─────────────────────────────────────────────────────────┘
```

### Pied de page
```
┌─────────────────────────────────────────────────────────┐
│  [Background Gris Foncé]                                │
│  © 2024 - Arnaud Gac | Développeur Full-Stack           │
│  Des défis, du code, des résultats.                     │
└─────────────────────────────────────────────────────────┘
```

## 🎯 Fonctionnalités Interactives

### HTMX Features
1. **Hover Effects** : Les cartes d'expérience ont un effet de survol
2. **Transitions fluides** : Animations CSS pour une expérience utilisateur améliorée
3. **Boutons En savoir plus** : Interactions dynamiques (prêt pour l'expansion)

### Design Responsive
- Adapté aux mobiles, tablettes et desktop
- Grid layout qui s'adapte à la taille de l'écran
- Polices qui s'ajustent automatiquement

### Palette de couleurs
- Bleu principal: #4f46e5
- Violet: #7c3aed
- Gris: #f3f4f6, #4b5563
- Blanc: #ffffff
- Gris foncé: #1f2937

## 📱 Aperçu Mobile

```
[Header vertical]

[Profile Card]
┌─────────────┐
│ 15          │
│ ans exp.    │
├─────────────┤
│ Expert      │
│ rôle actuel  │
├─────────────┤
│ 50+         │
│ projets     │
└─────────────┘

[Expériences en colonne unique]
┌─────────────┐
│ ZF Group    │
│ 2021-2026   │
│ Tech Lead   │
└─────────────┘

┌─────────────┐
│ Versa       │
│ 2016-2021   │
│ Confirmé    │
└─────────────┘
```

## 🎨 Technologies Utilisées

- **Backend**: Django, Python
- **Frontend**: HTMX, Tailwind CSS, JavaScript
- **Design**: Gradient backgrounds, card-based layout, smooth transitions
- **Responsive**: Mobile-first approach

## 🔗 Comment tester

1. Installez les dépendances
2. Démarrez le serveur: `python manage.py runserver`
3. Ouvrez http://localhost:8000
4. Naviguez sur la page pour voir le design
5. Survolez les cartes d'expérience pour voir les effets

## ✨ Points forts du design

- **Moderne**: Design épuré et professionnel
- **Lisible**: Hiérarchie claire de l'information
- **Interactif**: Effets visuels engageants
- **Responsive**: S'adapte à tous les appareils
- **Personnalisable**: Facile à modifier

## 📝 Notes de personnalisation

Pour modifier le design:
1. Éditez `static/css/style.css` pour les couleurs et polices
2. Modifiez `templates/cv/home.html` pour la structure
3. Utilisez les classes Tailwind pour des ajustements rapides

Pour ajouter plus de contenu:
1. Ajoutez des entrées dans les fixtures
2. Ou utilisez l'interface admin Django
