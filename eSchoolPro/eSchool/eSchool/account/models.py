from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=255,verbose_name='昵称',
                                blank=True, null=True)
    gender = models.CharField(max_length=6, choices=(('male','男'),('female','女')),
    						default='female',verbose_name='性别')
    VISITOR = 0
    STUDENT = 1
    PARENT = 2
    TEACHER = 3
    ROLES = (
        (VISITOR, 'vistor'),
        (STUDENT,
         'student'),
        (PARENT,
         'parent'),
        (TEACHER, 'teacher'),
    )
    role = models.IntegerField(
        choices=ROLES,
        default=VISITOR)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    birth = models.DateField(blank=True, null=True)
    interest = models.TextField(blank=True, null=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)