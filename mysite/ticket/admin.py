from django.contrib import admin
from ticket.models import Ticket
# Register your models here.
class TicketAdmin(admin.ModelAdmin):


    list_display = ['id','candidate','asignedTo','title','status','department','created_at','updated_at']
    list_filter =  ['id','candidate','asignedTo','title','status','department','created_at','updated_at']

admin.site.register(Ticket,TicketAdmin)
