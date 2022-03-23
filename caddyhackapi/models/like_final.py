from django.db import models


class LikeFinal(models.Model):
    golfer = models.ForeignKey("Golfer", on_delete=models.CASCADE)
    final_score = models.ForeignKey("FinalScore", on_delete=models.CASCADE)
