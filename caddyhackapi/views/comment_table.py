from caddyhackapi.models.golfer import Golfer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from caddyhackapi.models.comment_table import CommentTable
from caddyhackapi.models.hole_by_hole import HoleByHole


class CommentTableView(ViewSet):
    def retrieve(self, request, pk):
        golfer = Golfer.objects.get(user=request.auth.user)
        try:
            comment = CommentTable.objects.get(pk=pk)
            if comment.golfer == golfer:
                comment.is_owner = True
            else:
                comment.is_owner = False
            serializer = GetCommentTableSerializer(comment)
            return Response(serializer.data)
        except CommentTable.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        table_comments = CommentTable.objects.all()
        golfer = Golfer.objects.get(user=request.auth.user)
        for comment in table_comments:
            if comment.golfer == golfer:
                comment.is_owner = True
            else:
                comment.is_owner = False

        serializer = GetCommentTableSerializer(table_comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        hole_by_hole = HoleByHole.objects.get(pk=request.data['hole_by_hole_id'])
        golfer = Golfer.objects.get(user_id=request.auth.user_id)

        serializer = CreateCommentTableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(golfer=golfer, hole_by_hole=hole_by_hole)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        table_comment = CommentTable.objects.get(pk=pk)
        table_comment.comment = request.data['comment']
        table_comment.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        table_comment = CommentTable.objects.get(pk=pk)
        table_comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GetCommentTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentTable
        fields = ('id', 'comment', 'golfer', 'hole_by_hole', 'is_owner')
        depth = 2


class CreateCommentTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentTable
        fields = ('comment', 'hole_by_hole_id', 'golfer_id')
