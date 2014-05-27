from django.contrib import admin
from models import Migrant, AbuseAdmin, CheckPoint


class AbuseAdmin(admin.ModelAdmin):
    list_display = ('type','description','migrante','created')
    #list_filter = ['name',]
    #search_fields = ('pseudo',)

    def get_list_display(self, request):
        display_list = list(super(AbuseAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(AbuseAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None



class MigrantAdmin(admin.ModelAdmin):
    list_display = ('pseudo','country','age','gender','country','martial','created','updated')
    #list_filter = ['name',]
    search_fields = ('pseudo',)

    def get_list_display(self, request):
        display_list = list(super(MigrantAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(MigrantAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None



class CheckPointAdmin(admin.ModelAdmin):
    list_display = ('migrante','lon','lat','other_location','city','state','country','created')
    #list_filter = ['name',]
    search_fields = ('pseudo',)

    def get_list_display(self, request):
        display_list = list(super(CheckPointAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(CheckPointAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None

admin.site.register(Migrant,MigrantAdmin)
admin.site.register(Abuse,AbuseAdmin)
admin.site.register(CheckPoint,CheckPointAdmin)
