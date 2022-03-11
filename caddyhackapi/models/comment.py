from django.db import models


class Comment(models.Model):
    golfer = models.ForeignKey("Golfer", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)


    @property
    def is_owner(self):
        return self.__is_owner

    @is_owner.setter
    def is_owner(self, value):
        self.__is_owner = value
