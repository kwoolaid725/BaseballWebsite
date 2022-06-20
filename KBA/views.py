from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Dango Http Response")


#example for choices in model
"""And in the forms.py:
'Metric_name ': forms.Select(attrs={'class': 'form-control'})"""

# Create your views here.
