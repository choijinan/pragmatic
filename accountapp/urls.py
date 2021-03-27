from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp" # 이렇게 하면 주소를 간단하게 나타낼수 있음!! 좋은거임 accountapp:아래의 name 즉 'account:name' 이런식으로 사용가능!! url호출시에



urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'), # route를 설정하고, view를 추가해주고, name을 추가해준다!!

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'), # 로그인은 template를 지정해줘야함
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # primary_key 가 필요함 특정 유저의 고유키를 의미!!
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]