from django.shortcuts import render_to_response
from News.models import News
from django.template import RequestContext
#form django.views.generic import DetailView 


def index(request):
    
    items = News.objects.all()[:10]

    q = RequestContext(request, {
                        'item':items
                })    
    
    return render_to_response('index.html', context_instance=q)#Create your views here.



def full_news(request, pk):
    
    #items = News.objects.all()[:10]
    #full_news = get_object_or_404(News, id=pk)
    item = News.objects.get(id=pk)
    
    c = RequestContext(request, {
                        'item':item
                })
                                              
    return render_to_response('full_news.html', context_instance=c)