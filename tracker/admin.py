from django.contrib import admin
from .models import Entry, Food, FoodEntry

class FoodEntryInline(admin.TabularInline):
	model = FoodEntry
	extra = 0

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
	list_display = ('date', 'weight', 'calorie_in')