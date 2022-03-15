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


class IndividualHoleView(ViewSet):
    def list(self, request):
        individual_holes = IndividualHole.objects.all()
        serializer = IndividualHoleSerializer(individual_holes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        individual_hole = IndividualHole.objects.get(pk=pk)
        serializer = IndividualHoleSerializer(individual_hole)
        return Response(serializer.data)
    
    def create(self, request):
        hole_by_hole = HoleByHole.objects.get(
            pk=request.data['hole_by_hole_id'])
        try:
            individual_hole = IndividualHole.objects.create(
                par=request.data['par'],
                hole_num=request.data['hole_num'],
                hole_by_hole=hole_by_hole,
                score=request.data['score']
            )
            serializer = IndividualHoleSerializer(individual_hole)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            individual_hole = IndividualHole.objects.get(pk=pk)
            individual_hole.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except IndividualHole.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


class IndividualHoleSerializer(ModelSerializer):
    class Meta:
        model = IndividualHole
        fields = ('id', 'par', 'score', 'hole_num', 'hole_by_hole')
        depth = 2