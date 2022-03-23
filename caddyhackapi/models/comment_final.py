from django.db import models


class CommentFinal(models.Model):
    golfer = models.ForeignKey("Golfer", on_delete=models.CASCADE)
    final_score = models.ForeignKey(
        "FinalScore", on_delete=models.CASCADE, related_name="comment_final")
    comment = models.CharField(max_length=500)
