from django.shortcuts import render
from jogoapp.forms import *


# Create your views here.
def index(request):
    form = JogoForm(request.POST)
    if request.method == "POST":
        form = JogoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = JogoForm()
    context = {'form':form}
    return render(request, 'jogo/index.html',context)