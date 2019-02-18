from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)