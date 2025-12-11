from django.db import models

# Create your models here.
class Cliente:
 def __init__(self, nome, telefone, email):
   self.nome = nome
   self.telefone = telefone
   self.email = email
