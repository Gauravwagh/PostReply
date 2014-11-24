from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


from postreply.models import Post, Reply
# Create your views here.
def home(request):
    post = Post.objects.all().order_by('-posted_date')
    for one in post:
        reply = list(Reply.objects.filter(post=one).order_by('-posted_date'))
        one.reply = reply
        print one.reply
    print post
    return render(request,'postreply.html', {'post':post})

@csrf_exempt
def post(request):
    postdata = request.POST["post"]
    userdata = request.user
    postobj = Post(user = userdata, post = postdata, posted_date = timezone.now(),updated = None, number_of_replies = 0)
    postobj.save()
    return render(request, 'postreply.html')

@csrf_exempt
def reply(request):
    replydata = request.POST["reply"]
    postid = request.POST["postid"]
    print replydata
    print postid
    postobj = Post.objects.get(id=int(postid))
    userdata = request.user
    replyobj = Reply(user = userdata, reply = replydata,post = postobj, posted_date = timezone.now(),updated = None)
    replyobj.save()
    return render(request, 'postreply.html')


