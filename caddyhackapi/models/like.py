from django.db import models


class Like(models.Model):
    golfer = models.ForeignKey("Golfer", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
