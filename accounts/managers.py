from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.apps import apps

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        if not username:
            raise ValueError(_("The Username must be set"))

        email = self.normalize_email(email)

        # Fetch model dynamically to avoid circular import
        CustomUser = apps.get_model('accounts', 'CustomUser')

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError(_("A user with this email already exists."))

        user = CustomUser(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, username, password, **extra_fields)
