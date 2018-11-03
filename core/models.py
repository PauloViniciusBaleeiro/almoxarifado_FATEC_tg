from django.db import models


class Estado(models.Model):
    sigla = models.CharField(max_length=2, primary_key=True)
    descrição = models.CharField(max_length=20)

    def __str__(self):
        return self.sigla


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Fabricante(models.Model):

    CNPJ = models.IntegerField(max_length=14, unique=True)
    nome_fantasia = models.CharField(max_length=20)
    razao_social = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=20, default='rua')
    nome_do_logradouro = models.CharField(max_length=20)
    numero = models.IntegerField(max_length=4)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    cep = models.IntegerField(max_length=9)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_fantasia


class Contato(models.Model):
    telefone = models.IntegerField()
    e_mail = models.EmailField


class Contato_Fabricante(models.Model):
    fabricante = models.OneToOneField(Fabricante, on_delete=models.CASCADE)


class Tipo_de_Material(models.Model):
    descrição = models.CharField(max_length=30)

    def __str__(self):
        return self.descrição


class Material(models.Model):
    nome = models.CharField(max_length=50)
    descrição = models.CharField(max_length=300)
    unidade = models.CharField(max_length=4)
    quantidade = models.FloatField()
    tipo_de_material= models.ForeignKey(Tipo_de_Material, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = "materiais"

    def __str__(self):
        return self.nome



