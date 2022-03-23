from django.db import models


class CommentTable(models.Model):
    golfer = models.ForeignKey("Golfer", on_delete=models.CASCADE)
    hole_by_hole = models.ForeignKey(
        "HoleByHole", on_delete=models.CASCADE, related_name="comment_table")
    comment = models.CharField(max_length=500)
