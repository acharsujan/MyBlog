from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	timestrap = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.id}. {self.title}"
	
	