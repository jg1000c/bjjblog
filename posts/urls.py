from django.conf.urls import url, include

from .views import PostListView, PostDetailView, PassingListView, OpenGuardListView, HalfGuardListView

app_name = 'posts'

urlpatterns = [
    url(r'(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^passing/', PassingListView.as_view(), name='passinglist'),
    url(r'^openguard/', OpenGuardListView.as_view(), name='openguardlist'),
    url(r'^halfguard/', HalfGuardListView.as_view(), name='halfguardlist'),
    url(r'^', PostListView.as_view(), name='list'),


]
