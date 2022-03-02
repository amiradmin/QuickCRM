

class SidebarMixin(object):

    def get_context_data(self, **kwargs):
        # Call class's get_context_data method to retrieve context
        context = super().get_context_data(**kwargs)
        adminStatus =False
        for g in self.request.user.groups.all():
            if  g.name == 'management' :
                adminStatus=True
            else:
                adminStatus = False
            if g.name=='training_admin':
                managerStatus = True
            else:
                managerStatus = False

        context['adminStatus'] = adminStatus
        context['managerStatus'] = managerStatus
        return context