from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topic(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.filter(name__startswith='a')
    QSWO=Webpage.objects.filter(name__endswith='i')
    QSWO=Webpage.objects.filter(name__contains='a')
    QSWO=Webpage.objects.filter(url__endswith='in')

    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QSAO=AccessRecord.objects.all()
    QSAO=AccessRecord.objects.filter(date__year='2000')
    QSAO=AccessRecord.objects.filter(date__month='08')
    QSAO=AccessRecord.objects.filter(date__day='24')
    QSAO=AccessRecord.objects.filter(date__year__gt='2000')
    QSAO=AccessRecord.objects.filter(date__year__lt='2000')
    QSAO=AccessRecord.objects.filter(date__year__gte='2000')
    QSAO=AccessRecord.objects.filter(date__year__lte='2000')
    QSAO=AccessRecord.objects.filter(author__startswith='t')
    d={'QSAO':QSAO}
    return render(request,'display_access.html',d)



