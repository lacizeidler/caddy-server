from caddyhackapi.models.comment import Comment
from caddyhackapi.models.golfer import Golfer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from caddyhackapi.models.post import Post


class CommentView(ViewSet):
    def retrieve(self, request, pk):
        golfer = Golfer.objects.get(user=request.auth.user)
        try:
            comment = Comment.objects.get(pk=pk)
            if comment.golfer == golfer:
                comment.is_owner = True
            else:
                comment.is_owner = False
            serializer = GetCommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        comments = Comment.objects.all()
        golfer = Golfer.objects.get(user=request.auth.user)
        for comment in comments:
            if comment.golfer == golfer:
                comment.is_owner = True
            else:
                comment.is_owner = False

        serializer = GetCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        post = Post.objects.get(pk=request.data['post_id'])
        golfer = Golfer.objects.get(user_id=request.auth.user_id)

        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(golfer=golfer, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.comment = request.data['comment']
        comment.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GetCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'golfer', 'post', 'is_owner')
        depth = 2


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'post_id', 'golfer_id')
