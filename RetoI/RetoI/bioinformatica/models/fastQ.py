from django.db import models


# Create your models here.

class FastQ(models.Model):
    sample = models.ForeignKey('Sample', on_delete=models.DO_NOTHING)
    name = models.CharField()

    def __str__(self):
        return self.name
