from __future__ import unicode_literals

from django.db import models


class Status(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(default="Eau de Web", max_length=50)

    def __unicode__(self):
        return '{} by {}'.format(self.text, self.author)


class Curs(models.Model):
	nume = models.CharField(max_length=40)

class User(models.Model):
	nume = models.CharField(max_length=50)
 	email = models.CharField(max_length=50)
 	parola = models.CharField(max_length=50)
 	scoala = models.CharField(max_length=50)
 	#cursuri_inscris = models.ForeignKey(Curs, on_delete=models.CASCADE)
 	cursuri_inscris = models.TextField()

class College(models.Model):
	nume = models.CharField(max_length=50)
	cursuri = models.TextField()



	