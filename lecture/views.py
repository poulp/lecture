#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.contrib.auth.views import login


def home(requests):
    return render_to_response('index.html')


def login_lecture(request, template_name='login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          extra_context=None):
    return login(request, template_name, redirect_field_name, authentication_form, extra_context)