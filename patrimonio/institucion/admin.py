from django.contrib import admin

from institucion.models import Exhibicion, GuiaMuseo, Museo

# Register your models here.
admin.site.register(Museo)
admin.site.register(GuiaMuseo)
admin.site.register(Exhibicion)