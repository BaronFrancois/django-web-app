from django.db import models

class Band(models.Models):
    name = models.fields.charfield(max_length=100)
