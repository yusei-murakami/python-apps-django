from django.shortcuts import render, redirect
from .forms import EntryForm  # Ensure you import the form class
from .models import Food, FoodEntry, Entry  # Import the Food, FoodEntry, and Entry models
from datetime import date  # Import date for calendar_redirect
import calendar  # Import calendar for calendar_view
from django.shortcuts import render

def index(request):
    return render(request, 'tracker/index.html')


def add_entry(request):
	form = EntryForm(request.POST or None)  # Define the form
	foods_text = request.POST.get('foods_text', '')
	if form.is_valid():
		entry = form.save(commit=False)
		# parse foods_text: lines like "Rice,200"
		total_kcal = 0
		entry.calorie_intake = 0
		entry.save()
		if foods_text.strip():
			lines = foods_text.strip().split('\n')
			for line in lines:
				parts = [p.strip() for p in line.split(',') if p.strip()]
				if len(parts) >= 2:
					name = parts[0]
					try:
						grams = float(parts[1])
					except ValueError:
						grams = 0
					food_obj, created = Food.objects.get_or_create(name__iexact=name, defaults={'name': name, 'kcal_per_100g': 0})
					# get exact match if possible
					try:
						food_obj = Food.objects.get(name__iexact=name)
					except Food.DoesNotExist:
						food_obj = Food.objects.create(name=name, kcal_per_100g=0)
					fe = FoodEntry.objects.create(entry=entry, food=food_obj, grams=grams)
					total_kcal += fe.kcal
			entry.calorie_intake = int(total_kcal)
			entry.save()
		return redirect('tracker:entry_list')
	else:
		return render(request, 'tracker/add.html', {'form': form})
	return render(request, 'tracker/add.html', {'form': form})


def entry_list(request):
	qs = Entry.objects.order_by('-date')
	# compute totals for chart page convenience
	return render(request, 'tracker/list.html', {'entries': qs})


def chart_view(request):
	qs = Entry.objects.order_by('date')
	dates = [e.date.strftime('%Y-%m-%d') for e in qs]
	weights = [e.weight or None for e in qs]
	sleep = [e.sleep_hours or None for e in qs]
	intake = [e.calorie_intake or 0 for e in qs]
	burned = [e.calorie_burned or 0 for e in qs]
	return render(request, 'tracker/chart.html', {
		'labels': dates,
		'weights': weights,
		'sleep': sleep,
		'intake': intake,
		'burned': burned,
	})


def calendar_redirect(request):
	today = date.today()
	return redirect('tracker:calendar', year=today.year, month=today.month)


def calendar_view(request, year, month):
	year = int(year)
	month = int(month)
	cal = calendar.Calendar()
	month_days = cal.itermonthdates(year, month)
	# build a list of weeks, each week is list of days
	weeks = []
	week = []
	entries_by_date = {e.date: e for e in Entry.objects.filter(date__year=year, date__month=month)}
	for d in month_days:
		day_entry = entries_by_date.get(d)
		week.append({'date': d, 'entry': day_entry})
		if len(week) == 7:
			weeks.append(week)
			week = []
	return render(request, 'tracker/calendar.html', {'weeks': weeks, 'year': year, 'month': month})