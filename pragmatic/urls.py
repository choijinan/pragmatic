"""pragmatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from articleapp.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),

    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')), # account/ 한다음 accountapp 안에있는 url이 추가로 붙는다 즉, :8080/account/hello_world 이런식이됨!!
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 이 설정을 해줘야 프로필 이미지가 나옴 미디어와 연결시켜주는 역할의 코드이다. media에 연결됨
