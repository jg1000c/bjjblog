from django.conf.urls import url

from .views import PostListView, PostDetailView, PassingListView

app_name = 'posts'

urlpatterns = [
    url(r'(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^passing/', PassingListView.as_view(), name='passinglist'),
    url(r'^', PostListView.as_view(), name='list'),



]
