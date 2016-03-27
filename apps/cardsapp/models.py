from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Card(models.Model):
	title = models.CharField(max_length=45)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'cards'

class Note(models.Model):
	card = models.ForeignKey(Card)
	body = models.TextField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	def __str__(self):
		return "This is note #%s" % self.id

	class Meta:
		db_table = 'notes'