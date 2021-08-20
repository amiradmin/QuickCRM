

class SidebarMixin(object):

    def get_context_data(self, **kwargs):
        # Call class's get_context_data method to retrieve context
        context = super().get_context_data(**kwargs)

        adminStatus =False
        for g in self.request.user.groups.all():
            if  g.name == 'super_admin' or g.name=='training_admin':
                adminStatus=True
                
        context['adminStatus'] = adminStatus
        return context