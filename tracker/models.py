from django.db import models
from django.urls import reverse

class Food(models.Model):
	name = models.CharField(max_length=100, unique=True)
	kcal_per_100g = models.FloatField(help_text='kcal per 100g')

	def __str__(self):
		return f"{self.name} ({self.kcal_per_100g} kcal/100g)"

class Entry(models.Model):
	date = models.DateField()
	temperature = models.FloatField(null=True, blank=True)
	weight = models.FloatField(null=True, blank=True)
	systolic = models.IntegerField(null=True, blank=True)
	diastolic = models.IntegerField(null=True, blank=True)
	sleep_hours = models.FloatField(null=True, blank=True)
	calorie_intake = models.IntegerField(null=True, blank=True)
	calorie_burned = models.IntegerField(null=True, blank=True)
	steps = models.IntegerField(null=True, blank=True)

	def bmi(self, height_m=1.7):
		# default height 1.7m; later you can add user profile for height
		if self.weight:
			try:
				return round(self.weight / (height_m ** 2), 2)
			except Exception:
				return None
		return None

	def __str__(self):
		return f"Entry {self.date}"

class FoodEntry(models.Model):
	entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='foods')
	food = models.ForeignKey(Food, on_delete=models.PROTECT)
	grams = models.FloatField()

	@property
	def kcal(self):
		return round(self.food.kcal_per_100g * (self.grams / 100.0))