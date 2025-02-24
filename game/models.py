from django.db import models

class DialogueChoice(models.Model):
    text = models.CharField(max_length=200)
    next_dialogue = models.IntegerField()

    def __str__(self):
        return self.text