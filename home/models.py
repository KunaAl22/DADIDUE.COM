from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=25)
    email=models.CharField(max_length=30)
    number=models.CharField(max_length=12)
    description=models.TextField(max_length=100)
    date=models.DateField()

    def __str__(self) :
        return self.name



class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Article Writing', 'Article Writing'),
			('Creative Design', 'Creative Design'),
			('Graphic Design', 'Graphic Design'),
			('Logo Design', 'Logo Design'),
			('Photo Editing', 'Photo Editing'),
			('Video Editing', 'Photo Editing'),
			('Photo Editing', 'Photo Editing'),
			('Audio, Music Edit', 'Audio, Music Edit'),

			) 
	

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True,max_length=5 )
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('On Process', 'On Process'),
			('Completed', 'Completed'),
						)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.product.name 

