import random
import string
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Arbeitsplan
from django.urls import reverse
from django.shortcuts import render

def einsatzplan_view(request):
    arbeitsplan_entries = Arbeitsplan.objects.all()
    arbeitsplan = []

    for entry in arbeitsplan_entries:
        entry_details_url = reverse('arbeitsplanung:arbeitsplan_entry_details', kwargs={'entry_id': entry.id})
        arbeitsplan.append({
            'title': f'{entry.mitarbeiter} - {entry.kunde}',
            'start': entry.start_datum.strftime('%Y-%m-%d'),
            'end': entry.end_datum.strftime('%Y-%m-%d'),
            'mitarbeiter': entry.mitarbeiter.name,
            'kunde': entry.kunde.name,
            'details_url': entry_details_url,
        })

    return render(request, 'einsatzplan.html', {'arbeitsplan': arbeitsplan})


def arbeitsplan_entry_details(request, entry_id):
    entry = get_object_or_404(Arbeitsplan, id=entry_id)
    return render(request, 'arbeitsplan_entry_details.html', {'entry': entry})


def get_random_color():
    # Generate a random color in hexadecimal format
    color = ''.join(random.choices(string.hexdigits[:-6], k=6))
    return '#' + color

def arbeitsplan_entries(request):
    entries = Arbeitsplan.objects.all()
    data = []

    for entry in entries:
        data.append({
            'title': f"{entry.mitarbeiter.name} - {entry.kunde.name}",
            'start': entry.start_datum.isoformat(),
            'end': entry.end_datum.isoformat(),
            'color': get_random_color(),  # Assign a random color
        })

    return JsonResponse(data, safe=False)
