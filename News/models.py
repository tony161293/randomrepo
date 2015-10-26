from django.db import models
from django.utils import timezone
import datetime
#import os
# from time import time

#@staticmethod
#def get_file_path(self, instance, filename):
#   return "media/%s_%s" % (str(time()).replace('.','_').filename)


class News(models.Model):

    def render(self, context):
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''

    pub_date = models.DateTimeField('date published')
    newsHead = models.CharField(max_length=200)
    news_image =models.ImageField(upload_to ="images", blank = True)
    news_thumb =models.ImageField(upload_to ="images", blank = True)
    newsContent=models.TextField()


    def __unicode__(self):
        return u'%s' % (self.newsHead)

    def save(self, *args, **kwargs):
            News.objects.all().order_by('-pub_date')
            super(News, self).save(*args, **kwargs)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


    #def get_absolute_url(self):
        #return ('(?P<pk>\d+)',(),{'pk':self.id})

# Create your models here.
