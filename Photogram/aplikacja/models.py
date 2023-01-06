from django.db import models

PROFILE_STATUS=(
    ('unfollowed', 'Unfollowed'),
    ('followed', "Followed")
)


class Profile(models.Model):
    user_name = models.TextField(max_length = 50)
    age = models.IntegerField(max_length=3)
    bio = models.TextField(max_length= 200)
    #profile_img = models.ImageField()
    status = models.CharField(choices=PROFILE_STATUS, max_length=30, default='unfollowed')

class Image(models.Model):
    description = models.TextField(max_length= 400)

class Like(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField(max_length= 1000)