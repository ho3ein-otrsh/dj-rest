import pdb
from tabnanny import verbose
from turtle import pd
from django.db import models
from account.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=50,blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'مقاله'
		verbose_name_plural = 'مقالات'

	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title,allow_unicode=True)
		super(Article, self).save(*args, **kwargs)