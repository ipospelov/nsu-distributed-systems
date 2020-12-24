from django.db import models

from distributed_systems.apps.architecture_types.models import ArchitectureType


class Architecture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    architecture_type = models.ForeignKey(ArchitectureType,
                                          blank=True, null=True,
                                          on_delete=models.CASCADE)
