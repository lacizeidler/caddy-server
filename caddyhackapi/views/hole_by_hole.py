from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from caddyhackapi.models.golf_course import GolfCourse
from caddyhackapi.models.golfer import Golfer
from caddyhackapi.models.hole_by_hole import HoleByHole
from rest_framework import status
from rest_framework.exceptions import ValidationError
from caddyhackapi.models.individual_hole import IndividualHole
from caddyhackapi.models.num_of_holes import NumOfHoles
from rest_framework.decorators import action


class HoleByHoleView(ViewSet):
    def list(self, request):
        hole_by_hole = HoleByHole.objects.all()
        serializer = HoleByHoleSerializer(hole_by_hole, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        hole_by_hole = HoleByHole.objects.get(pk=pk)
        serializer = HoleByHoleSerializer(hole_by_hole)
        return Response(serializer.data)

    def create(self, request):
        golfer = Golfer.objects.get(user_id=request.auth.user_id)
        golf_course = GolfCourse.objects.get(pk=request.data['course_id'])
        num_of_holes = NumOfHoles.objects.get(
            pk=request.data['num_of_holes_id'])
        try:
            hole_by_hole = HoleByHole.objects.create(
                date=request.data['date'],
                course=golf_course,
                num_of_holes=num_of_holes,
                share=request.data['share'],
                golfer=golfer
            )
            serializer = HoleByHoleSerializer(hole_by_hole)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            hole_by_hole = HoleByHole.objects.get(pk=pk)
            hole_by_hole.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except HoleByHole.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=False)
    def userholebyhole(self, request):
        golfer = Golfer.objects.get(user=request.auth.user)
        hole_by_holes = HoleByHole.objects.filter(golfer=golfer)
        serializer = HoleByHoleSerializer(hole_by_holes, many=True)
        return Response(serializer.data)
    

class HoleByHoleSerializer(ModelSerializer):
    class Meta:
        model = HoleByHole
        fields = ('id', 'date', 'share', 'course', 'golfer', 'num_of_holes')
        depth = 2

class IndividualHoleSerializer(ModelSerializer):
    class Meta:
        model = IndividualHole
        fields = ('id', 'par', 'score', 'hole_num', 'hole_by_hole')
        depth = 2