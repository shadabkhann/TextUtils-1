from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == "on":
        print(removepunc)
        analyzed = djtext
        punctuations = '''!@#$%^&*()<.?/':;\|'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed punctuations', 'Analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to UpperCase', 'Analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Remove New Line', 'Analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed += char
        params = {'purpose': 'Remove extra space', 'Analyzed_text': analyzed}
        djtext = analyzed

    if removepunc != "on" and newlineremover != "on" and fullcaps != "on" and extraspaceremover != "on":
        return HttpResponse("Error !!!")
    return render(request, 'analyze.html', params)
