from django.db import models
from django.db.models import Max, Sum

# Create your models here.

class Museo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()

    def costo_total_produccion(self):
        total = Exhibicion.objects.filter(guia__museo=self).aggregate(total=Sum('costo_produccion'))['total']
        return total or 0

    def guia_mas_experiencia(self):
        max_exp = self.guias.aggregate(max_exp=Max('anos_experiencia_guia'))['max_exp']
        if max_exp is None:
            return ''
        nombres = self.guias.filter(anos_experiencia_guia=max_exp).values_list('nombre_completo', flat=True)
        return ', '.join(nombres)

    def __str__(self):
        return "%s (%s) - Costo total producción: %s - Guía(s) con más experiencia: %s" % (
            self.nombre,
            self.ciudad,
            self.costo_total_produccion(),
            self.guia_mas_experiencia(),
        )

class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=150)
    anos_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=200)
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="guias")

    def __str__(self):
        return "%s - %s años" % (self.nombre_completo, self.anos_experiencia_guia)


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=200)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=12, decimal_places=2)
    tematica = models.CharField(max_length=200)
    guia = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE, related_name="exhibiciones")

    def __str__(self):
        return "%s - %s" % (self.titulo_exhibicion, self.tematica)
