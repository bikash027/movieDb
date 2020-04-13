from django.db import models
import datetime
# Create your models here.
class Movie(models.Model):
	name= models.CharField(max_length=200)
	date= models.DateField(default=datetime.date.today)
	genre= models.CharField(max_length=100)
	rating= models.DecimalField(max_digits=2, decimal_places=1)
	creator= models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

	def __str__(self):
		return '%d: %s' %(self.id, self.name)