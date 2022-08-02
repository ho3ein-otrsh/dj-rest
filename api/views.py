from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ArticleSerializer,UserSerializer
from account.models import User
from blog.models import Article
from .permissions import IsStaffReadOnlyOrSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework import status

# from rest_framework.views import APIView
# from rest_framework.response import Response


# class TokenRevoke(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def delete(self, request, format=None):
#         request.auth.delete()
        
        
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsStaffOrReadOnly]



class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsStaffReadOnlyOrSuperUser]


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsStaffReadOnlyOrSuperUser]

