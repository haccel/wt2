from django.db import models

# Create your models here.


class Translation(models.Model):
	native_text	= models.CharField(max_length=100)
	foreign_text	= models.CharField(max_length=100)
	description_text	= models.CharField(max_length=1000)
	rating		= models.IntegerField(default=0)
	flags		= models.IntegerField(default=0)
	create_date 	= models.DateTimeField('date created')
	last_date 	= models.DateTimeField('date last showed')