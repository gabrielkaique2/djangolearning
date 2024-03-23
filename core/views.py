from django.shortcuts import render

def index(request):
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Angélica linda, amor da minha vida. não vamos na cacau show de campos do jodão'
    }
    return render(request,'index.html', context)

def contato(request):
    return render(request,"contato.html")