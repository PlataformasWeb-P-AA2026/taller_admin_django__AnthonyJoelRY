from django.contrib import admin
from institucion.models import Exhibicion, GuiaMuseo, Museo

# Configuración en tabla para Museo
class MuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'anio_fundacion', 'presentacion')
    search_fields = ('nombre', 'ciudad')

    def presentacion(self, obj):
        return obj.presentacion()
    presentacion.short_description = 'Presentación'

# Configuración en tabla para GuiaMuseo
class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'anos_experiencia_guia', 'idiomas_hablados', 'museo')
    search_fields = ('nombre_completo', 'idiomas_hablados')

# Configuración en tabla para Exhibicion
class ExhibicionAdmin(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses', 'costo_produccion', 'tematica', 'guia')
    search_fields = ('titulo_exhibicion', 'tematica')


# Registro de los modelos con sus respectivas clases de administración
admin.site.register(Museo, MuseoAdmin)
admin.site.register(GuiaMuseo, GuiaMuseoAdmin)
admin.site.register(Exhibicion, ExhibicionAdmin)