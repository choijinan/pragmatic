from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # profile의 주인이 누구인지 알려주는 코드

    image = models.ImageField(upload_to='profile/', null=True) # 유저의 이미지는 서버에 저장될 것이고 그경로를 설정, 꼭 사진이없어도된다 null
    nickname = models.CharField(max_length=20, unique=True, null=True) # unique 로 이 닉네임은 유일하다고 명시하기 즉 닉넴은 하나만 가능 같은닉넴 x
    message = models.CharField(max_length=100, null=True)


