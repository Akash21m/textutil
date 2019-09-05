# I have created this file......

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")
def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    upper=request.POST.get('upper','off')
    spaceremover=request.POST.get('spaceremover','off')
    newlineremover=request.POST.get('newlineremover','off')
    if (removepunc == "on"):
        puncutuations = '''!-[](){};:'"\,<>./?@#$%^&*_~'''
        #analyze the text
        analyzed= ""
        for char in djtext:
            if char not in puncutuations:
                analyzed=analyzed + char

        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if (upper == "on"):
        analyzed= ""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Change into Upper Case', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if (spaceremover == "on"):
        analyzed= ""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]== " ":
                pass
            else:
                analyzed= analyzed + char
        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if (newlineremover =="on"):
        analyzed= ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed= analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext=analyzed

    if (removepunc != "on" and upper != "on" and spaceremover != "on" and newlineremover != "on"):
         return HttpResponse("Please select any operation and try again....")
        #return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)
   # return HttpResponse("RemovePunc <a href='/'>Back</a>")
