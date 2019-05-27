from django.db import models

# Create your models here.
class Fighter(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField()
    first_appearance = models.CharField(max_length=30, default="SSB64")
    origin_game = models.CharField(max_length=30, default="Super Mario")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Tier(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=22)
    color = models.IntegerField()
    fighters = models.ManyToManyField(Fighter)

    class Meta:
        ordering = ['label']

    def get_fighters(self):
        return self.fighters

    def add_fighters(self, fs=[]):
        for f in fs:
            self.fighters.append(f)
        return self.fighters
