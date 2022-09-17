from django.contrib import admin
from .models import EMPRESA
from .models import TIPO_EMPRESA
from .models import PRODUCTO
from .models import COSTO_VARIABLE
# Register your models here.
admin.site.register(EMPRESA)
admin.site.register(TIPO_EMPRESA)
admin.site.register(PRODUCTO)
admin.site.register(COSTO_VARIABLE)