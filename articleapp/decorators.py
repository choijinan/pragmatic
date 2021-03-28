from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk']) # 요청을 받으면서 primary_key로 받은 값(pk)을 가지고 있는 User.objects가 user가 된다.
        if not article.writer == request.user: # 위에서 선언한 user 가 request.user 가 아니라면
            return HttpResponseForbidden() # 오류페이지를 반환해준다!!
        return func(request, *args, **kwargs) # 맞는 경우에는 이걸 반환해준다. => 맞으니까 그냥 페이지로 보내준다.
    return decorated