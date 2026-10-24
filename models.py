from django.db import models
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  age = models.IntegerField(null=True, blank=True)
  city = models.CharField(max_length=100, blank=True)
  gender = models.CharField(max_length=20, blank=True)
  bio = models.TextField(blank=True)

  def __str__(self):
    return self.user.username


class Like(models.Model):
  sender = models.ForeignKey(
      User, related_name='sent_likes', on_delete=models.CASCADE
  )
  receiver = models.ForeignKey(
      User, related_name='received_likes', on_delete=models.CASCADE
  )
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = ('sender', 'receiver')


# Create your models here.
