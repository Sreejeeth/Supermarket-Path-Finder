from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#from sirmvit.models import Studentdbs,Category
from django.shortcuts import render, get_object_or_404

# Create your views here.
