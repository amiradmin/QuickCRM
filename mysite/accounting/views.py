from training.views import LecturerView
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.conf import settings
from training.models import CandidateProfile, Lecturer,Event,TesCandidate
from django.contrib.auth.hashers import make_password
import datetime
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
                    return redirect('accounting:canprofile_', id =user.id)

            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class LecturerProfileView(TemplateView):

    template_name = "accounts/profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LecturerProfileView, self).get_context_data()
        lecturer = Lecturer.objects.filter(id = self.kwargs['id']).first()
        event = Event.objects.all()
        context['lecturer'] = lecturer
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



    
class CandidateProfileView(TemplateView):

    template_name = "accounts/can_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CandidateProfileView, self).get_context_data()
        print(self.kwargs['id'])
        candidate = CandidateProfile.objects.filter(id = self.kwargs['id']).first()
        context['candidate'] = candidate
        return context


    def post(self, request, *args, **kwargs):
       
        if request.method == 'POST':
            aboutMe =  request.POST['aboutMe']
            print(aboutMe)
            lecturer = CandidateProfile.objects.filter(id = self.kwargs['id']).first()
            lecturer.aboutMe = aboutMe
            lecturer.save()  
            return render(request, "accounts/profile.html",context = {'lecturer':lecturer})
        return render(request, "index.html")


class RegisterView(TemplateView):
    template_name = "accounts/registration.html"

    def get_context_data(self):
        context = super(RegisterView, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context

    def post(self, request, *args, **kwargs):

        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            # print(request.POST['tes_id'])
            firstName = request.POST['first_name']
            lastName = request.POST['last_name']
            print(firstName)
            result = TesCandidate.objects.filter(first_name=firstName, last_name=lastName).count()
            # if result > 0:
            #     print('exist')
            #     response = JsonResponse({"error": "there was an error"})
            #     response.status_code = 403  # To announce that the user isn't allowed to publish
            #
            #     return render(request, 'training/errors.html')
            user = User()

            # user.refresh_from_db()
            user.username = request.POST['email']
            user.password =make_password(request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            # user.tes_candidate_id = request.POST['tesCanID']
            user.tescandidate.first_name = request.POST['first_name']
            user.tescandidate.middleName = request.POST['middleName']
            user.tescandidate.last_name = request.POST['last_name']
            user.tescandidate.birth_date = datetime.datetime.strptime(request.POST['birthDate'], '%m/%d/%Y')
            # user.tescandidate.tes_candidate_id = request.POST['tes_id']
            user.tescandidate.customer_id = request.POST['customer_id']
            user.tescandidate.address = request.POST['address']
            # user.passport_id = request.POST['passport_id']
            user.tescandidate.sponsor_company = request.POST['sponsor_company']
            user.tescandidate.email = request.POST['email']
            user.tescandidate.contact_number = request.POST['phone']
            user.save()
            group = Group.objects.get(name='candidates')
            group.user_set.add(user)
            # user.note = request.POST['note']
            # if request.FILES.get('photo', False):
            #     user.photo = request.FILES['photo']
            # if request.FILES.get('doc_1', False):
            #     user.document_1 = request.FILES['doc_1']
            # if request.FILES.get('doc_2', False):
            #     user.document_2 = request.FILES['doc_2']
            # if request.FILES.get('doc_3', False):
            #     user.document_3 = request.FILES['doc_3']
            # if request.FILES.get('doc_4', False):
            #     user.document_4 = request.FILES['doc_4']
            # if request.FILES.get('doc_5', False):
            #     user.document_5 = request.FILES['doc_5']
            # if request.FILES.get('doc_6', False):
            #     user.document_6 = request.FILES['doc_6']
            # if request.FILES.get('doc_7', False):
            #     user.document_7 = request.FILES['doc_7']
            # if request.FILES.get('doc_8', False):
            #     user.document_8 = request.FILES['doc_8']
            # if request.FILES.get('doc_9', False):
            #     user.document_9 = request.FILES['doc_9']
            # if request.FILES.get('doc_10', False):
            #     user.document_9 = request.FILES['doc_10']
            print("here")
            print(user.username)
            canObj = CandidateProfile()
            canObj.user = user
            canObj.first_name = request.POST['first_name']
            canObj.last_name = request.POST['last_name']
            canObj.save()
            print('End')

        return redirect('forms:twienrolreg_')

class RegSuccessView(TemplateView):
    template_name = "accounts/success.html"

    def get_context_data(self):
        context = super(RegSuccessView, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context