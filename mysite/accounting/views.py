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
from django.urls import reverse_lazy
from django.db.models import Q
import datetime
from mailer.views import sendMail
from exam_certification.models import (CertificateAttendance,ExamMaterialL3,ExamMaterialPAUTL2,ExamMaterialTOFDModel1,
                                       PcnCertificateAttendance,CSWIPCertificateAttendance,PcnCertificateProduct,
                                       CswipCertificateProduct,ExamMaterialPiWiModel,ExamResultPautL2,ExamMaterialTofdL3,
                                       CSWIPWeldingInspector3_1ExamMaterial,CSWIPWeldingInspector3_1Result,Samples,
                                       CSWIPWeldingInspector3_1ResultIntermadiate,CSWIPWeldingInspector3_2_1ExamMaterial,
                                       CSWIPWeldingInspector3_2_1_Result,CSWIPWeldingInspector3_2_2ExamMaterial,
                                       CSWIPWeldingInspector3_2_2_Result,BGAS_CSWIP_PaintingInspectorMaterial,
                                       BGAS_CSWIP_PaintingInspectorResult,ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP,
                                       Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP,ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN,
                                       Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN,PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial,
                                       PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult,PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material,
                                       PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result,TimeFlightDiffractionTOFDLevel3_CSWIP_Material2,
                                       TimeFlightDiffractionTOFDLevel3_CSWIP_Result,TimeFlightDiffractionTOFDLevel3_PCN_Material2,
                                       TimeFlightDiffractionTOFDLevel3_PCN_Result3,RadiographicInterpretationWeldsRIMaterial
                                       ,RadiographicInterpretationWeldsRIResult,DigitalRadiographicInterpretationDRI_Level2_Material3,
                                       DigitalRadiographicInterpretationDRI_Level2_Result,ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN,
                                       Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN,ExamMaterialTOFD_CSWIP )

# Create your views here.

class LoginView(TemplateView):

    template_name = "login.html"

    def get(self,request):
        context = super(LoginView, self).get_context_data()
        if self.request.user.is_authenticated:
            print("Logged in")
            candidate = TesCandidate.objects.filter(user=self.request.user).first()
            group_name = request.user.groups.values_list('name', flat=True).first()
            print(group_name)

            if group_name == 'management':
                return HttpResponseRedirect(reverse_lazy('training:trainpanel_'))
            elif group_name == 'training_admin':
                return HttpResponseRedirect(reverse_lazy('training:trainpanel_'))
            elif group_name == 'Staff':

                # return redirect('accounting:staffprofile_', id=self.request.user.id)
                # return HttpResponseRedirect(reverse_lazy('training:trainpanel_',id=candidate.id))
                return redirect('training:trainpanel_', id=candidate.id)
            elif group_name == 'training_operator':
                # candidate = TesCandidate.objects.filter(user=self.request.user).first()
                print("Here now today zanjan 33")
                # print(candidate.id)
                # return HttpResponseRedirect(reverse_lazy('accounting:staffprofile_', id=candidate.id))
                return redirect('accounting:staffprofile_', id=candidate.id)

            elif group_name == 'candidates':
                print('can here 1')
                redirect_to = request.META.get('HTTP_REFERER')
                print(redirect_to)
                if 'next' in redirect_to:
                    print("exist")
                    return redirect(redirect_to.replace('?next=/', ''))
                else:
                    candidate = TesCandidate.objects.filter(user=self.request.user).first()
                    response = redirect('accounting:canprofile_', id=candidate.id)
                    return response

        # return context
        return render(request, "login.html")

    def post(self, request):
        context = super(LoginView, self).get_context_data()
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST['remember_me']
        user = authenticate(username=username, password=password)


        if user is not None:
            if user.is_active:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                group_name = request.user.groups.values_list('name', flat=True).first()
                print(group_name)
                print("Here now today zanjan 1")
                if group_name == 'management' :

                    return redirect('training:trainpanel_')
                elif group_name == 'training_admin':
                    return redirect('training:trainpanel_')
                elif group_name == 'Staff':
                    candidate = TesCandidate.objects.filter(user=user).first()
                    return redirect('accounting:staffprofile_',id=request.user.id)

                elif group_name == 'training_operator':
                    candidate = TesCandidate.objects.filter(user=user).first()
                    return redirect('accounting:staffprofile_',id=request.user.id)
                elif group_name == 'candidates':



                    redirect_to = request.META.get('HTTP_REFERER')
                    print(redirect_to)
                    if 'next' in redirect_to:
                        print("exist")
                        return redirect(redirect_to.replace('?next=/',''))
                    else:
                        print("Here main")
                        print(request.user)
                        candidate = TesCandidate.objects.filter(user=request.user).first()
                        response = redirect('accounting:canprofile_' , id=candidate.id)
                        return response
                    # response.set_cookie('tesUser', candidate.id, max_age=1000)
                    # response.set_cookie('userName', candidate.first_name, max_age=1000)



            else:
                return render(request, "index.html", {'msg': 'Your username or password is wrong!'})
        else:
            return render(request, 'login.html', {'msg': 'Wrong username or password!'})
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
                print("Here now today zanjan 2")
                if group_name == 'super_admin':

                    return redirect('adminpanel:adpanel_')
                elif group_name == 'training_admin':
                    return redirect('training:trainpanel_')
                elif group_name == 'Staff':
                    return redirect('accounting:staffprofile_', id=request.user.id)
                elif group_name == 'candidates':

                    print('can Here')
                    candidate = TesCandidate.objects.filter(user=user).first()
                    print(candidate.id)
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
        print(id)
        user = User.objects.filter(id=id).first()
        # staff_profile = StaffProfile.objects.filter(user=user).first()
        # print(user.first_name)
        candidate = TesCandidate.objects.filter(user=user).first()
        # events = Event.objects.filter(candidate=candidate)
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        print('Staff Profile')
        print(candidate.first_name)
        print('Staff Profile')

        now = datetime.datetime.now()
        context['user'] = user
        context['candidate'] = candidate
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            print("Here")
            aboutMe = request.POST['aboutMe']
            print(aboutMe)
            user = User.objects.filter(id = self.kwargs['id']).first()
            profileData = TesCandidate.objects.filter(user = user).first()
            profileData.first_name = request.POST['first_name']
            profileData.middleName = request.POST['middleName']
            profileData.last_name = request.POST['last_name']
            profileData.emergencyContact = request.POST['emergencyContact']
            profileData.email = request.POST['email']
            profileData.address = request.POST['address']
            profileData.contact_number = request.POST['contact_number']
            if not request.POST.get('password', '') == None:
                profileData.password = request.POST['password']

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
            return render(request, "accounts/staff_profile.html", context={'candidate': profileData})
        return render(request, "index.html")

