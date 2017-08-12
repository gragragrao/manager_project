# -*- coding: utf-8 -*-
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, identifier, email, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address')

        email = UserManager.normalize_email(email)
        user = self.model(
            identifier=identifier,
            email=email,
            is_active=True,
            last_login=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
