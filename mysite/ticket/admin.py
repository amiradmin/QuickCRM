from django.contrib import admin
from ticket.models import Ticket,TicketAnswer
# Register your models here.
class TicketAnswerAdmin(admin.ModelAdmin):
    list_display = ['id','title','status','department','created_at','updated_at']
    list_filter =  ['id','title','status','department','created_at','updated_at']

admin.site.register(TicketAnswer,TicketAnswerAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id','TicketNumber','candidate','asignedTo','title','status','department','created_at','updated_at']
    list_filter =  ['id','candidate','asignedTo','title','status','department','created_at','updated_at']

admin.site.register(Ticket,TicketAdmin)
