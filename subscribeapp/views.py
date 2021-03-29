from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})


    def get(self, request, *args, **kwargs):

        # project pk 를 가진 Project 를 찾는데 없다면 404를 돌려줘라 라는 의미의 코드이다.
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user,
                                                   project=project)

        if subscription.exists(): # 구독정보가 있다면
            subscription.delete() # 찾은 구독정보를 없애고
        else: # 구독정보가 존재하지 않는다면
            Subscription(user=user, project=project).save() # 새로 만들어주고 저장한다.

        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    template_name = 'subscribeapp/list.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self):
        # projects 안에는 구독한 모든 프로젝트들이 리스트화되어 담겨진다.
        projects = Subscription.objects.filter(user=self.request.user).values_list('project') # 유저가 구독하고 있는 project를 찾는 코드이다.
        article_list = Article.objects.filter(project__in=projects)
        return article_list
