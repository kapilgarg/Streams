# Create your views here.
from time import gmtime, strftime
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponseNotModified
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
import feedparser

# Do not forget to pass RequestContext(request) to render_to_response otherwise setting variables like static_url won't
# be recognized.
from StreamApp.models import feed_inventory

def home(request):
    my_feeds = feed_inventory.objects.all()
    return render_to_response('Home.html',{'feeds':my_feeds},RequestContext(request))

def feeds(request,feed_id):
#    Get feed url corrosponding to the feed_id
    my_feeds = feed_inventory.objects.all()
    feed = feed_inventory.objects.get(id=feed_id)
    data = feedparser.parse(feed.feed_url,feed.modified_date)
    return render_to_response('Home.html',{'data':data,'feeds':my_feeds},RequestContext(request))

@csrf_exempt
def add_new_feed(request):
    url = request.POST['newfeedurl']
    feed = feed_inventory.objects.filter(feed_url=url)
    if feed.count() == 0 :
        data = feedparser.parse(url)
        new_feed = feed_inventory(feed_name=data.feed.title,feed_url=url,modified_date = strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        new_feed.save()
        feed = feed_inventory.objects.get(feed_url=url)
        return HttpResponseRedirect('/reader/feeds/'+str(feed.id))
    else:
        return HttpResponseRedirect('/reader/feeds/'+str(feed[0].id))






