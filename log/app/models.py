from django.contrib.auth.models import User
from django.db import models

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveIntegerField()
    kasb = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=30)
    matn = models.TextField()
    rasm = models.URLField()
    sana = models.DateTimeField(auto_now_add=True)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha


class Talks(models.Model):
    sarlavha = models.CharField(max_length=30)
    video = models.URLField()
    sana = models.DateTimeField(auto_now_add=True)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha