from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    post = models.CharField(max_length=300, null=True, blank = True)
    posted_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    number_of_replies = models.IntegerField(default=0,null=True, blank=True)
    def __unicode__(self):
        return self.user.username + " " +"said " + self.post
    
        
class Reply(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    post = models.ForeignKey(Post, null=True, blank=True)
    reply = models.CharField(max_length=300, null=True, blank = True)
    posted_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.user.username + " " +"replied" + self.reply
     