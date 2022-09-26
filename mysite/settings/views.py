from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User,Group
# Create your views here.


# class UserStatistics(LoginRequiredMixin, TemplateView):
#     template_name = "monitoring/user_statistics.html"
#
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(UserStatistics, self).get_context_data()
#
#         # context['last_user_list'] = last_user_list
#         return context

class SidebarView(TemplateView):
    template_name = "sidebar.html"
    # add models, authentication, whatever

    def get_context_data(self, **kwargs):
        # handle the context data
        return context
