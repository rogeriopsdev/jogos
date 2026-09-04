from django import forms
from jogoapp.models import *

class ServidorForm(forms.ModelForm):
    class Meta:
        model =Servidor
        fields = '__all__'

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'

class NivelForm(forms.ModelForm):
    class Meta:
        model = Nivel
        fields = '__all__'

class FaseForm(forms.ModelForm):
    class Meta:
        model = Fase
        fields = '__all__'

class CriadorForm(forms.ModelForm):
    class Meta:
        model = Criador
        fields = '__all__'

class PersonagemForm(forms.ModelForm):
    class Meta:
        model =Personagem
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model =Usuario
        fields = '__all__'

class JogoForm(forms.ModelForm):
    class Meta:
        model =Jogo
        fields = '__all__'