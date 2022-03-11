from unicodedata import name
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from caddyhackapi.models.golf_course import GolfCourse


class GolfCourseView(ViewSet):
    def list(self, request):
        golf_courses = GolfCourse.objects.all()
        serializer = GolfCourseSerializer(golf_courses, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        golf_course = GolfCourse.objects.get(pk=pk)
        serializer = GolfCourseSerializer(golf_course)
        return Response(serializer.data)
    
    def create(self, request):
        golf_course = GolfCourse.objects.create(
            name = request.data['name'],
            address = request.data['address'],
            state = request.data['state'],
            zipcode = request.data['zipcode']
        )
        serializer = GolfCourseSerializer(golf_course)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        golf_course = GolfCourse.objects.get(pk=pk)
        golf_course.name = request.data['name']
        golf_course.address = request.data['address']
        golf_course.state = request.data['state']
        golf_course.zipcode = request.data['zipcode']
        golf_course.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        golf_course = GolfCourse.objects.get(pk=pk)
        golf_course.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GolfCourseSerializer(ModelSerializer):
    class Meta:
        model = GolfCourse
        fields = ('id', 'name', 'address', 'state', 'zipcode')
        depth = 1