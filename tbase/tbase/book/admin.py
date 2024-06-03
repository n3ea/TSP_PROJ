
#tbase/tbase/book/admin.py
from django.contrib import admin
from .models import Room_Info, Serv_Info, Prebook, Clients

admin.site.register(Room_Info)
admin.site.register(Serv_Info)
admin.site.register(Clients)
class PrebookAdmin(admin.ModelAdmin):
    list_display = ('id_req', 'id_c', 'b_start', 'b_end', 'stat')
admin.site.register(Prebook, PrebookAdmin)

# Register your models here.
