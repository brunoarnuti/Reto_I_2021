from django.db import models

from bioinformatica.models import experiment


class DynamicAttribute(models.Model):

    TYPE1 = 'T1'
    TYPE2 = 'T2'
    TYPE3 = 'T3'

    ATTRIBUTE_TYPES_CHOICES = [
        ('TYPE1', 'Type 1'),
        ('TYPE2', 'Type 2'),
        ('TYPE3', 'Type 3'),
    ]
    attribute_id = models.CharField(max_length=120)
    attribute_type = models.CharField(max_length=5, choices=ATTRIBUTE_TYPES_CHOICES, default=TYPE1)
    attribute_value = models.CharField(max_length=200)
    experiment_attributes = models.ForeignKey('experiment', on_delete=models.CASCADE, blank=True, null=True)

