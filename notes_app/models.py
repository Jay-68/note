from django.db import models
from django.utils import timezone


class Note(models.Model):
    note_title = models.CharField(max_length=50)
    note_text = models.TextField(max_length=250)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.note_title

    def save_note(self):
        return self.save()

    def delete_note(self):
        return self.delete()
