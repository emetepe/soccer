from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    # Emblem
    emblem_pic = models.ImageField(upload_to='teams/emblems', blank=True, null=True)

    # Coach Detail
    coach_name = models.CharField(max_length=255, blank=True, null=True)
    coach_pic = models.ImageField(upload_to='teams/coaches', blank=True, null=True)

    # Shirt
    shirt_pic = models.ImageField(upload_to='teams/shirts', blank=True, null=True)

    # Stadium
    stadium = models.ForeignKey('Stadium', on_delete=models.CASCADE, related_name='stadium')

    # Description
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Stadium(models.Model):
    name = models.CharField(max_length=255)
    pic = models.ImageField(upload_to='teams/stadiums', blank=True, null=True)

    def __str__(self):
        return self.name
