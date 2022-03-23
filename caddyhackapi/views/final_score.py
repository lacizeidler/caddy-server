from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from caddyhackapi.models.final_score import FinalScore
from caddyhackapi.models.golfer import Golfer
from caddyhackapi.models.golf_course import GolfCourse
from caddyhackapi.models.num_of_holes import NumOfHoles
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action


class FinalScoreView(ViewSet):
    def list(self, request):
        golfer = Golfer.objects.get(user=request.auth.user)
        final_score = FinalScore.objects.filter(golfer=golfer)
        serializer = FinalScoreSerializer(final_score, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        final_score = FinalScore.objects.get(pk=pk)
        serializer = FinalScoreSerializer(final_score)
        return Response(serializer.data)

    def create(self, request):
        golfer = Golfer.objects.get(user_id=request.auth.user_id)
        golf_course = GolfCourse.objects.get(pk=request.data['course_id'])
        num_of_holes = NumOfHoles.objects.get(
            pk=request.data['num_of_holes_id'])
        try:
            final_score = FinalScore.objects.create(
                date=request.data['date'],
                course=golf_course,
                par=request.data['par'],
                score=request.data['score'],
                share=request.data['share'],
                golfer=golfer,
                num_of_holes=num_of_holes
            )
            serializer = FinalScoreSerializer(final_score)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            final_score = FinalScore.objects.get(pk=pk)
            final_score.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except FinalScore.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        final_score = FinalScore.objects.get(pk=pk)
        final_score.score = request.data['score']
        final_score.par = request.data['par']
        final_score.share = request.data['share']
        final_score.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False)
    def sharedfinal(self, request):
        final_scores = FinalScore.objects.filter(share=1)
        serializer = FinalScoreSerializer(final_scores, many=True)
        return Response(serializer.data)
    
    @action(methods=['put'], detail=True)
    def like(self, request, pk):
        golfer = Golfer.objects.get(user_id=request.auth.user_id)
        final_score = FinalScore.objects.get(pk=pk)
        final_score.likes.add(golfer)
        return Response({'message': 'Liked Post'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def unlike(self, request, pk):
        golfer = Golfer.objects.get(user_id=request.auth.user_id)
        final_score = FinalScore.objects.get(pk=pk)
        final_score.likes.remove(golfer)
        return Response({'message': 'Unlike Post'}, status=status.HTTP_201_CREATED)


class FinalScoreSerializer(ModelSerializer):
    class Meta:
        model = FinalScore
        fields = ('id', 'date', 'score', 'share',
                  'par', 'golfer', 'course', 'num_of_holes', 'comment_final', 'final_likes')
        depth = 2
