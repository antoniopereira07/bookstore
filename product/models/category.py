from django.db import models


class Category(models.Model):
    title: models.CharField = models.CharField(max_length=100)
    slug: models.SlugField = models.SlugField(unique=True)
    description: models.CharField = models.CharField(
        max_length=200, blank=True, null=True
    )
    active: models.BooleanField = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
