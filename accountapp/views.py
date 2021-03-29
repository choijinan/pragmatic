from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]    # 이렇게 데코레이터 명들을 새로운 변수에 배열(리스트)형태로 선언해서 넣어주면
                                                                # 4줄짜리 데코레이터를 2줄로 줄일 수 있다.
                                                                # has_ownership을 @method_decorator()안에서 실행시킬 데코레이터 명으로 넣어주면
                                                                # 알아서 배열안에 들어있는 데코레이터를 다 실행시킨다!! 꿀같은 정보!!


class AccountCreateView(CreateView): # 회원가입
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login') # 계정생성 성공시 이동할 url
    template_name = 'accountapp/create.html' # 회원가입을 할 때 볼 html을 지정해주기


class AccountDetailView(DetailView, MultipleObjectMixin): # 개인정보 확인
    model = User
    context_object_name = 'target_user' # 이걸 설정해줘야 , 다른 사람이 내 페이지를 와도 자기 정보가 아닌 내 정보를 볼 수 있음!!!
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get') # 일반 function에 사용하는 데코레이터를 method에사용할 수 있도록 해주는 데코레이터다.
@method_decorator(has_ownership, 'post') # 첫번째 인자는 사용하고자 했던 login_required 데코레이터를 써주고 두번째 인자는 get 또는 post 타입을 적어주면된다.
class AccountUpdateView(UpdateView): # 회원가입 CreateView랑 거의 동일함 , 회원정보변경
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:detail') # 정보 변경 성공시 이동할 url
    template_name = 'accountapp/update.html' # 회원정보 변경을 할 때 볼 html을 지정해주기


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView): # 회원탈퇴
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

