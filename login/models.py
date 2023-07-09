from django.db import models


class User_Data(models.Model):
    first = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    password= models.CharField(max_length=120)
    date = models.DateField()
    def __str__(self):
        return f"{self.first}{self.last_name}"


class Scores(models.Model):
    first=models.CharField(max_length=80)
    email=models.EmailField()
    currentlevel=models.CharField(max_length=80)
    score=models.IntegerField()
    time=models.CharField(max_length=80)
    def __str__(self):
        return f"{self.first}{self.email}"