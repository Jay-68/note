from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# class NoteForm(forms.Form):
#     note_title = forms.CharField(max_length=20)
#     note_text = forms.CharField(max_length=300,widget=SummernoteWidget())


from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('note_title', 'note_text')
        widgets={'note_text':SummernoteWidget()}
