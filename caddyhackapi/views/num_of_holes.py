from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from caddyhackapi.models.num_of_holes import NumOfHoles

class NumOfHolesView(ViewSet):
    def list(self, request):
        num_of_holes = NumOfHoles.objects.all()
        serializer = NumOfHolesSerializer(num_of_holes, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        num_of_holes = NumOfHoles.objects.get(pk=pk)
        serializer = NumOfHolesSerializer(num_of_holes)
        return Response(serializer.data)

class NumOfHolesSerializer(ModelSerializer):
    class Meta:
        model = NumOfHoles
        fields = ('id', 'holes')
        depth = 1