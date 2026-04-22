from django.db import models


class Category(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    source_code = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    rating = models.FloatField(null=True, blank=True)
    metacritic = models.IntegerField(null=True, blank=True)
    budget = models.BigIntegerField(null=True, blank=True)
    runtime = models.CharField(null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.name
