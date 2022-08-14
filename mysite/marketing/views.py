from django.shortcuts import render, redirect
from authorization.sidebarmixin import SidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from forms.models import CandidateForms
from training.models import TesCandidate
from django.contrib.auth.models import User, Group
from braces.views import GroupRequiredMixin
from dotenv import load_dotenv
import os
import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
from exam_certification.models import CertificateAttendance,PcnCertificateProduct
import datetime
from dateutil.relativedelta import relativedelta
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



class NotificationView(GroupRequiredMixin,SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "marketing/Notification_list.html"
    group_required = [u'management', u'admin', u'training_admin', u'training_operator']

    def get_context_data(self):
        context = super(NotificationView, self).get_context_data()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()

        result_list = []

        cswip31_result = CSWIPWeldingInspector3_1Result.objects.all()
        if cswip31_result.count() > 0:
            for item in cswip31_result:
                result1 = {}
                result1['id'] = item.id
                result1['class'] = item.__class__.__name__
                result1['event'] = item.event
                result1['candidate'] = item.candidate
                result1['exam_date'] = item.exam.exam_date
                result1['exam_title'] = item.exam.exam_title
                result1['file'] = item.file
                result1['overall'] = item.overall
                result_list.append(result1)

        cswip321_result = CSWIPWeldingInspector3_2_1_Result.objects.all()
        if cswip321_result.count() > 0:
            for item in cswip321_result:
                result2 = {}
                result2['id'] = item.id
                result2['class'] = item.__class__.__name__
                result2['event'] = item.event
                result2['candidate'] = item.candidate
                result2['exam_date'] = item.exam_date
                result2['exam_title'] = item.exam_title
                result2['file'] = item.file
                result2['overall'] = item.overall
                result_list.append(result2)

        cswip322_result = CSWIPWeldingInspector3_2_2_Result.objects.all()
        if cswip322_result.count() > 0:
            for item in cswip322_result:
                result3 = {}
                result3['id'] = item.id
                result3['class'] = item.__class__.__name__
                result3['event'] = item.event
                result3['candidate'] = item.candidate
                result3['exam_date'] = item.exam_date
                result3['exam_title'] = item.exam_title
                result3['file'] = item.file
                result3['overall'] = item.overall
                result_list.append(result3)

        painting_cswip_result = BGAS_CSWIP_PaintingInspectorResult.objects.all()
        if painting_cswip_result.count() > 0:
            for item in painting_cswip_result:
                result4 = {}
                result4['id'] = item.id
                result4['class'] = item.__class__.__name__
                result4['event'] = item.event
                result4['candidate'] = item.candidate
                result4['exam_date'] = item.exam_date
                result4['exam_title'] = item.exam_title
                result4['file'] = item.file
                result4['overall'] = item.overall
                result_list.append(result4)

        paut_l2_cswip_result = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.all()
        if paut_l2_cswip_result.count() > 0:
            for item in paut_l2_cswip_result:
                result5 = {}
                result5['id'] = item.id
                result5['class'] = item.__class__.__name__
                result5['event'] = item.event
                result5['candidate'] = item.candidate
                result5['exam_date'] = item.exam_date
                result5['exam_title'] = item.exam_title
                result5['file'] = item.file
                result5['overall'] = item.overall
                result_list.append(result5)

        paut_l2_pcn_result = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.all()
        if paut_l2_pcn_result.count() > 0:
            for item in paut_l2_pcn_result:
                result6 = {}
                result6['id'] = item.id
                result6['class'] = item.__class__.__name__
                result6['event'] = item.event
                result6['candidate'] = item.candidate
                result6['exam_date'] = item.exam_date
                result6['exam_title'] = item.exam_title
                result6['file'] = item.file
                result6['overall'] = item.overall
                result_list.append(result6)

        paut_l3_cswip_result = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult.objects.all()
        if paut_l3_cswip_result.count() > 0:
            for item in paut_l3_cswip_result:
                result7 = {}
                result7['id'] = item.id
                result7['class'] = item.__class__.__name__
                result7['event'] = item.event
                result7['candidate'] = item.candidate
                result7['exam_date'] = item.exam_date
                result7['exam_title'] = item.exam_title
                result7['file'] = item.file
                result7['overall'] = item.overall
                result_list.append(result7)

        paut_l3_pcn_result = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result.objects.all()
        if paut_l3_pcn_result.count() > 0:
            for item in paut_l3_pcn_result:
                result8 = {}
                result8['id'] = item.id
                result8['class'] = item.__class__.__name__
                result8['event'] = item.event
                result8['candidate'] = item.candidate
                result8['exam_date'] = item.exam_date
                result8['exam_title'] = item.exam_title
                result8['file'] = item.file
                result8['overall'] = item.overall
                result_list.append(result8)

        tofd_l2_pcn_result = Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.all()
        if tofd_l2_pcn_result.count() > 0:
            for item in tofd_l2_pcn_result:
                result9 = {}
                result9['id'] = item.id
                result9['class'] = item.__class__.__name__
                result9['event'] = item.event
                result9['candidate'] = item.candidate
                result9['exam_date'] = item.exam_date
                result9['exam_title'] = item.exam_title
                result9['file'] = item.file
                result9['overall'] = item.overall
                result_list.append(result9)

        tofd_l2_cswip_result = ExamMaterialTOFD_CSWIP.objects.all()
        if tofd_l2_cswip_result.count() > 0:
            for item in tofd_l2_cswip_result:
                result10 = {}
                result10['id'] = item.id
                result10['class'] = item.__class__.__name__
                result10['event'] = item.event
                result10['candidate'] = item.candidate
                result10['exam_date'] = item.exam_date
                result10['exam_title'] = item.exam_title
                result10['file'] = item.file
                result10['overall'] = item.overall
                result_list.append(result10)

        tofd_l3_cswip_result = TimeFlightDiffractionTOFDLevel3_CSWIP_Result.objects.all()
        if tofd_l3_cswip_result.count() > 0:
            for item in tofd_l3_cswip_result:
                result11 = {}
                result11['id'] = item.id
                result11['class'] = item.__class__.__name__
                result11['event'] = item.event
                result11['candidate'] = item.candidate
                result11['exam_date'] = item.exam_date
                result11['exam_title'] = item.exam_title
                result11['file'] = item.file
                result11['overall'] = item.overall
                result_list.append(result11)

        tofd_l3_pcn_result = TimeFlightDiffractionTOFDLevel3_PCN_Result3.objects.all()
        if tofd_l3_pcn_result.count() > 0:
            for item in tofd_l3_pcn_result:
                result12 = {}
                result12['id'] = item.id
                result12['class'] = item.__class__.__name__
                result12['event'] = item.event
                result12['candidate'] = item.candidate
                result12['exam_date'] = item.exam_date
                result12['exam_title'] = item.exam_title
                result12['file'] = item.file
                result12['overall'] = item.overall
                result_list.append(result12)

        ri_result = RadiographicInterpretationWeldsRIResult.objects.all()
        if ri_result.count() > 0:
            for item in ri_result:
                result13 = {}
                result13['id'] = item.id
                result13['class'] = item.__class__.__name__
                result13['event'] = item.event
                result13['candidate'] = item.candidate
                result13['exam_date'] = item.exam_date
                result13['exam_title'] = item.exam_title
                result13['file'] = item.file
                result13['overall'] = item.overall
                result_list.append(result13)

        dri_result = DigitalRadiographicInterpretationDRI_Level2_Result.objects.all()
        if dri_result.count() > 0:
            for item in dri_result:
                result14 = {}
                result14['id'] = item.id
                result14['class'] = item.__class__.__name__
                result14['event'] = item.event
                result14['candidate'] = item.candidate
                result14['exam_date'] = item.exam_date
                result14['exam_title'] = item.exam_title
                result14['file'] = item.file
                result14['overall'] = item.overall
                result_list.append(result14)

        # pcn_certifications = PcnCertificateProduct.objects.all()
        # for item in pcn_certifications:
        #     result1 = {}
        #     result1['id'] = item.id
        #     result1['cer_number'] = item.cer_number
        #     result1['candidate'] = item.candidate
        #     result1['issue_date'] = item.issue_date
        #     result_list.append(result1)

        context['group_name'] = group_name
        context['candidate'] = candidate
        context['result_list'] = result_list
        return context

    def post(self, request, *args, **kwargs):
        context = super(NotificationView, self).get_context_data()
        if request.method == 'POST':
            project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            load_dotenv(os.path.join(project_folder, '.env'))
            MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')

            ids = request.POST.getlist('ids[]')
            print(ids)

            print("here")
            # message = {
            #     "from_email": "erp@tescan.ca",
            #     "subject": subject,
            #     "text": message,
            #     "to": [
            #         {
            #             "email": target_email,
            #             "type": "to"
            #         }
            #     ]
            # }
            # try:
            #     mailchimp = MailchimpTransactional.Client(MAILCHIMP_API_KEY)
            #     response = mailchimp.messages.send({"message": message})
            #     print('API called successfully: {}'.format(response))
            # except ApiClientError as error:
            #     print('An exception occurred: {}'.format(error.text))
            #

            candidate = TesCandidate.objects.filter(user=self.request.user).first()
            group_name = self.request.user.groups.values_list('name', flat=True).first()
            context['group_name'] = group_name
            context['candidate'] = candidate

            return redirect('marketing:notificationlist_')

class MailerView(GroupRequiredMixin,SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "marketing/new_mail.html"
    group_required = [u'management', u'admin', u'training_admin', u'training_operator']

    def get_context_data(self):
        context = super(MailerView, self).get_context_data()
        user_list =User.objects.filter(groups__name='candidates')
        candidate_list = TesCandidate.objects.filter(tes_candidate_id__isnull = False)
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()

        context['candidate_list'] = candidate_list
        context['group_name'] = group_name
        context['candidate'] = candidate

        return context


class NewMailchipEmail(GroupRequiredMixin,SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "marketing/new_mailchip_mail.html"
    group_required = [u'management', u'admin', u'training_admin', u'training_operator']

    def get_context_data(self):
        context = super(NewMailchipEmail, self).get_context_data()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] = candidate
        return context


    def post(self, request, *args, **kwargs):
        context = super(NewMailchipEmail, self).get_context_data()
        if request.method == 'POST':
            project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            load_dotenv(os.path.join(project_folder, '.env'))
            target_email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')

            message = {
                "from_email": "erp@tescan.ca",
                "subject": subject,
                "text": message,
                "to": [
                    {
                        "email": target_email,
                        "type": "to"
                    }
                ]
            }
            try:
                mailchimp = MailchimpTransactional.Client(MAILCHIMP_API_KEY)
                response = mailchimp.messages.send({"message": message})
                print('API called successfully: {}'.format(response))
            except ApiClientError as error:
                print('An exception occurred: {}'.format(error.text))


            candidate = TesCandidate.objects.filter(user=self.request.user).first()
            group_name = self.request.user.groups.values_list('name', flat=True).first()
            context['group_name'] = group_name
            context['candidate'] = candidate

            return redirect('marketing:mailer_')
