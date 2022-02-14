from django.shortcuts import render

# Create your views here.

def document_a4(request):
    return render(request, 'index.html')
