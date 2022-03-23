from django.db import models


class FinalScore(models.Model):
    date = models.DateField()
    num_of_holes = models.ForeignKey("NumOfHoles", on_delete=models.CASCADE)
    course = models.ForeignKey("GolfCourse", on_delete=models.CASCADE)
    golfer = models.ForeignKey("Golfer", on_delete=models.CASCADE)
    score = models.IntegerField()
    share = models.BooleanField()
    par = models.IntegerField()
    final_likes = models.ManyToManyField(
        "Golfer", through='LikeFinal', related_name='final_likes')
