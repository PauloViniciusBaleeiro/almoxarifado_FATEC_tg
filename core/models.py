from django.db import models


class Estado(models.Model):
    sigla = models.CharField(max_length=2, primary_key=True)
    descricao = models.CharField(max_length=20, verbose_name='descrição', null=True)

    def __str__(self):
        return self.sigla


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome + '/' + str(self.estado)


class Fabricante(models.Model):

    CNPJ = models.CharField(max_length=20, blank=False, null=False, unique=True)
    nome_fantasia = models.CharField(max_length=20, verbose_name='nome fantasia')
    razao_social = models.CharField(max_length=20, verbose_name='razão social')
    logradouro = models.CharField(max_length=20, default='rua')
    nome_do_logradouro = models.CharField(max_length=20, verbose_name='nome do logradouro')
    numero = models.IntegerField(verbose_name='número', blank=True)
    complemento = models.CharField(max_length=20, blank=True)
    bairro = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)
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
    descricao = models.CharField(max_length=30, verbose_name='descrição', null=True)

    class Meta:
        verbose_name = 'tipo de material'
        verbose_name_plural = 'tipos de materiais'

    def __str__(self):
        return self.descricao


class Material(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=300, verbose_name='descrição', null=True)
    unidade = models.CharField(max_length=4)
    quantidade = models.FloatField()
    tipo_de_material= models.ForeignKey(TipodeMaterial, on_delete=models.CASCADE, verbose_name='tipo do material')

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = "materiais"

    def __str__(self):
        return self.nome


class EntradaDeMaterial(models.Model):
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    lote = models.CharField(max_length=30)
    nota_fiscal = models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota Fiscal')
    data_de_fabricacao = models.DateField(blank=True, null=True, verbose_name='Data de Fabricação')
    data_de_validade = models.DateField(blank=True, null=True, verbose_name='Data de Validade')
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'entrada de material'
        verbose_name_plural = 'entrada de materiais'
        unique_together = ['material', 'lote']