from django.db import models


class HoleByHole(models.Model):
    date = models.DateField()
    num_of_holes = models.ForeignKey("NumOfHoles", on_delete=models.CASCADE)
    course = models.ForeignKey("GolfCourse", on_delete=models.CASCADE)
    golfer = models.ForeignKey("Golfer", on_delete=models.CASCADE)
    share = models.BooleanField()
