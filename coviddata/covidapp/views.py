from django.shortcuts import render
import urllib,json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Create your views here.

def home(request):
    url="https://api.covid19india.org/data.json"
    res=urllib.request.urlopen(url)
    data=json.loads(res.read())
    return render(request,'home.html',{'data':data})