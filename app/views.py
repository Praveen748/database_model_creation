from django.shortcuts import render

# Create your views here.
from app.models import *
def topic_template(request):
    topic=Topic.objects.all()
    d={'topic':topic}

    return render(request,'topic_template.html',d)

def webpage_template(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'webpage.html',d)

def access_record(request):
    accessrecords=Accessrecord.objects.all()
    d={'accessrecords':accessrecords}
    return render(request,'access_record.html',d)
