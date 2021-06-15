from training.views import LecturerView
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.conf import settings
from training.models import Lecturer,Event
# Create your views here.

class LoginView(TemplateView):

    template_name = "login.html"

    def get_context_data(self):
        context = super(LoginView, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                group_name = request.user.groups.values_list('name', flat=True).first()
                print(group_name)
                if group_name == 'super_admin' :
                    
                    return redirect('adminpanel:adpanel_')
                elif group_name == 'training_admin':
                    return redirect('training:trainpanel_')
                elif group_name == 'candidates':

                    print('can')
                    return redirect('training:canprofile_')

            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return HttpResponseRedirect(settings.LOGIN_URL)


class ProfileView(TemplateView):

    template_name = "accounts/profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data()
        lecturer = Lecturer.objects.filter(id = self.kwargs['id']).first()
        event = Event.objects.all()
        context['lecturer'] = lecturer
        context['event'] = event
        return context


    def post(self, request, *args, **kwargs):
        


        if request.method == 'POST':
            aboutMe =  request.POST['aboutMe']
            print(aboutMe)
            lecturer = Lecturer.objects.filter(id = self.kwargs['id']).first()
            lecturer.aboutMe = aboutMe
            lecturer.save()  
            return render(request, "accounts/profile.html",context = {'lecturer':lecturer})
        return render(request, "index.html")