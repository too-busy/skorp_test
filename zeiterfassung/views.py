from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Zeiteintrag
from .forms import ZeiteintragForm


@login_required
def zeiterfassung(request):
    if request.method == 'POST':
        form = ZeiteintragForm(request.POST)
        if form.is_valid():
            zeiteintrag = form.save(commit=False)
            zeiteintrag.mitarbeiter = request.user
            zeiteintrag.save()
            return redirect('zeiterfassung_list')
    else:
        form = ZeiteintragForm(initial={'mitarbeiter': request.user})

    return render(request, 'zeiterfassung.html', {'form': form})


def zeiterfassung_list(request):
    zeiteintraege = Zeiteintrag.objects.all()
    return render(request, 'zeiterfassung_list.html', {'zeiteintraege': zeiteintraege})
