from django.shortcuts import render
from jogoapp.forms import *


# Create your views here.
def index(request):
    jogos = Jogo.objects.all()
    form = JogoForm(request.POST)
    if request.method == "POST":
        form = JogoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = JogoForm()
    context = {'form':form ,'jogos':jogos}
    return render(request, 'jogo/index.html',context)