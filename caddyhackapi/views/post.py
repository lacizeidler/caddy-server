from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from caddyhackapi.models.golfer import Golfer
from caddyhackapi.models.post import Post
from caddyhackapi.models.golf_course import GolfCourse
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.exceptions import ValidationError


class PostView(ViewSet):
    def list(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def like(self, request, pk):
        user = request.auth.user
        post = Post.objects.get(pk=pk)
        post.likes.add(user)
        return Response({'message': 'Liked Post'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def unlike(self, request, pk):
        user = request.auth.user
        post = Post.objects.get(pk=pk)
        post.likes.remove(user)
        return Response({'message': 'Unlike Post'}, status=status.HTTP_201_CREATED)

    def create(self, request):
        golfer = Golfer.objects.get(user_id=request.auth.user_id)
        golf_course = GolfCourse.objects.get(pk=request.data['course_id'])
        try:
            post = Post.objects.create(
                date=request.data['date'],
                course=golf_course,
                content=request.data['content'],
                image_url=request.data['image_url'],
                golfer=golfer
            )
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.content = request.data['content']
        post.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'date', 'content', 'image_url',
                  'course', 'golfer', 'likes', 'comment_post')
        depth = 2
