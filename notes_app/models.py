from django.db import models


class Note(models.Model):
    note_title = models.CharField(max_length=50)
    note_text = models.TextField(max_length=250, blank=True)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.note_title

    def save_note(self):
        return self.save()

    def delete_note(self):
        return self.delete()
