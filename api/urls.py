from django.urls import path, include
from .views import ArticleList, ArticleDetail, UserList, UserDetail
# from rest_framework.authtoken.views import obtain_auth_token

app_name = "api"

urlpatterns = [
    # path('token/', obtain_auth_token),
    # path('token/revoke', TokenRevoke.as_view(), name='token_revoke'),
    path('rest-auth/', include('dj_rest_auth.urls'), name= 'rest-auth'),

    path('article/', ArticleList.as_view(), name='api-list-article'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='api-detail-article'),
    path('user/', UserList.as_view(), name='api-list-user'),
    path('user/<int:pk>', UserDetail.as_view(), name='api-detail-user'),


]

 