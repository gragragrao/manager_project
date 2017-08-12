# -*- coding: utf-8 -*-
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class PersonManager(BaseUserManager):

    def create_user(self, identifier, email, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address')

        email = PersonManager.normalize_email(email)
        person = self.model(
            identifier=identifier,
            email=email,
            is_active=True,
            last_login=now,
            **extra_fields
        )
        person.set_password(password)
        person.save(using=self._db)

        return person
