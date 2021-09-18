from rest_framework import viewsets
from blog.models import Post
from blog.serializers import PostSerializer
from user_profile.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        if self.request.user.is_staff and self.request.query_params.get('editor') == 'True':
            return Post.objects.all()
        else:
            return Post.objects.filter(published=True)