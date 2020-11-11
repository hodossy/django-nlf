from django.contrib.auth.models import User
from django.db import models


class Publication(models.Model):
    DIGITAL = 0
    PRINTED = 1
    CATEGORIES = ((DIGITAL, "Digital"), (PRINTED, "Printed"))

    title = models.CharField(max_length=30)
    category = models.SmallIntegerField(choices=CATEGORIES, default=DIGITAL)
    subscription_fee = models.DecimalField(max_digits=5, decimal_places=2)
    market_share = models.FloatField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    views = models.IntegerField(default=0)
    archived = models.BooleanField(default=False)
    publications = models.ManyToManyField(Publication, related_name="articles")

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline
