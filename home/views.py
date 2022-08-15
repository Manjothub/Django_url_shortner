from django.shortcuts import render
import pyshorteners

def INDEX(request):
    return render(request,'index.html')

def URLSHORTNER(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.chilpit.short(url)
        context ={
            'urls':shortened_url
        }
    return render(request,'done.html',context)