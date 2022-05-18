from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'Store/index.html', context=context)