from django.shortcuts import render

def gulya(request):
    return render(request, 'gulhayo.html')

def guli(request):
    return render(request, 'gulbahor.html')

def shax(request):
    return render(request, 'shaxnoza.html')

def umi(request):
    return render(request, 'umida.html')

def seva(request):
    return render(request, 'sevara.html')

def begim(request):
    return render(request, 'oybegim.html')
