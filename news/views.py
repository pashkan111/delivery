from django.views import generic

from news.models import Post
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'news_detail.html'