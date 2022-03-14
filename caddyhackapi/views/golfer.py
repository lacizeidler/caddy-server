from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from caddyhackapi.models.golfer import Golfer
from rest_framework.decorators import action


class GolferView(ViewSet):
    def list(self, request):
        golfer = Golfer.objects.all()
        serializer = GolferSerializer(golfer, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        golfer = Golfer.objects.get(pk=pk)
        serializer = GolferSerializer(golfer)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def currentgolfer(self, request):
        golfer = Golfer.objects.get(user=request.auth.user)
        serializer = GolferSerializer(golfer)
        return Response(serializer.data)


class GolferSerializer(ModelSerializer):
    class Meta:
        model = Golfer
        fields = "__all__"
        depth = 1
