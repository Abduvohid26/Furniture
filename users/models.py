from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from shared.models import BaseModel

ADMIN, MANAGER, WORKER = ('admin', 'manager', 'worker')


class User(AbstractUser, BaseModel):
    USER_ROLES = (
        (ADMIN, ADMIN),
        (MANAGER, MANAGER),
        (WORKER, WORKER),
    )
    user_roles = models.CharField(max_length=100, choices=USER_ROLES, default=WORKER)

    def __str__(self):
        return self.username

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }

    def check_hash_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

    def save(self, *args, **kwargs):
        self.check_hash_password()
        super(User, self).save(*args, **kwargs)










