from caddyhackapi.models.comment import Comment
from caddyhackapi.models.golfer import Golfer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from caddyhackapi.models.post import Post
from caddyhackapi.models.comment_final import CommentFinal
from caddyhackapi.models.final_score import FinalScore


class CommentFinalView(ViewSet):
    def retrieve(self, request, pk):
        golfer = Golfer.objects.get(user=request.auth.user)
        try:
            comment = Comment.objects.get(pk=pk)
            if comment.golfer == golfer:
                comment.is_owner = True
            else:
                comment.is_owner = False
            serializer = GetCommentFinalSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        final_comments = CommentFinal.objects.all()
        golfer = Golfer.objects.get(user=request.auth.user)
        for comment in final_comments:
            if comment.golfer == golfer:
                comment.is_owner = True
            else:
                comment.is_owner = False

        serializer = GetCommentFinalSerializer(final_comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        final_score = FinalScore.objects.get(pk=request.data['final_score_id'])
        golfer = Golfer.objects.get(user_id=request.auth.user_id)

        serializer = CreateCommentFinalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(golfer=golfer, final_score=final_score)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        final_comment = CommentFinal.objects.get(pk=pk)
        final_comment.comment = request.data['comment']
        final_comment.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        final_comment = CommentFinal.objects.get(pk=pk)
        final_comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GetCommentFinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentFinal
        fields = ('id', 'comment', 'golfer', 'final_score', 'is_owner')
        depth = 2


class CreateCommentFinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentFinal
        fields = ('comment', 'final_score_id', 'golfer_id')
