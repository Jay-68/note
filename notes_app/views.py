from django.shortcuts import render, get_list_or_404
from .models import Note
from django.utils import timezone


def home(request):
  notes = get_list_or_404(Note)
  return render(request, 'notes/home.html', {'notes': notes})

def details(request, note_id):
    notes=get_list_or_404(Note, pk = note_id)
    return render(request, 'notes/details.html', {'notes': notes})

def confirm_delete(request):
  return render(request,'notes/confirm.html')