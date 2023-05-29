from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from kundendatenbank.models import Kunden
from .models import NfcTag, NfcScan
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import NfcTag
from .forms import NfcScanForm




def view_all_tag(request):
    kunden = Kunden.objects.all()  # Alle Kunden abrufen
    context = {'kunden': kunden}
    return render(request, 'nfctags.html', context)



def register_scan(request, tag_id):
    # Get the NfcTag object with the given ID.
    tag = get_object_or_404(NfcTag, id=tag_id)

    # Create an NfcScan entry with the current timestamp.
    NfcScan.objects.create(user=request.user, tag=tag)

    return HttpResponse('Scan erfolgreich registriert.')


def view_tag(request, tag_id):
    tag = get_object_or_404(NfcTag, id=tag_id)
    scan = NfcScan.objects.filter(tag=tag).order_by('-timestamp').first()
    success_message = ""
    error_message = ""

    if request.method == 'POST':
        form = NfcScanForm(request.POST, request.FILES, instance=scan)
        if form.is_valid():
            scan = form.save(commit=False)  # Objekt vorübergehend speichern
            scan.user = request.user  # Benutzer zuweisen
            scan.save()  # Eintrag speichern
            form.save_m2m()  # M2M-Beziehungen speichern
            success_message = "Scan erfolgreich aktualisiert."
        else:
            error_message = "Fehler beim Speichern des Scans. Bitte überprüfen Sie Ihre Eingaben."
    else:
        form = NfcScanForm(instance=scan)

    context = {
        'tag': tag,
        'scan': scan,
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
    }

    return render(request, 'view_tag.html', context)


@login_required
def scan_list(request):
    kunden = Kunden.objects.annotate()
    today = date.today()

    return render(request, 'scan_list.html', {'kunden': kunden, 'today': today})
def check_all_scanned(request, kunden_id):
    kunde = get_object_or_404(Kunden, id=kunden_id)
    nfctags = NfcTag.objects.filter(kunde=kunde)
    scanned_tags = NfcScan.objects.filter(tag__in=nfctags)

    if scanned_tags.count() == nfctags.count():
        return HttpResponse("All NFC tags have been scanned.")
    else:
        return HttpResponse("Not all NFC tags have been scanned.")

def not_scanned_tags(request, kunden_id):
    kunde = Kunden.objects.get(id=kunden_id)
    nfctags = NfcTag.objects.filter(kunde=kunde)
    scanned_tags = NfcScan.objects.filter(tag__in=nfctags)

    not_scanned_tags = nfctags.exclude(id__in=scanned_tags.values_list('tag_id', flat=True))

    return render(request, 'not_scanned_tags.html', {'tags': not_scanned_tags})
