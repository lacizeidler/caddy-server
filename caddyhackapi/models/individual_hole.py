from django.db import models


class IndividualHole(models.Model):
    par = models.IntegerField()
    score = models.IntegerField()
    hole_by_hole = models.ForeignKey("HoleByHole", on_delete=models.CASCADE)
    hole_num = models.IntegerField()
