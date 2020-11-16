from django.contrib import admin

# Register your models here.
from cobro.models import Origen
from cobro.models import Pago
from cobro.models import Fecha


admin.site.register(Origen)

admin.site.register(Pago)

admin.site.register(Fecha)