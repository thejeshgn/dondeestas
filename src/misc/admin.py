from django.contrib import admin
from models import Migrant





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


admin.site.register(Migrant,MigrantAdmin)
