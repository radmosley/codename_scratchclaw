from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Species(models.Model):
    species_name = models.CharField(max_length=300)

    def __str__(self):
        return self.species_name

class AbilityType(models.Model):
    ability_type_name = models.CharField(max_length=300)

    def __str__(self):
        return self.ability_type_name

class Ability(models.Model):
    ability_name = models.CharField(max_length=300)
    ability_type = models.ForeignKey(AbilityType, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ability_name
    

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_species = models.ForeignKey(Species, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=300)
    level = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)
    hit_points = models.IntegerField(null=True, blank=True)
    # abilities = models.ForeignKey(Ability, on_delete=models.CASCADE)
    # clothing = models.ForiegnKey(Species)
    # equipment = models.ForiegnKey(Species)
    
    def __str__(self):
        return self.pet_name

