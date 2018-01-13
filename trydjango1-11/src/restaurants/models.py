from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):  # inheritance
	name	 	= models.CharField(max_length=120)  # run migration to create model
	location 	= models.CharField(max_length=120, null=True, blank= True) #add field location to model then migrate to save
	category 	= models.CharField(max_length=120, null=True, blank= True)
	timestamp	= models.DateTimeField(auto_now= True)
	updated		= models.DateTimeField(auto_now_add=True) # date saved automatically

	# check out fields

	def _str_(self):
		return self.name

