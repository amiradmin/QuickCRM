from training.views import LecturerView
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings
from training.models import CandidateProfile, Lecturer,Event,TesCandidate
from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin
from contacts.models import Contact
from training.models import TesCandidate,StaffProfile,CourseRequest
from django.db.models import Q
import datetime
from mailer.views import sendMail

# Create your views here.

class LoginView(TemplateView):

    template_name = "login.html"

    def get_context_data(self):
        context = super(LoginView, self).get_context_data()

        return context

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        # remember = request.POST['remember_me']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                group_name = request.user.groups.values_list('name', flat=True).first()
                print(group_name)
                if group_name == 'management' :
                    
                    return redirect('training:trainpanel_')
                elif group_name == 'training_admin':
                    return redirect('training:trainpanel_')
                elif group_name == 'Staff':

                    return redirect('accounting:staffprofile_',id=request.user.id)
                elif group_name == 'candidates':

                    print('can')
                    candidate = TesCandidate.objects.filter(user=user).first()
                    response = redirect('accounting:canprofile' , i=candidate.id)
                    response.set_cookie('tesUser', candidate.id, max_age=1000)
                    response.set_cookie('userName', candidate.first_name, max_age=1000)

                    return response

            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")


class CandidateLoginView(TemplateView):
    template_name = "candidate_login.html"

    def get_context_data(self):
        context = super(CandidateLoginView, self).get_context_data()

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
                if group_name == 'super_admin':

                    return redirect('adminpanel:adpanel_')
                elif group_name == 'training_admin':
                    return redirect('training:trainpanel_')
                elif group_name == 'Staff':
                    return redirect('accounting:staffprofile_', id=request.user.id)
                elif group_name == 'candidates':

                    print('can')
                    candidate = TesCandidate.objects.filter(user=user).first()
                    return redirect('accounting:canprofile_', id=candidate.id)

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


class StaffProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/staff_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(StaffProfileView, self).get_context_data()
        id = self.kwargs['id']
        user = User.objects.filter(id=id).first()
        staff_profile = StaffProfile.objects.filter(user=user).first()
        print(user.first_name)
        # candidate = TesCandidate.objects.filter(id=self.kwargs['id']).first()
        # events = Event.objects.filter(candidate=candidate)
        # contact = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False)).order_by("-id")
        # contactRead = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False))
        print('Staff Profile')
        now = datetime.datetime.now()
        context['user'] = user
        context['staff_profile'] = staff_profile
        # context['events'] = events
        # context['now'] = now
        # context['contact'] = contact
        # context['contactRead'] = contactRead
        return context

    
