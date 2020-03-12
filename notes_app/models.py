from django.db import models

class Note(models.Model):
  note_title=models.CharField(max_length=50,default='Title')
  note_text=models.CharField(max_length=250)
  publish_date=models.DateTimeField()