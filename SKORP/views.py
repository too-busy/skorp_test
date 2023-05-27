from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def einsatzplan_view(request):
    arbeitsplan = [
        {
            'title': 'Ereignis 1',
            'start': '2023-05-27',
            'end': '2023-05-28'
        },
        {
            'title': 'Ereignis 2',
            'start': '2023-05-30',
            'end': '2023-05-31'
        },
        # Weitere Einträge hier
    ]
    return render(request, 'einsatzplan.html', {'arbeitsplan': arbeitsplan})
