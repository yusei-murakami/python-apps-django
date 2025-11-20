from django.contrib import admin
from .models import Profile, Entry, Food

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("height_cm",)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("date", "temperature", "weight", "calorie_in", "steps")
    list_filter = ("date",)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "kcal_per_100g")

# @admin.register(FoodEntry)
# class FoodEntryAdmin(admin.ModelAdmin):
#     list_display = ("entry", "food", "grams", "kcal")
