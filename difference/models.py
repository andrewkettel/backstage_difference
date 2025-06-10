from django.db import models


class OccurenceCount(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    number = models.IntegerField(default=0)
    value = models.IntegerField(default=0)
    occurences = models.IntegerField(default=0)
    last_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"num:{self.number} - value:{self.value} - occ:{self.occurences}"
