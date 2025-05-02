import pyotp

from django.contrib.auth.models import AbstractBaseUser,\
BaseUserManager, PermissionsMixin

from django.db import models



class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, token=None):
        if username is None:
            raise TypeError('User must have a username')
        
        if email is None:
            raise TypeError('User must have an email address')
        
        if token is None:
            raise TypeError('User must have a token base32')
        
                    
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            token_base32=token
        )
        
        user.set_password(password)
        user.save()


        return user
    
    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superuser must have a password')


        user = self.create_user(
            username, 
            email, 
            password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save()


        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    token_base32 = models.TextField(default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._get_token_now()


    @property
    def token_object(self):
        return self._get_token_totp()


    
    def token_isvalid(self, token):
        return self.token_object.verify(token)


    def get_full_name(self):
        return self.username
    

    def get_short_name(self):
        return self.username
    

    def _get_token_totp(self):
        totp = pyotp.TOTP(self.token_base32)
        
        return totp


    def _get_token_now(self):
        return self.token_object.now()



