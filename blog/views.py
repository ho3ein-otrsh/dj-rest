from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView,CreateView
from .models import Article
from django.urls import reverse_lazy



# Create your views here.
class ArticleList(ListView):
	def get_queryset(self):
		return Article.objects.filter(status=True)


class ArticleDetail(DetailView):
	def get_object(self):
		return get_object_or_404(
			Article.objects.filter(status=True),
			pk=self.kwargs.get("pk")
		)

class ArticleCreate(CreateView):
	model = Article
	fields = ['title','author','content','publish','status']
	success_url = reverse_lazy("blog:create")	