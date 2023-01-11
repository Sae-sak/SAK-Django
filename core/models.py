from django.db import models


class Project(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title} from {self.year}'