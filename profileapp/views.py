from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form): # post 를 통해 호출되서 form 안에 image, nickname, message 정보를 가지고 있다.
        temp_profile = form.save(commit=False) # commit 을 false로 하면 임시데이터가 저장됨!!
        temp_profile.user = self.request.user # form 을 통해 들어온 user정보를 request 요청보낸 당사자의 user정보로 지정해줌
        temp_profile.save() # 최종적으로 저장
        return super().form_valid(form)

    def get_success_url(self): # pk 값 때문에 그냥 get_success_url에 값을 넣으면 연결이안됨!! 그래서 오버라이드 해주는 것임
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})