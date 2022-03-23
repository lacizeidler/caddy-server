from django.db import models


class LikeTable(models.Model):
    golfer = models.ForeignKey("Golfer", on_delete=models.CASCADE)
    hole_by_hole = models.ForeignKey("HoleByHole", on_delete=models.CASCADE)
