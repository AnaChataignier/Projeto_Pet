from django.contrib import admin

from galeria.models import Pet

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "raca", "cor", "idade", "categoria", "publicada")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Pet, ListandoFotografias)