class CandidateProfileView(LoginRequiredMixin,TemplateView):

    template_name = "accounts/profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CandidateProfileView, self).get_context_data()
        print(self.kwargs['id'])
        candidate = TesCandidate.objects.filter(id = self.kwargs['id']).first()
        events = Event.objects.filter(candidate = candidate)
        contact = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False)).order_by("-id")
        contactRead = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False))
        print("Good Day")
        now = datetime.datetime.now()
        group_name = self.request.user.groups.values_list('name', flat=True).first()

        result_list=[]
        result1={}
        result2={}
        result3={}
        result4={}
        result5={}
        result6={}
        result7={}
        result8={}
        result9={}
        result10={}
        result11={}
        result12={}
        result13={}
        result14={}
        result15={}
        result16={}
        result17={}

        cswip31_result = CSWIPWeldingInspector3_1Result.objects.filter(candidate=candidate)
        if cswip31_result.count() >0:
            for item in cswip31_result:
                result1['id'] = item.id
                result1['event'] = item.event
                result1['exam_date'] = item.exam_date
                result1['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result1)

        cswip321_result = CSWIPWeldingInspector3_2_1_Result.objects.filter(candidate=candidate)
        if cswip321_result.count() > 0:
            for item in cswip321_result:
                result2['id'] = item.id
                result2['event'] = item.event
                result2['exam_date'] = item.exam_date
                result2['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result2)


        cswip322_result = CSWIPWeldingInspector3_2_2_Result.objects.filter(candidate=candidate)
        if cswip322_result.count() > 0:
            for item in cswip322_result:
                result3['id'] = item.id
                result3['event'] = item.event
                result3['exam_date'] = item.exam_date
                result3['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result3)

        painting_cswip_result = BGAS_CSWIP_PaintingInspectorResult.objects.filter(candidate=candidate)
        if painting_cswip_result.count() > 0:
            for item in painting_cswip_result:
                result4['id'] = item.id
                result4['event'] = item.event
                result4['exam_date'] = item.exam_date
                result4['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result4)

        paut_l2_cswip_result = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.filter(candidate=candidate)
        if paut_l2_cswip_result.count() > 0:
            for item in paut_l2_cswip_result:
                result5['id'] = item.id
                result5['event'] = item.event
                # result5['exam_date'] = item.exam.exam_date
                # result5['exam_title'] = item.exam.exam_title
                result14['file'] = item.file
                result_list.append(result5)

        paut_l2_pcn_result = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.filter(candidate=candidate)
        if paut_l2_pcn_result.count() > 0:
            for item in paut_l2_pcn_result:
                result6['id'] = item.id
                result6['event'] = item.event
                result6['exam_date'] = item.exam_date
                result6['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result6)

        paut_l3_cswip_result = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult.objects.filter(candidate=candidate)
        if paut_l3_cswip_result.count() > 0:
            for item in paut_l3_cswip_result:
                result7['id'] = item.id
                result7['event'] = item.event
                result7['exam_date'] = item.exam_date
                result7['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result7)


        paut_l3_pcn_result = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result.objects.filter(candidate=candidate)
        if paut_l3_pcn_result.count() > 0:
            for item in paut_l3_pcn_result:
                result8['id'] = item.id
                result8['event'] = item.event
                # result8['exam_date'] = item.exam.exam_date
                # result8['exam_title'] = item.exam.exam_title
                result_list.append(result8)

        tofd_l2_pcn_result = Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.filter(candidate=candidate)
        if tofd_l2_pcn_result.count() > 0:
            for item in tofd_l2_pcn_result:
                result9['id'] = item.id
                result9['event'] = item.event
                result9['exam_date'] = item.exam_date
                result9['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result9)

        tofd_l2_cswip_result = ExamMaterialTOFD_CSWIP.objects.filter(candidate=candidate)
        if tofd_l2_cswip_result.count() > 0:
            for item in tofd_l2_cswip_result:
                result10['id'] = item.id
                result10['event'] = item.event
                result10['exam_date'] = item.exam_date
                result10['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result10)

        tofd_l3_cswip_result = TimeFlightDiffractionTOFDLevel3_CSWIP_Result.objects.filter(candidate=candidate)
        if tofd_l3_cswip_result.count() > 0:
            for item in tofd_l3_cswip_result:
                result11['id'] = item.id
                result11['event'] = item.event
                result11['exam_date'] = item.exam_date
                result11['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result11)


        tofd_l3_pcn_result = TimeFlightDiffractionTOFDLevel3_PCN_Result3.objects.filter(candidate=candidate)
        if tofd_l3_pcn_result.count() > 0:
            for item in tofd_l3_pcn_result:
                result12['id'] = item.id
                result12['event'] = item.event
                result12['exam_date'] = item.exam_date
                result12['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result12)


        ri_result = RadiographicInterpretationWeldsRIResult.objects.filter(candidate=candidate)
        if ri_result.count() > 0:
            for item in ri_result:
                result13['id'] = item.id
                result13['event'] = item.event
                result13['exam_date'] = item.exam_date
                result13['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result13)


        dri_result = DigitalRadiographicInterpretationDRI_Level2_Result.objects.filter(candidate=candidate)
        if dri_result.count() >0:
            for item in dri_result:
                result14['id'] = item.id
                result14['event'] = item.event
                result14['exam_date'] = item.exam_date
                result14['exam_title'] = item.exam_title
                result14['file'] = item.file
                result_list.append(result14)


        cetrificates = CertificateAttendance.objects.all()


        # upcoming_event = Event.objects.filter( start_date__gte > datetime.now()).order_by('start_date')[:5]
        upcoming_event = Event.objects.filter( start_date__gte=datetime.datetime.now()).order_by('start_date')[:5]
        # results = cswip31_materials
        context['cetrificates'] = cetrificates
        context['upcoming_event'] = upcoming_event
        context['result_list'] = result_list
        context['group_name'] = group_name
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
            print(request.POST['contact_number'])
            if not request.POST.get('password', '') == None:
                profileData.password = request.POST['password']

            if not request.POST.get('birthDate', '') == '':
                profileData.birth_date = datetime.datetime.strptime(self.request.POST['birthDate'], '%m/%d/%Y')
            profileData.currentCompany = request.POST['currentCompany']
            profileData.currentPosition = request.POST['currentPosition']
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
            print("Redirect Here! 555fff")
            firstName = request.POST['first_name']
            lastName = request.POST['last_name']
            middleName = request.POST['middleName']
            print(firstName)
            result = TesCandidate.objects.filter(first_name=firstName, last_name=lastName).count()

            # lastCan = TesCandidate.objects.exclude(tes_candidate_id__exact=None).last()
            # print(lastCan)
            # tempID = int(lastCan.tes_candidate_id.split('-')[1]) + 1
            # tempID = 'TESN-0' + str(tempID)
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
            # user.tescandidate.tes_candidate_id = tempID
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

            redirect_to = request.META.get('HTTP_REFERER')
            print(redirect_to)
            if 'next' in redirect_to:
                print("exist")
                login(request, user)
                return redirect(redirect_to.replace('literegister/?next=/', ''))
            else:
                candidate = TesCandidate.objects.filter(user=user).first()
                response = redirect('accounting:canprofile_', id=candidate.id)
                return response
        return redirect('training:resquestsuccess_')


class RegSuccessView(TemplateView):
    template_name = "accounts/success.html"

    def get_context_data(self):
        context = super(RegSuccessView, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context
