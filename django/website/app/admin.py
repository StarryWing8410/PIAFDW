from django.contrib import admin
from .models import Estanteria, Caja, Locker, Mueble

# Register your models here.
admin.site.register(Estanteria)
admin.site.register(Caja)
admin.site.register(Locker)
admin.site.register(Mueble)
