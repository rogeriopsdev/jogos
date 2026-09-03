from django.db import models

# Create your models here.
class Servidor(models.Model):
    id_servidor = models.AutoField(primary_key=True)
    nome_servidor =models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.nome_servidor
    

class Plataforma(models.Model):
    id_plataforma = models.AutoField(primary_key=True)
    nome_plataforma = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.nome_plataforma
    
class Nivel(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    nome_nivel = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.nome_nivel
    
class Fase(models.Model):
    id_fase = models.AutoField(primary_key=True)
    nome_fase = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.nome_fase
    
class Criador(models.Model):
    id_criador = models.AutoField(primary_key=True)
    nome_criador = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.nome_criador


class Personagem(models.Model):
    id_personagem = models.AutoField(primary_key=True)
    nome_personagem = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.nome_personagem
    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.nome_usuario
    
    

        
    
class Jogo(models.Model):
    id_jogo = models.AutoField(primary_key=True)
    nome_jogo = models.CharField(max_length=200, null=False)
    id_criador = models.ForeignKey(Criador,models.DO_NOTHING, db_column="id_criador",blank=True ,null=True )
    
    def __str__(self):
        return self.nome_jogo
    

class Servidor_jogo(models.Model):
    id_servidor_jogo = models.AutoField(primary_key=True)
    id_jogo = models.ForeignKey(Jogo, models.DO_NOTHING, db_column="id_jogo", blank=True, null=True)
    id_servidor = models.ForeignKey(Servidor, models.DO_NOTHING, db_column="id_servidor", blank=True, null=True)    
    
    
    def __int__(self):
        return self.id_servidor_jogo
    

class Plataforma_jogo(models.Model):
    id_plataforma_jogo = models.AutoField(primary_key=True)
    id_jogo = models.ForeignKey(Jogo, models.DO_NOTHING, db_column="id_jogo", blank=True, null=True)
    id_plataforma = models.ForeignKey(Plataforma, models.DO_NOTHING, db_column="id_plataforma", blank=True, null=True) 
    
    def __int__(self):
        return self.id_plataforma_jogo
    


class Nivel_jogo(models.Model):
    id_nivel_jogo =models.AutoField(primary_key=True)
    id_jogo = models.ForeignKey(Jogo, models.DO_NOTHING, db_column="id_jogo", blank=True, null=True)
    id_nivel= models.ForeignKey(Nivel, models.DO_NOTHING, db_column="id_nivel", blank=True, null=True) 
        
    def __int__(self):
        return self.id_nivel_jogo
    
class Usuario_jogo(models.Model):
    id_usuario_jogo = models.AutoField(primary_key=True)
    id_jogo = models.ForeignKey(Jogo, models.DO_NOTHING, db_column="id_jogo", blank=True, null=True)
    id_usuario= models.ForeignKey(Usuario, models.DO_NOTHING, db_column="id_usuario", blank=True, null=True) 
    
    def __int__(self):
        return self.id_usuario_jogo