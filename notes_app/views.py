from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .models import Note
from django.utils import timezone
from .forms import NoteForm


def home(request):
    notes = get_list_or_404(Note)[::-1]
    context = {'notes': notes}
    return render(request, 'notes/home.html', context)


def details(request, note_id):
    notes = get_list_or_404(Note, pk=note_id)
    return render(request, 'notes/details.html', {'notes': notes})


def confirm_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    context = {'note': note}
    if request.method=='POST':
        note.delete()
        return redirect('home')
    else:
        return render(request, 'notes/confirm.html', context)


def new_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()

    context = {'form': form}
    return render(request, 'notes/new_note.html', context)
