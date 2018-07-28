# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        "current_time": datetime.now
    }
    return render(request, 'first_app/index.html', context)