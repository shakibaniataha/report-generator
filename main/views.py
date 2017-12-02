# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from main.forms import SignUpForm
from .models import API
from django.http import JsonResponse
import json

def index(request):
    apis = API.objects.all()
    return render(request, 'main/index.html', {'apis': apis})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def ajaxGetAPIRequests(request):
    api_id = str(request.GET['api_id'])
    api = API.objects.get(id=api_id)
    owner_requests = api.request_set.filter(owner__username=request.user)

    response  = []
    for owner_req in owner_requests:
        params = owner_req.input_params
        response.append({
            "id": owner_req.id,
            "api_name": owner_req.api_id.name,
            "preferred_run_date": owner_req.preferred_run_date,
            "params": json.dumps(params) if params else "",
            "status": owner_req.status
        })

    return JsonResponse(response, safe=False)