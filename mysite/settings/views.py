from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User,Group
from settings.models import Sidebar
# Create your views here.


# def top_nav(request):
#     this_user_person = Sidebar.objects.all()
#     context = { 'this_user_person': this_user_person}
#     return render(request, 'sidebar.html', context)
#
# class SidebarView(TemplateView):
#     template_name = "sidebar.html"
#     # add models, authentication, whatever
#
#     def get_context_data(self,*args,**kwargs):
#         context = super(SidebarView, self).get_context_data()
#         print("Sidebar")
#         main_menu = Sidebar.objects.all()
#         context['main_menu'] = main_menu
#         print(main_menu)
#
#
#
#         return context
