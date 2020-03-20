from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('note_title', 'note_text')
        widgets={'note_text':SummernoteWidget()}
