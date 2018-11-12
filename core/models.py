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
        return self.nome + '/' + str(self.estado)


class Fabricante(models.Model):

    CNPJ = models.CharField(max_length=20, blank=False, null=False, unique=True)
    nome_fantasia = models.CharField(max_length=20, verbose_name='nome fantasia')
    razao_social = models.CharField(max_length=20, verbose_name='razão social')
    logradouro = models.CharField(max_length=20, default='rua')
    nome_do_logradouro = models.CharField(max_length=20, verbose_name='nome')
    numero = models.IntegerField(verbose_name='número', blank=True)
    complemento = models.CharField(max_length=20, blank=True)
    bairro = models.CharField(max_length=20)
    cep = models.IntegerField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_fantasia


class Contato(models.Model):
    telefone = models.CharField(max_length=10, blank=True, null=True)
    e_mail = models.EmailField(blank=True, null=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ['telefone', 'e_mail', 'fabricante']


class TipodeMaterial(models.Model):
    descrição = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'tipo de material'
        verbose_name_plural = 'tipos de materiais'

    def __str__(self):
        return self.descrição


class Material(models.Model):
    nome = models.CharField(max_length=50)
    descrição = models.CharField(max_length=300)
    unidade = models.CharField(max_length=4)
    quantidade = models.FloatField()
    tipo_de_material= models.ForeignKey(TipodeMaterial, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = "materiais"

    def __str__(self):
        return self.nome



