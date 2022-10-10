from django.contrib import admin
from settings.models import Sidebar,SubMenuLevelOne,SubMenuLevelTwo,SubMenuLevelThree
# Register your models here.
class SidebarAdmin(admin.ModelAdmin):

    list_display = ['id','title','created_at','updated_at']
    list_filter = ['id','title','created_at','updated_at']
admin.site.register(Sidebar,SidebarAdmin)


class SubMenuLevelOneAdmin(admin.ModelAdmin):

    list_display = ['id','title','created_at','updated_at']
    list_filter = ['id','title','created_at','updated_at']
admin.site.register(SubMenuLevelOne,SubMenuLevelOneAdmin)

class SubMenuLevelTwoAdmin(admin.ModelAdmin):

    list_display = ['id','title','created_at','updated_at']
    list_filter = ['id','title','created_at','updated_at']
admin.site.register(SubMenuLevelTwo,SubMenuLevelTwoAdmin)

class SubMenuLevelThreeAdmin(admin.ModelAdmin):

    list_display = ['id','title','created_at','updated_at']
    list_filter = ['id','title','created_at','updated_at']
admin.site.register(SubMenuLevelThree,SubMenuLevelThreeAdmin)
