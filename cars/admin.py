from django.contrib import admin
from cars.models import Car, Brand
 
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "factory_year","model_year", "value") # exibe o que vai aparecer na tabela como titulo
    search_fields = ("model", "brand") #cria oque vai ser usado como nome chave para busca. 
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin )
