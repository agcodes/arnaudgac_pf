from django.db import models

class Experience(models.Model):
    LEVEL_CHOICES = [
        ('junior', 'Junior'),
        ('confirmed', 'Confirmé'),
        ('expert', 'Expert'),
        ('lead', 'Tech Lead'),
    ]
    
    company = models.CharField(max_length=200, verbose_name="Entreprise")
    position = models.CharField(max_length=200, verbose_name="Poste")
    start_date = models.CharField(max_length=50, verbose_name="Date de début")
    end_date = models.CharField(max_length=50, verbose_name="Date de fin")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name="Niveau")
    description = models.TextField(verbose_name="Description")
    skills = models.CharField(max_length=500, blank=True, verbose_name="Compétences")
    
    class Meta:
        verbose_name = "Expérience"
        verbose_name_plural = "Expériences"
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.company} - {self.position}"


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Compétence")
    category = models.CharField(max_length=100, blank=True, verbose_name="Catégorie")
    
    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"
        ordering = ['category', 'name']
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom")
    title = models.CharField(max_length=300, blank=True, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    years_experience = models.IntegerField(default=0, verbose_name="Années d'expérience")
    current_role = models.CharField(max_length=100, blank=True, verbose_name="Rôle actuel")
    projects_count = models.IntegerField(default=0, verbose_name="Nombre de projets")
    
    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"
    
    def __str__(self):
        return self.name
