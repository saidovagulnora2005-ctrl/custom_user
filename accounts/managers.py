from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,**extra_fields):
            extra_fields.setdefault('is_active',True)
            extra_fields.setdefault('is_staff',True)
            extra_fields.setdefault('is_superuser',True)

            if extra_fields.get('is_active') is not True:
                raise ValueError("Superuser must be active") 
            if extra_fields.get('is_staff') is not True:
                raise ValueError("In superuser is_staff must be true") 
            if extra_fields.get('is_superuser') is not True:
                raise ValueError("In superuser is_superuser must be true") 
            
            return self.create_user(email,password,**extra_fields)

    