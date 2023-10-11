from django.db import models

class Tarefa(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    # idade = models.IntegerField()
    tarefa = models.TextField(max_length=255)
