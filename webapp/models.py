import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


# Email verification model
class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    verified = models.BooleanField(default=False)

    @property
    def token_expired(self):
        expiration_duration = timedelta(hours=3)
        return self.created_at < timezone.now() - expiration_duration


# Send reset password email model
class ResetForgottenPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    @property
    def token_expired(self):
        expiration_duration = timedelta(hours=3)
        return self.created_at < self.created_at - expiration_duration
