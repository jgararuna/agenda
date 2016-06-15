from django.db import models

class Contato(models.Model):
	
	SEXO_CHOICES = {

		(u'masculino', u'Masculino'),
		(u'feminino', u'Feminino'),

	}

	ESTADO_CIVIL_CHOICES = {

		(u'solteiro(a)', u'Solteiro(a)'),
		(u'casado(a)', u'Casado(a)'),
		(u'divorciado(a)', u'Divorciado(a)'),
		(u'viuvo(a)', u'Viuvo(a)'),
		
	}

	contato_id = models.AutoField(primary_key=True)
	contato_nome = models.CharField(max_length=50)
	contato_nascimento = models.DateField()
	contato_sexo = models.CharField(max_length=50, choices=SEXO_CHOICES)
	contato_estado_civil = models. CharField(max_length=50, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado Civil')
	contato_email = models.CharField(max_length=50)
	contato_favorito = models.BooleanField(verbose_name='Favorito')