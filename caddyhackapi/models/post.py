from django.db import models


class Post(models.Model):
    date = models.DateField()
    content = models.CharField(max_length=200)
    course = models.ForeignKey("GolfCourse", on_delete=models.CASCADE)
    image_url = models.ImageField()
    golfer = models.ForeignKey("Golfer", on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        "Golfer", through='Like', related_name='likes')
