from django.shortcuts import render
from django.http import HttpResponse
from .forms import Hospitalforms
from .models import Hospital

# Create your views here.

def index(request):
    return render(request, 'hospitais/index.html')

def hospital(request):
    hospitais = Hospital.objects.all()
    busca = request.GET.get('search')
    if busca:
        hospitais = Hospital.objects.filter(nome_hospital__icontains=busca)
    return render(request, 'hospitais/hospitais.html', {'hospitais':hospitais})

def editar(request, id):
    hosp = get_object_or_404(Hospital,pk=id)
    form = Hospitalforms(intance=hosp)
    if request.method == "POST":
        form = Hospitalforms(intance=hosp)
        if form.is_valid():
            form.save()
            return redirect('hospital')

        else:
            return render(request, 'hospitais/editar_hospitais.html',{'forms':forms, 'hosp':hosp})
    
    else:
        return render(request, 'hospitais/editar_hospitais.html',{'forms':forms, 'hosp':hosp})

def deletar(request, id):
    hosp = get_object_or_404(Hospital, pk=id)
    if request.method == "POST":
        hosp.delete()
        return redirect('hospitais')
    
    return render(request, 'hospitais/deletar_hospital.html', {'hosp':hosp})

def criar_hospital(request):
    form = Hospitalforms(request.POST)
    if request.method == "POST":
        form = Hospitalforms(request.POST, request.FILES)
        if form.is_valid():
            hosp = form.save()
            hosp.save()
            form = Hospitalforms
    
    return render(request,'hospitais/criar_hospitais.html',{'forms':form})