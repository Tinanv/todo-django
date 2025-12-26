from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

