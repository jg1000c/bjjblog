from django.db import models
from django.core.urlresolvers import reverse

from embed_video.fields import EmbedVideoField


class Post(models.Model):
    author = models.CharField(max_length=50)
    technique_type = models.CharField(max_length=50)
    description =  models.TextField(max_length=3000)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=250)
    video = EmbedVideoField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')