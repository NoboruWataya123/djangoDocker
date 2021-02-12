from django.db import models

class Author(models.Model):

    name = models.TextField()

class Course(models.Model):

    name = models.TextField()

    category = models.TextField()

    date = models.DateField()

    owner = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
