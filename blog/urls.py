from django.urls import path
from .views import ArticleList, ArticleDetail,ArticleCreate

app_name = "blog"

urlpatterns = [
	path("", ArticleList.as_view(), name="list"),
	path("<int:pk>", ArticleDetail.as_view(), name="detail"),
	path('article/create',ArticleCreate.as_view(),name='create')
]
