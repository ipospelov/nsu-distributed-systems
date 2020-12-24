from django.db import models


class ArchitectureType(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    parent_type = models.ForeignKey('ArchitectureType',
                                    blank=True, null=True,
                                    on_delete=models.CASCADE)
