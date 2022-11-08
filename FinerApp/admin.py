from django.contrib import admin
from .models import Empresa
from .models import Producto
from .models import Concepto
from .models import Cfu
from .models import Costos
# Register your models here.
admin.site.register(Empresa)
admin.site.register(Producto)
admin.site.register(Concepto)
admin.site.register(Cfu)
admin.site.register(Costos)