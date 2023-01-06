from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField('user_name', max_length=15, null=False, unique=True, primary_key=True)
    password = models.CharField('password', max_length=20, null=False)

    def __str__(self):
        return f'{self.user_name}'


class UserInfo(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    mobile = models.CharField('mobile', unique=True, max_length=10)
    first_name = models.CharField('first_name', max_length=35, null=False)
    last_name = models.CharField('last_name', max_length=55, null=False)
    birthdate = models.DateField('birthdate', null=False)
    gender = models.CharField('gender', max_length=10, choices=[('1', 'Male'), ('2', 'Female')])
    address = models.CharField(max_length=100, null=False)
    profile_image = models.ImageField(upload_to='Photos/User', default='Photos/User/unknownen.png')

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.mobile}'
