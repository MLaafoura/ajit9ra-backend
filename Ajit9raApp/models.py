from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, fullName, phone_number, website="", password=None):
        if not email:
            raise ValueError('Users must have an email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, fullName=fullName, phone_number=phone_number, website=website)
        user.set_password(password)

        user.save()

        return user


class AgentAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    fullName = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    website = models.CharField(max_length=255, default="")
    is_active = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName', 'phone_number']

    def get_full_name(self):
        return self.fullName

    def __str__(self):
        return self.email

