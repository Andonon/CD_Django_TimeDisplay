# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    context = {
    "date": now.strftime('%b %d, %Y'),
    "time": now.strftime('%I:%M %p')
    
    }
    return render(request, 'homepage/index.html', context)


