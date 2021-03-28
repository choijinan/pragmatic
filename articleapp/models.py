from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True) # null이어도 된다!!
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True) # 긴 글이 될수도있으니 TextField로 선언

    created_at = models.DateField(auto_now_add=True, null=True) # 언제 생성했는지 확인하는 코드