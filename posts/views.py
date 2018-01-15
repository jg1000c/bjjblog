from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self):
        queryset = Post.objects.filter(author__startswith='Jason')
        return queryset

class PostDetailView(DetailView):
    model = Post


class PassingListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'posts/technique_list.html'
    def get_queryset(self):
        queryset = Post.objects.filter(technique_type__startswith='Guard Passing')
        return queryset


class LucasDetailView(DetailView):
    model = Post