from django.db import models
from bioinformatica.models.experiment import Experiment


class DynamicAttributeDefinition(models.Model):

    attribute_description = models.TextField(max_length=120, blank=True)
    attribute_name = models.CharField(max_length=120)

    def __str__(self):
        return self.attribute_name


class DynamicAttributeInstance(models.Model):

    attribute_value = models.CharField(max_length=120)
    experiment_attributes = models.ForeignKey('Experiment', on_delete=models.CASCADE, blank=True, null=True)

    attribute_type = models.ForeignKey(
        DynamicAttributeDefinition,
        on_delete=models.CASCADE,
        default=None,
        null=True
    )

    def __str__(self):
        return str(self.attribute_type)


