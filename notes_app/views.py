from django.shortcuts import render, get_list_or_404
from .models import Note
from django.utils import timezone
from .forms import NoteForm


def home(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NoteForm()
    notes = get_list_or_404(Note)
    context = {'form': form, 'notes': notes}
    return render(request, 'notes/home.html', context)


def details(request, note_id):
    notes = get_list_or_404(Note, pk=note_id)
    return render(request, 'notes/details.html', {'notes': notes})


def confirm_delete(request):
    return render(request, 'notes/confirm.html')
