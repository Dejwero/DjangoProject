from django.db import models

PROFILE_STATUS=(
    ('unfollowed', 'Unfollowed'),
    ('followed', "Followed")
)


class Profile(models.Model):
    user_name = models.TextField(max_length = 50)
    age = models.IntegerField()
    bio = models.TextField(max_length= 200)
    # profile_img = models.ImageField()
    status = models.CharField(choices=PROFILE_STATUS, max_length=30, default='unfollowed')

    def __str__(self):
        return self.user_name


class Image(models.Model):
    description = models.TextField(max_length= 400)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Like(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=500)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    # vfasivy

    def __str__(self):
        return ""