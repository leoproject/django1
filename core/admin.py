from django.contrib import admin

from .models import Product, Client

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','email')


admin.site.register(Product, ProdutoAdmin)
admin.site.register(Client,ClientAdmin)
