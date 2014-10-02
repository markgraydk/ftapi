from django.db import models

# Create your models here.

class aktor(models.Model):
    id = models.AutoField(primary_key=True)
    aktorid = models.IntegerField(null=True, blank=True)
    typeid = models.IntegerField(null=True, blank=True)
    gruppenavnkort = models.CharField(max_length=200, null=True, blank=True)
    navn = models.CharField(max_length=200, null=True, blank=True)
    fornavn = models.CharField(max_length=200, null=True, blank=True)
    efternavn = models.CharField(max_length=200, null=True, blank=True)
    biografi = models.TextField(null=True, blank=True)
    opdateringsdato = models.DateTimeField(null=True, blank=True)
    periodeid = models.IntegerField(null=True, blank=True)
    startdato = models.DateTimeField(null=True, blank=True)
    slutdato = models.DateTimeField(null=True, blank=True)
    
    

class aktoraktor(models.Model):
    id = models.AutoField(primary_key=True)
    aktoraktorid = models.IntegerField(null=True, blank=True)
    fraaktorid = models.IntegerField(null=True, blank=True)
    tilaktorid = models.IntegerField(null=True, blank=True)
    startdato = models.DateTimeField(null=True, blank=True)
    slutdato = models.DateTimeField(null=True, blank=True)
    rolleid = models.IntegerField(null=True, blank=True)
    


class aktoraktorrolle(models.Model):
    
    id = models.AutoField(primary_key=True)
    aktoraktorrolleid = models.IntegerField(null=True, blank=True)
    rolle = models.CharField(max_length=200, null=True, blank=True)
    opdateringsdato = models.DateTimeField(null=True, blank=True)



class aktortype(models.Model):
    
    id = models.AutoField(primary_key=True)
    aktortypeid = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    opdateringsdato = models.DateTimeField(null=True, blank=True)

