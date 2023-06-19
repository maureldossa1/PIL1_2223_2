from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class filiaire(models.Model):
    nom = models.CharField(max_length=150,unique=True,verbose_name="nom")
    
    class Meta:
        verbose_name="filiaire"
        verbose_name_plural="filiaire"

    def __str__(self):
        return self.nom
    
class jour(models.Model):
    nom = models.CharField(max_length=25,unique=True,verbose_name="nom")
    
    class Meta:
        verbose_name="jour"
        verbose_name_plural="jours"

    def __str__(self):
        return self.nom
    

class cour(models.Model):
    nom = models.CharField(max_length=150,unique=True,verbose_name="nom")
    
    class Meta:
        verbose_name="cour"
        verbose_name_plural="cours"

    def __str__(self):
        return self.nom
    

class professeur(models.Model):
    nom = models.CharField(max_length=64,verbose_name="nom")
    prenom = models.CharField(max_length=64,verbose_name="prenom") 
    class Meta:
        verbose_name="professeur"
        verbose_name_plural="professeurs"

    def __str__(self):
        return self.nom
    

class cursus(models.Model):
    nom = models.CharField(max_length=100,unique=True)
    class Meta:
        verbose_name="Annee"
        verbose_name_plural ="Annee"
    def __str__(self):
        return self.nom


class emploi(models.Model):
    date = models.DateField(verbose_name="date")
    filiaire = models.ForeignKey(filiaire,on_delete=models.CASCADE,verbose_name="filiaire")
    Annee = models.ForeignKey(cursus,on_delete=models.CASCADE,verbose_name="classe")
    
    class Meta:
        verbose_name="emploi du temps"
        verbose_name_plural="emplois du temps"
    
    def __str__(self):
        return (f"du {self.date} filaire:{self.filiaire} Annee:{self.Annee}")
    
class salle(models.Model):
    nom = models.CharField(max_length=100,unique=True,verbose_name="salle")
    class Meta:
        verbose_name="salle"
        verbose_name_plural="salle"
    def __str__(self):
        return self.nom

class programme(models.Model):
    jour = models.ForeignKey(jour,on_delete=models.CASCADE,verbose_name="jour")
    cour = models.ForeignKey(cour,on_delete=models.CASCADE,verbose_name="cour")
    professeur = models.ForeignKey(professeur,on_delete=models.CASCADE,verbose_name="professeur")
    emploi = models.ForeignKey(emploi,on_delete=models.CASCADE,verbose_name="emploi")
    salle= models.ForeignKey(salle,on_delete=models.CASCADE,verbose_name="salle")
    hrd = models.IntegerField(validators=[MinValueValidator(7), MaxValueValidator(19)],verbose_name="heure de debut")
    hrf = models.IntegerField(validators=[MinValueValidator(7), MaxValueValidator(19)],verbose_name="heurde de fin")

    def __str__(self):
        return (f"{self.jour} {self.salle} ")
