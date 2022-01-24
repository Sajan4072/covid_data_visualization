from django.shortcuts import render
import urllib,json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Create your views here.

def home(request):
    url="https://api.covid19india.org/data.json"
    res=urllib.request.urlopen(url)
    data=json.loads(res.read())

    # passing to chartjs scripts
    labels=[]
    chartdata=[]
    for state in data['statewise']:
        labels.append(state['state'])
        chartdata.append(state['confirmed'])


    return render(request,'home.html',{'data':data,'labels':labels,'chartdata':chartdata})