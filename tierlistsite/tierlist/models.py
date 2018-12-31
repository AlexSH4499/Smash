from django.db import models

# Create your models here.
class Fighter(models.Model):
    id = models.IntegerField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Tier(models.Model):
    id = models.IntegerField(max_length=1, primary_key=True)
    label = models.CharField(max_length=22)
    color = models.IntegerField(max_length=6)
    fighters = models.ManyToManyField(Fighter)

    class Meta:
        ordering = ['label']

    def get_fighters(self):
        return self.fighters

    def add_fighters(self, fs=[]):
        for f in fs:
            self.fighters.append(f)
        return self.fighters
