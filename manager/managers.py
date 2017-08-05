# -*- coding: utf-8 -*-
from django.contrib.auth.models import BaseUserManager


class PersonManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        person = self.model(email=self.normalize_email(email))
        person.set_password(password)
        person.save(using=self._db)

        return person
