from django.db import models

class Ingredient(models.Model):
    STORAGE_CHOICES = [
        ('fridge', '冷蔵'),
        ('freezer', '冷凍'),
        ('room', '常温'),
    ]

    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expire_date = models.DateField()
    storage_type = models.CharField(max_length=10, choices=STORAGE_CHOICES)

    def __str__(self):
        return self.name


class RecipePlan(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class RecipeIngredient(models.Model):
    recipe_plan = models.ForeignKey(
        RecipePlan, on_delete=models.CASCADE, related_name='items'
    )
    name = models.CharField(max_length=100)
    required_quantity = models.IntegerField()