class CandidateProfileView(LoginRequiredMixin,TemplateView):

    template_name = "accounts/profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CandidateProfileView, self).get_context_data()
        print(self.kwargs['id'])
        candidate = TesCandidate.objects.filter(id = self.kwargs['id']).first()
        events = Event.objects.filter(candidate = candidate)
        contact = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False)).order_by("-id")
        contactRead = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False))
        print(contactRead)
        now = datetime.datetime.now()
        context['candidate'] = candidate
        context['events'] = events
        context['now'] = now
        context['contact'] = contact
        if contact.count() > 0:
            context['newMessage'] = True
        else:
            context['newMessage'] = False
        context['contactRead'] = contactRead
        return context


    def post(self, request, *args, **kwargs):
       
        if request.method == 'POST':
            print("Here")
            aboutMe =  request.POST['aboutMe']
            print(aboutMe)
            profileData = TesCandidate.objects.filter(id = self.kwargs['id']).first()
            profileData.first_name = request.POST['first_name']
            profileData.middleName = request.POST['middleName']
            profileData.last_name = request.POST['last_name']
            profileData.emergencyContact = request.POST['emergencyContact']
            profileData.email = request.POST['email']
            profileData.address = request.POST['address']
            profileData.contact_number = request.POST['contact_number']
            if not request.POST.get('password', '') == None:
                profileData.password = request.POST['password']
            profileData.currentCompany = request.POST['currentCompany']
            profileData.website = request.POST['website']
            profileData.facebook = request.POST['facebook']
            profileData.twitter = request.POST['twitter']
            profileData.skype = request.POST['skype']
            profileData.linkedin = request.POST['linkedin']
            profileData.instagram = request.POST['instagram']
            profileData.aboutMe = aboutMe
            if request.FILES.get('photo', False):
                profileData.photo = request.FILES['photo']
            if request.FILES.get('doc_1', False):
                profileData.document_1 = request.FILES['doc_1']
            if request.FILES.get('doc_2', False):
                profileData.document_2 = request.FILES['doc_2']
            profileData.save()
            return render(request, "accounts/profile.html",context = {'candidate':profileData})
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
            lastCan = TesCandidate.objects.last()
            print(lastCan)
            tempID = int(lastCan.tes_candidate_id.split('-')[1]) + 1
            tempID = 'TESN-0' + str(tempID)
            user = User()

            # user.refresh_from_db()
            user.username = request.POST['email']
            user.password =make_password(request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            group = Group.objects.filter(id=1).first()
            user.groups.add(group)
            # user.tes_candidate_id = request.POST['tesCanID']
            user.tescandidate.first_name = request.POST['first_name']
            user.tescandidate.middleName = request.POST['middleName']
            user.tescandidate.last_name = request.POST['last_name']
            user.tescandidate.birth_date = datetime.datetime.strptime(request.POST['birthDate'], '%m/%d/%Y')
            user.tescandidate.tes_candidate_id = tempID
            # user.tescandidate.customer_id = request.POST['customer_id']
            user.tescandidate.address = request.POST['address']
            # user.passport_id = request.POST['passport_id']

            user.tescandidate.emergencyContact = request.POST['emergencyContact']
            user.tescandidate.email = request.POST['email']
            user.tescandidate.contact_number = request.POST['phone']
            user.save()
            # group = Group.objects.get(name='candidates')
            # group.user_set.add(user)

            #     user.document_9 = request.FILES['doc_10']

            print(user.username)
            canObj = CandidateProfile()
            canObj.user = user
            canObj.first_name = request.POST['first_name']
            canObj.last_name = request.POST['last_name']
            if request.FILES.get('photo', False):
                canObj.photo = request.FILES['photo']
            if request.FILES.get('doc_1', False):
                canObj.document_1 = request.FILES['doc_1']
            if request.FILES.get('doc_2', False):
                canObj.document_2 = request.FILES['doc_2']
            canObj.save()
            print('End')

            fullName = canObj.first_name + ' ' + canObj.last_name
            msg = 'Your account has been created successfully'
            sendMail(request.POST['email'],fullName,msg)
            print('Mail Sent')

        return redirect('accounting:canprofile_',id=user.tescandidate.id)



class LitteRegisterView(TemplateView):
    template_name = "accounts/lite_reg.html"

    def get_context_data(self):
        context = super(LitteRegisterView, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form

        return context

    def post(self, request, *args, **kwargs):

        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            # print(request.POST['tes_id'])
            firstName = request.POST['first_name']
            lastName = request.POST['last_name']
            middleName = request.POST['middleName']
            print(firstName)
            result = TesCandidate.objects.filter(first_name=firstName, last_name=lastName).count()

            lastCan = TesCandidate.objects.exclude(tes_candidate_id__exact=None).last()
            print(lastCan)
            tempID = int(lastCan.tes_candidate_id.split('-')[1]) + 1
            tempID = 'TESN-0' + str(tempID)
            user = User()

            user.username = request.POST['email']
            user.password =make_password(request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            group = Group.objects.filter(id=3).first()
            user.groups.add(group)
            # user.tes_candidate_id = request.POST['tesCanID']
            user.tescandidate.first_name = request.POST['first_name']
            user.tescandidate.middleName = request.POST['middleName']
            user.tescandidate.last_name = request.POST['last_name']
            user.tescandidate.email = request.POST['email']
            user.tescandidate.tes_candidate_id = tempID
            user.tescandidate.contact_number = request.POST['contactNumber']
            user.save()

            requestObj = CourseRequest()
            requestObj.candidate = user.tescandidate
            requestObj.request = request.POST['message']
            # requestObj.save()
            print(user.username)

            fullName = user.tescandidate.first_name + ' ' + user.tescandidate.last_name
            msg = 'Your account has been created successfully'
            # sendMail(request.POST['email'],fullName,msg)
            # print('Mail Sent')
            print("Redirect Here! 555fff")
            candidate = TesCandidate.objects.filter(user=user).first()
            return redirect('accounting:canprofile' , i=candidate.id)
        return redirect('training:resquestsuccess_')


class RegSuccessView(TemplateView):
    template_name = "accounts/success.html"

    def get_context_data(self):
        context = super(RegSuccessView, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context