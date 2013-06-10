from django.db import models
import hashlib

# Create your models here.

class Account(models.Model):

    email = models.CharField(max_length = 128)
    password = models.CharField(max_length = 128)
    first_name = models.CharField(max_length = 128)
    is_active = models.CharField(max_length = 128)


    def is_authenticated(self):
        return True


    def hashed_password(self, password = None):
        if not password:
            return self.password
        else:
            return hashlib.md5(password).hexdigest()


    def check_password(self, password):
        if self.hashed_password(password) == self.password:
            return True
        return False

    class Meta:
        db_table = 'account'


