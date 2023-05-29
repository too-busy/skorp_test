from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Zeiteintrag
from .forms import ZeiteintragForm
from arbeitsplanung.models import Mitarbeiter

@login_required
def zeiterfassung(request):
    if request.method == 'POST':
        form = ZeiteintragForm(request.POST)
        if form.is_valid():
            zeiteintrag = form.save(commit=False)

            # Get the Mitarbeiter object for the logged-in user
            mitarbeiter = request.user.mitarbeiter

            zeiteintrag.mitarbeiter = mitarbeiter
            zeiteintrag.save()
            messages.success(request, 'Zeiteintrag erfolgreich erstellt!')
            return redirect('/zeiterfassung/list')
        else:
            messages.error(request, 'Fehler beim Erstellen des Zeiteintrags.')
            print(form.errors)
    else:
        # Get the logged-in user's Mitarbeiter object
        mitarbeiter = request.user.mitarbeiter

        # Populate the dropdown menu with only the logged-in user's Mitarbeiter object
        form = ZeiteintragForm(initial={'mitarbeiter': mitarbeiter})
        form.fields['mitarbeiter'].disabled = True

    return render(request, 'zeiterfassung.html', {'form': form})

def zeiterfassung_list(request):
    zeiteintraege = Zeiteintrag.objects.all()
    return render(request, 'zeiterfassung_list.html', {'zeiteintraege': zeiteintraege})
