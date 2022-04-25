from django.shortcuts import render, redirect
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


from training.models import TesCandidate
from django.contrib.auth.mixins import LoginRequiredMixin
from authorization.sidebarmixin import SidebarMixin
from django.views.generic import View, TemplateView
from training.models import TesCandidate,Event
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from dateutil.relativedelta import *
from django.db.models import Q
import datetime

# Create your views here.



class ExamResultHistoryCSWIP31(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/cswip_result_history_3_1.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamResultHistoryCSWIP31, self).get_context_data()
        print(self.kwargs['candidate_id'])
        # user = User.objects.filter(id = self.kwargs['candidate_id']).first()
        candidate = TesCandidate.objects.filter(id=self.kwargs['candidate_id']).first()
        print(candidate)
        results = CSWIPWeldingInspector3_1Result.objects.filter(candidate=candidate)

        context['results'] = results
        # context['examCount'] = examCount
        return context




class DeleteExam_Result_ExamMaterialTOFD_CSWIP(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = ExamMaterialTOFD_CSWIP
    success_url = reverse_lazy('exam_certification:examtofdl2cswipresultsummary_')




class NewExam_Result_ExamMaterialTOFD_CSWIP(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_tofd_ultra_l3_cswip_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExam_Result_ExamMaterialTOFD_CSWIP, self).get_context_data()
        exams = ExamMaterialTOFDModel1.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExam_Result_ExamMaterialTOFD_CSWIP, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo 2")
                print(request.POST['exam_ID'])
                exam = ExamMaterialTOFDModel1.objects.filter(id=self.request.POST['exam_ID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                print(exam)
                context['exam'] = exam

                return render(request, 'certificates/new_tofd_ultra_l3_cswip_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")

                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                print(self.request.POST['exam_ID'])
                exam = ExamMaterialTOFDModel1.objects.filter(id=self.request.POST['exam_ID']).first()
                obj = ExamMaterialTOFD_CSWIP()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam

                if not request.POST.get('exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.exam_title = self.request.POST['examTitle']
                obj.customerID = self.request.POST['customerID']
                # obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.specific_theory = self.request.POST['specific_theory']
                obj.general_theory = self.request.POST['general_theory']
                obj.sample1 = self.request.POST['sample1']
                obj.sample2 = self.request.POST['sample2']
                obj.data_file_1 = self.request.POST['data_file_1']
                obj.data_file_2 = self.request.POST['data_file_2']
                obj.data_file_3 = self.request.POST['data_file_3']
                obj.data_file_4 = self.request.POST['data_file_4']
                obj.written_instruction = self.request.POST['written_instruction']

                obj.remark = self.request.POST['paut_remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialTOFD_CSWIP.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examtofdl2cswipresultsummary_')
            return redirect('exam_certification:examtofdl2cswipresultsummary_')



class Exam_Result_ExamMaterialTOFD_CSWIP_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_cswip_tofd_l2_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Exam_Result_ExamMaterialTOFD_CSWIP_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = ExamMaterialTOFD_CSWIP.objects.all()
        examCount = ExamMaterialTOFD_CSWIP.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context



class DeleteExam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN
    success_url = reverse_lazy('exam_certification:examresulttofdl2pcnsummary_')


class NewExam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_paut_l2_exam_pcn_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN, self).get_context_data()
        exams = ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo 2")
                print(request.POST['examID'])
                exam = ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                print(exam)
                context['exam'] = exam

                return render(request, 'certificates/new_paut_l2_exam_pcn_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")

                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                print(self.request.POST['examID'])
                exam = ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.filter(id=self.request.POST['examID']).first()
                obj = Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam

                if not request.POST.get('exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.exam_title = self.request.POST['examTitle']
                obj.customerID = self.request.POST['customerID']
                # obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.specific_theory = self.request.POST['specific_theory']
                # obj.general_practical = self.request.POST['general_practical']
                obj.sample1_collection = self.request.POST['sample1_collection']
                obj.sample2_collection = self.request.POST['sample2_collection']
                obj.sample1_analysis = self.request.POST['sample1_analysis']
                obj.sample2_analysis = self.request.POST['sample2_analysis']
                obj.sample3_analysis = self.request.POST['sample3_analysis']
                obj.sample4_analysis = self.request.POST['sample4_analysis']
                obj.sample5_analysis = self.request.POST['sample5_analysis']
                obj.written_instruction = self.request.POST['written_instruction']

                obj.remark = self.request.POST['remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examresulttofdl2pcnsummary_')
            return redirect('exam_certification:examresulttofdl2pcnsummary_')




class Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_pcn_tofd_l2_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.all()
        examCount = Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context


class DeleteExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN
    success_url = reverse_lazy('exam_certification:exammaterialtofdl2pcnsummary_')

class NewExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_pautl2_pcn_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_pautl2_pcn_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_pautl2_pcn_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['customerID']
                # obj.paut_scheme = self.request.POST['paut_scheme']
                if not request.POST.get('exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')


                obj.specific_theory = self.request.POST['specific_theory']
                sample = Samples.objects.filter(id=self.request.POST['sample1_collection']).first()
                obj.sample1_collection = sample
                sample = Samples.objects.filter(id=self.request.POST['sample2_collection']).first()
                obj.sample2_collection = sample
                sample = Samples.objects.filter(id=self.request.POST['sample1_analysis']).first()
                obj.sample1_analysis = sample
                sample = Samples.objects.filter(id=self.request.POST['sample2_analysis']).first()
                obj.sample2_analysis = sample
                sample = Samples.objects.filter(id=self.request.POST['sample3_analysis']).first()
                obj.sample3_analysis = sample
                sample = Samples.objects.filter(id=self.request.POST['sample4_analysis']).first()
                obj.sample4_analysis = sample
                sample = Samples.objects.filter(id=self.request.POST['sample5_analysis']).first()
                obj.sample5_analysis = sample
                sample = Samples.objects.filter(id=self.request.POST['written_instruction']).first()
                obj.written_instruction = sample
                # obj.delivery_method = self.request.POST['paut_delivery_method']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.exam_title = self.request.POST['examTitle']
                obj.remark = self.request.POST['remarks']
                obj.save()
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_material_l3_summary.html', context=context)
                return redirect('exam_certification:exammaterialtofdl2pcnsummary_')
            return redirect('exam_certification:exammaterialtofdl2pcnsummary_')




class ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCNAdmin_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_tofd_pcn_l2_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCNAdmin_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.all()
        examCount = ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context


class DeleteDigitalRadiographicInterpretationDRI_Level2_Result(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = DigitalRadiographicInterpretationDRI_Level2_Result
    success_url = reverse_lazy('exam_certification:examdriresultsummary_')


class NewDigitalRadiographicInterpretationDRI_Level2_Result(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_dri_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewDigitalRadiographicInterpretationDRI_Level2_Result, self).get_context_data()
        exams = DigitalRadiographicInterpretationDRI_Level2_Material3.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewDigitalRadiographicInterpretationDRI_Level2_Result, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = DigitalRadiographicInterpretationDRI_Level2_Material3.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                context['exam'] = exam

                return render(request, 'certificates/new_dri_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                print(self.request.POST['exam_ID'])
                exam = DigitalRadiographicInterpretationDRI_Level2_Material3.objects.filter(id=self.request.POST['exam_ID']).first()
                obj = DigitalRadiographicInterpretationDRI_Level2_Result()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                obj.exam_title = self.request.POST['examTitle']
                if not request.POST.get('exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')

                obj.general_theory = self.request.POST['general_theory']
                obj.specific_theory = self.request.POST['specific_theory']
                obj.general_practical = self.request.POST['general_practical']
                obj.data_analysis1 = self.request.POST['data_analysis1']
                obj.data_analysis2 = self.request.POST['data_analysis2']
                obj.data_analysis3 = self.request.POST['data_analysis3']
                obj.data_analysis3 = self.request.POST['data_analysis3']
                obj.data_analysis4 = self.request.POST['data_analysis4']
                obj.data_analysis5 = self.request.POST['data_analysis5']
                obj.data_analysis6 = self.request.POST['data_analysis6']

                obj.remark = self.request.POST['paut_remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = DigitalRadiographicInterpretationDRI_Level2_Result.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examdriresultsummary_')
            return redirect('exam_certification:examdriresultsummary_')




class DigitalRadiographicInterpretationDRI_Level2_Result_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/dri_result_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DigitalRadiographicInterpretationDRI_Level2_Result_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = DigitalRadiographicInterpretationDRI_Level2_Result.objects.all()
        examCount = DigitalRadiographicInterpretationDRI_Level2_Result.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context




class DeleteDigitalRadiographicInterpretationDRI_Level2_Material(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = DigitalRadiographicInterpretationDRI_Level2_Material3
    success_url = reverse_lazy('exam_certification:exammaterialdrisummary_')



class DigitalRadiographicInterpretationDRI_Level2_Material_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/dri_material_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DigitalRadiographicInterpretationDRI_Level2_Material_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = DigitalRadiographicInterpretationDRI_Level2_Material3.objects.all()
        examCount = DigitalRadiographicInterpretationDRI_Level2_Material3.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context




class NewDigitalRadiographicInterpretationDRI_Level2_Material(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_dri_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewDigitalRadiographicInterpretationDRI_Level2_Material, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewDigitalRadiographicInterpretationDRI_Level2_Material, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_dri_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_dri_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = DigitalRadiographicInterpretationDRI_Level2_Material3()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['customerID']
                obj.exam_title = self.request.POST['examTitle']
                if not request.POST.get('exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')

                obj.general_theory = self.request.POST['general_theory']
                obj.specific_theory = self.request.POST['specific_theory']
                obj.general_practical = self.request.POST['general_practical']
                obj.data_analysis1 = self.request.POST['data_analysis1']
                obj.data_analysis2 = self.request.POST['data_analysis2']
                obj.data_analysis3 = self.request.POST['data_analysis3']
                obj.data_analysis4 = self.request.POST['data_analysis4']
                obj.data_analysis5 = self.request.POST['data_analysis5']
                obj.data_analysis6 = self.request.POST['data_analysis6']
                # obj.delivery_method = self.request.POST['paut_delivery_method']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                # obj.venue = self.request.POST['venue']
                obj.remark = self.request.POST['remarks']
                obj.save()
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = DigitalRadiographicInterpretationDRI_Level2_Material3.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_material_l3_summary.html', context=context)
                return redirect('exam_certification:exammaterialdrisummary_')
            return redirect('exam_certification:exammaterialdrisummary_')




class DeleteRadiographicInterpretationWeldsRIResult(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = RadiographicInterpretationWeldsRIResult
    success_url = reverse_lazy('exam_certification:examriresultsummary_')



class NewRadiographicInterpretationWeldsRIResult(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_ri_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewRadiographicInterpretationWeldsRIResult, self).get_context_data()
        exams = RadiographicInterpretationWeldsRIMaterial.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewRadiographicInterpretationWeldsRIResult, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = RadiographicInterpretationWeldsRIMaterial.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                context['exam'] = exam

                return render(request, 'certificates/new_ri_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                print(self.request.POST['exam_ID'])
                exam = RadiographicInterpretationWeldsRIMaterial.objects.filter(id=self.request.POST['exam_ID']).first()
                obj = RadiographicInterpretationWeldsRIResult()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                obj.exam_title = self.request.POST['examTitle']
                if not request.POST.get('exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.general_theory = self.request.POST['general_theory']
                obj.specific_theory = self.request.POST['specific_theory']
                obj.practical = self.request.POST['practical']

                obj.remark = self.request.POST['paut_remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = RadiographicInterpretationWeldsRIResult.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examriresultsummary_')
            return redirect('exam_certification:examriresultsummary_')




class RadiographicInterpretationWeldsRIResult_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_ri_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RadiographicInterpretationWeldsRIResult_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = RadiographicInterpretationWeldsRIResult.objects.all()
        examCount = RadiographicInterpretationWeldsRIResult.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context



class DeleteRadiographicInterpretationWeldsRIMaterial(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = RadiographicInterpretationWeldsRIMaterial
    success_url = reverse_lazy('exam_certification:examrisummary_')



class NewRadiographicInterpretationWeldsRIMaterial(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_ri_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewRadiographicInterpretationWeldsRIMaterial, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewRadiographicInterpretationWeldsRIMaterial, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_ri_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_ri_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = RadiographicInterpretationWeldsRIMaterial()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['customerID']
                obj.exam_title = self.request.POST['examTitle']
                if not request.POST.get('exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.general_theory = self.request.POST['general_theory']
                obj.specific_theory = self.request.POST['specific_theory']
                obj.practical = self.request.POST['practical']

                # obj.delivery_method = self.request.POST['paut_delivery_method']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                # obj.venue = self.request.POST['venue']
                obj.remark = self.request.POST['remarks']
                obj.save()
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = RadiographicInterpretationWeldsRIMaterial.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_material_l3_summary.html', context=context)
                return redirect('exam_certification:examrisummary_')
            return redirect('exam_certification:examrisummary_')


class RadiographicInterpretationWeldsRIMaterial_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_RI_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RadiographicInterpretationWeldsRIMaterial_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = RadiographicInterpretationWeldsRIMaterial.objects.all()
        examCount = RadiographicInterpretationWeldsRIMaterial.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context


class DeleteTimeFlightDiffractionTOFDLevel3_PCN_Result(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = TimeFlightDiffractionTOFDLevel3_PCN_Result3
    success_url = reverse_lazy('exam_certification:newpcntofdresultresult_')


class NewTimeFlightDiffractionTOFDLevel3_PCN_Result(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_tofd_ultra_l3_pcn_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewTimeFlightDiffractionTOFDLevel3_PCN_Result, self).get_context_data()
        exams = TimeFlightDiffractionTOFDLevel3_PCN_Material2.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewTimeFlightDiffractionTOFDLevel3_PCN_Result, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = TimeFlightDiffractionTOFDLevel3_PCN_Material2.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                context['exam'] = exam

                return render(request, 'certificates/new_tofd_ultra_l3_pcn_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                print(self.request.POST['exam_ID'])
                exam = TimeFlightDiffractionTOFDLevel3_PCN_Material2.objects.filter(id=self.request.POST['exam_ID']).first()
                obj = TimeFlightDiffractionTOFDLevel3_PCN_Result3()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                if not request.POST.get('exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.exam_title = self.request.POST['examTitle']
                obj.basic_a1 = self.request.POST['basic_a1']
                obj.basic_a2 = self.request.POST['basic_a2']
                obj.basic_b_part_1 = self.request.POST['basic_b_part_1']
                obj.basic_b_part_2 = self.request.POST['basic_b_part_2']
                obj.basic_b_part_3 = self.request.POST['basic_b_part_3']
                obj.basic_b_part_4 = self.request.POST['basic_b_part_4']
                obj.main_d = self.request.POST['main_d']
                obj.main_e = self.request.POST['main_e']
                obj.main_f = self.request.POST['main_f']
                obj.practical_tofd_l2 = self.request.POST['practical_tofd_l2']
                obj.remark = self.request.POST['paut_remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = TimeFlightDiffractionTOFDLevel3_PCN_Result3.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:exampcntofdresultsummary_')
            return redirect('exam_certification:exampcntofdresultsummary_')




class TimeFlightDiffractionTOFDLevel3_PCN_Result_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_l3_tofd_altra_pcn_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TimeFlightDiffractionTOFDLevel3_PCN_Result_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = TimeFlightDiffractionTOFDLevel3_PCN_Result3.objects.all()
        examCount = TimeFlightDiffractionTOFDLevel3_PCN_Result3.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context


class DeleteTimeFlightDiffractionTOFDLevel3_PCN_Material(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = TimeFlightDiffractionTOFDLevel3_PCN_Material2
    success_url = reverse_lazy('exam_certification:exampcntofdl3summary_')



class NewTimeFlightDiffractionTOFDLevel3_PCN_Material(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_pcn_tofd_phased_array_ultera_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewTimeFlightDiffractionTOFDLevel3_PCN_Material, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewTimeFlightDiffractionTOFDLevel3_PCN_Material, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_pcn_tofd_phased_array_ultera_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_pcn_tofd_phased_array_ultera_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = TimeFlightDiffractionTOFDLevel3_PCN_Material2()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['customerID']
                obj.exam_title = self.request.POST['examTitle']
                if not request.POST.get('exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.basic_a1 = self.request.POST['paut_basic_a1']
                obj.basic_a2 = self.request.POST['paut_basic_a2']
                obj.basic_b_part_1 = self.request.POST['paut_basic_b_part_1']
                obj.basic_b_part_2 = self.request.POST['paut_basic_b_part_2']
                obj.basic_b_part_3 = self.request.POST['paut_basic_b_part_3']
                obj.basic_b_part_4 = self.request.POST['paut_basic_b_part_4']
                obj.main_d = self.request.POST['main_d']
                obj.main_e = self.request.POST['main_e']
                obj.main_f = self.request.POST['main_f']
                obj.practical_tofd_l2 = self.request.POST['practical_tofd_l2']
                # obj.delivery_method = self.request.POST['paut_delivery_method']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                # obj.venue = self.request.POST['venue']
                obj.remark = self.request.POST['remarks']
                obj.save()
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = TimeFlightDiffractionTOFDLevel3_PCN_Material2.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_material_l3_summary.html', context=context)
                return redirect('exam_certification:exampcntofdl3summary_')
            return redirect('exam_certification:exampcntofdl3summary_')


class TimeFlightDiffractionTOFDLevel3_PCN_Material_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_l3_tofd_altra_pcn_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TimeFlightDiffractionTOFDLevel3_PCN_Material_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = TimeFlightDiffractionTOFDLevel3_PCN_Material2.objects.all()
        examCount = TimeFlightDiffractionTOFDLevel3_PCN_Material2.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context



class DeleteTimeFlightDiffractionTOFDLevel3_CSWIP_Result(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = TimeFlightDiffractionTOFDLevel3_CSWIP_Result
    success_url = reverse_lazy('exam_certification:examswiptofdresultsummary_')



class TimeFlightDiffractionTOFDLevel3_CSWIP_Result_Result(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_tofd_ultra_l3_cswip_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TimeFlightDiffractionTOFDLevel3_CSWIP_Result_Result, self).get_context_data()
        exams = TimeFlightDiffractionTOFDLevel3_CSWIP_Material2.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(TimeFlightDiffractionTOFDLevel3_CSWIP_Result_Result, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = TimeFlightDiffractionTOFDLevel3_CSWIP_Material2.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                context['exam'] = exam

                return render(request, 'certificates/new_tofd_ultra_l3_cswip_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                print(self.request.POST['exam_ID'])
                exam = TimeFlightDiffractionTOFDLevel3_CSWIP_Material2.objects.filter(id=self.request.POST['exam_ID']).first()
                obj = TimeFlightDiffractionTOFDLevel3_CSWIP_Result()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                if not request.POST.get('paut_exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['paut_exam_date'], '%m/%d/%Y')
                obj.exam_title = self.request.POST['paut_examTitle']
                obj.basic_a1 = self.request.POST['basic_a1']
                obj.basic_a2 = self.request.POST['basic_a2']
                obj.basic_b_part_1 = self.request.POST['basic_b_part_1']
                obj.basic_b_part_2 = self.request.POST['basic_b_part_2']
                obj.basic_b_part_3 = self.request.POST['basic_b_part_3']
                obj.basic_b_part_4 = self.request.POST['basic_b_part_4']
                obj.main_c_1 = self.request.POST['main_c_1']
                obj.main_c_2 = self.request.POST['main_c_2']
                obj.main_c_3 = self.request.POST['main_c_3']
                obj.practical_tofd_l2 = self.request.POST['practical_tofd_l2']
                obj.remark = self.request.POST['paut_remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = TimeFlightDiffractionTOFDLevel3_CSWIP_Result.objects.all()

                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examswiptofdresultsummary_')
            return redirect('exam_certification:examswiptofdresultsummary_')



class TimeFlightDiffractionTOFDLevel3_CSWIP_Result_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_l3_tofd_altra_cswip_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TimeFlightDiffractionTOFDLevel3_CSWIP_Result_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = TimeFlightDiffractionTOFDLevel3_CSWIP_Result.objects.all()
        examCount = TimeFlightDiffractionTOFDLevel3_CSWIP_Result.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context




class DeleteTimeFlightDiffractionTOFDLevel3_CSWIP_Material(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = TimeFlightDiffractionTOFDLevel3_CSWIP_Material2
    success_url = reverse_lazy('exam_certification:examcswiptofdl3summary_')





class NewTimeFlightDiffractionTOFDLevel3_CSWIP_Material(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_cswip_tofd_phased_array_ultera_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewTimeFlightDiffractionTOFDLevel3_CSWIP_Material, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewTimeFlightDiffractionTOFDLevel3_CSWIP_Material, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_cswip_tofd_phased_array_ultera_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_cswip_tofd_phased_array_ultera_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = TimeFlightDiffractionTOFDLevel3_CSWIP_Material2()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['customerID']
                # obj.paut_scheme = self.request.POST['paut_scheme']
                if not request.POST.get('exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')

                obj.basic_a1 = self.request.POST['paut_basic_a1']
                obj.basic_a2 = self.request.POST['paut_basic_a2']
                obj.basic_b_part_1 = self.request.POST['paut_basic_b_part_1']
                obj.basic_b_part_2 = self.request.POST['paut_basic_b_part_2']
                obj.basic_b_part_3 = self.request.POST['paut_basic_b_part_3']
                obj.basic_b_part_4 = self.request.POST['paut_basic_b_part_4']
                obj.main_c1 = self.request.POST['main_c1']
                obj.main_c2 = self.request.POST['main_c2']
                obj.main_c3 = self.request.POST['main_c3']
                obj.practical_tofd_l2 = self.request.POST['practical_tofd_l2']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                # obj.venue = self.request.POST['venue']
                obj.exam_title = self.request.POST['examTitle']
                obj.save()
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = TimeFlightDiffractionTOFDLevel3_CSWIP_Material2.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_material_l3_summary.html', context=context)
                return redirect('exam_certification:examcswiptofdl3summary_')
            return redirect('exam_certification:examcswiptofdl3summary_')



class TimeFlightDiffractionTOFDLevel3_CSWIP_Material_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_l3_tofd_altra_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TimeFlightDiffractionTOFDLevel3_CSWIP_Material_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = TimeFlightDiffractionTOFDLevel3_CSWIP_Material2.objects.all()
        examCount = TimeFlightDiffractionTOFDLevel3_CSWIP_Material2.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context





class DeletePhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result
    success_url = reverse_lazy('exam_certification:exampcnultral3resultsummary_')



class NewPhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_paut_ultra_l3_pcn_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewPhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result, self).get_context_data()
        exams = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewPhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                context['exam'] = exam

                return render(request, 'certificates/new_paut_ultra_l3_pcn_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                print(self.request.POST['exam_ID'])
                exam = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material.objects.filter(id=self.request.POST['exam_ID']).first()
                obj = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.basic_a1 = self.request.POST['basic_a1']
                obj.basic_a2 = self.request.POST['basic_a2']
                obj.basic_b_part_1 = self.request.POST['basic_b_part_1']
                obj.basic_b_part_2 = self.request.POST['basic_b_part_2']
                obj.basic_b_part_3 = self.request.POST['basic_b_part_3']
                obj.basic_b_part_4 = self.request.POST['basic_b_part_4']
                obj.main_d = self.request.POST['main_d']
                obj.main_e = self.request.POST['main_e']
                obj.main_f = self.request.POST['main_f']
                obj.practical_paut_l2 = self.request.POST['practical_paut_l2']
                obj.remark = self.request.POST['paut_remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:exampcnultral3resultsummary_')
            return redirect('exam_certification:exampcnultral3resultsummary_')



class PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_l3_paut_altra_pcn_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result.objects.all()
        examCount = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context



class DeletePhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material
    success_url = reverse_lazy('exam_certification:exampcnl3summary_')



class NewExamMaterialPAUTUltraL3PCN(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_paut_ultra_l3_pcn_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialPAUTUltraL3PCN, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialPAUTUltraL3PCN, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_paut_ultra_l3_pcn_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_paut_ultra_l3_pcn_material.html', context)
            elif 'submit_paut' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['customerID']
                obj.exam_title = self.request.POST['examTitle']
                if not request.POST.get('paut_exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['paut_exam_date'], '%m/%d/%Y')
                obj.basic_a1 = self.request.POST['paut_basic_a1']
                obj.basic_a2 = self.request.POST['paut_basic_a2']
                obj.basic_b_part_1 = self.request.POST['paut_basic_b_part_1']
                obj.basic_b_part_2 = self.request.POST['paut_basic_b_part_2']
                obj.basic_b_part_3 = self.request.POST['paut_basic_b_part_3']
                obj.basic_b_part_4 = self.request.POST['paut_basic_b_part_3']
                obj.main_d = self.request.POST['main_d']
                obj.main_e = self.request.POST['main_e']
                obj.main_f = self.request.POST['main_f']
                obj.practical_paut_l2 = self.request.POST['practical_paut_l2']
                obj.lecturer = self.request.POST['paut_lecturer']
                obj.invigilator = self.request.POST['paut_invigilator']
                # obj.venue = self.request.POST['paut_venue']
                obj.remark = self.request.POST['paut_remarks']
                obj.save()
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_material_l3_summary.html', context=context)
                return redirect('exam_certification:exampcnl3summary_')



class PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_l3_pcn_phased_array_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material.objects.all()
        examCount = PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context





class DeletePhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult
    success_url = reverse_lazy('exam_certification:examscwipultral3resultsummary_')



class NewExamResultPAUTUltraL3(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_paut_ultra_l3_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamResultPAUTUltraL3, self).get_context_data()
        exams = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamResultPAUTUltraL3, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                context['exam'] = exam

                return render(request, 'certificates/new_paut_ultra_l3_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                print(self.request.POST['exam_ID'])
                exam = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial.objects.filter(id=self.request.POST['exam_ID']).first()
                obj = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.basic_a1 = self.request.POST['basic_a1']
                obj.basic_a2 = self.request.POST['basic_a2']
                obj.basic_b_part_1 = self.request.POST['basic_b_part_1']
                obj.basic_b_part_2 = self.request.POST['basic_b_part_2']
                obj.basic_b_part_3 = self.request.POST['basic_b_part_3']
                obj.basic_b_part_4 = self.request.POST['basic_b_part_4']
                obj.practical_paut_l2 = self.request.POST['practical_paut_l2']
                obj.remark = self.request.POST['paut_remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examscwipultral3resultsummary_')
            return redirect('exam_certification:examscwipultral3resultsummary_')


class PhasedArrayUltrasonicTesting_PAUT_L3CSWIP_Result_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_l3_paut_altra_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PhasedArrayUltrasonicTesting_PAUT_L3CSWIP_Result_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult.objects.all()
        examCount = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context


class DeletePhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial
    success_url = reverse_lazy('exam_certification:examscwipultral3summary_')



class NewExamMaterialPAUTUltraL3(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_paut_ultra_l3_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialPAUTUltraL3, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialPAUTUltraL3, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_paut_ultra_l3_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_paut_ultra_l3_material.html', context)
            elif 'submit_paut' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['customerID']
                # obj.paut_scheme = self.request.POST['paut_scheme']
                if not request.POST.get('paut_exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['paut_exam_date'], '%m/%d/%Y')

                obj.basic_a1 = self.request.POST['paut_basic_a1']
                obj.basic_a2 = self.request.POST['paut_basic_a2']
                obj.basic_b_part_1 = self.request.POST['paut_basic_b_part_1']
                obj.basic_b_part_2 = self.request.POST['paut_basic_b_part_2']
                obj.basic_b_part_3 = self.request.POST['paut_basic_b_part_3']
                obj.basic_b_part_4 = self.request.POST['paut_basic_b_part_4']
                obj.main_c_1 = self.request.POST['paut_main_c_1']
                obj.main_c_2 = self.request.POST['paut_main_c_2']
                obj.main_c_3 = self.request.POST['paut_main_c_3']
                obj.practical_paut_l2 = self.request.POST['practical_paut_l2']
                # obj.delivery_method = self.request.POST['paut_delivery_method']
                obj.lecturer = self.request.POST['paut_lecturer']
                obj.invigilator = self.request.POST['paut_invigilator']
                # obj.venue = self.request.POST['paut_venue']
                obj.remark = self.request.POST['paut_remarks']
                obj.save()
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_material_l3_summary.html', context=context)
                return redirect('exam_certification:examscwipultral3summary_')


        # return render(request, 'certificates/exam_material_l3_summary.html',context=context)



class PhasedArrayUltrasonicTesting_PAUT_L3CSWIPSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_l3_paut_altra_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PhasedArrayUltrasonicTesting_PAUT_L3CSWIPSummary, self).get_context_data()
        events = Event.objects.all()
        exams = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial.objects.all()
        examCount = PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context






class DeletePhasedArrayPCNResult(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN
    success_url = reverse_lazy('exam_certification:exampcnphasedarrayresultsummary_')



class NewExamResultPCNPhasedArrayUltrasonic(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_phased_array_l2_exam_pcn_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamResultPCNPhasedArrayUltrasonic, self).get_context_data()
        exams = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamResultPCNPhasedArrayUltrasonic, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                context['exam'] = exam

                return render(request, 'certificates/new_phased_array_l2_exam_pcn_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                print(self.request.POST['exam_ID'])
                exam = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.filter(id=self.request.POST['exam_ID']).first()
                obj = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.general_theory = self.request.POST['general_theory']
                obj.sample1_analysis = self.request.POST['sample1_analysis']
                obj.sample1_collection = self.request.POST['sample1_collection']
                obj.sample2_analysis = self.request.POST['sample2_analysis']
                obj.sample2_collection = self.request.POST['sample2_collection']
                obj.sample3_analysis = self.request.POST['sample3_analysis']
                obj.sample3_collection = self.request.POST['sample3_collection']
                obj.written_instruction = self.request.POST['written_instruction']
                obj.remark = self.request.POST['remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:exampcnphasedarrayresultsummary_')
            return redirect('exam_certification:exampcnphasedarrayresultsummary_')



class PCNPhasedArrayUltrasonicResultSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_phaied_array_ultera_pcn_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PCNPhasedArrayUltrasonicResultSummary, self).get_context_data()
        events = Event.objects.all()
        exams = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.all()
        examCount = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context




class DeletePhasedArrayPCNMaterial(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN
    success_url = reverse_lazy('exam_certification:exampcnphasedarraysummary_')



class NewExamMaterialPCNPhasedArrayUltera(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_pcn_phased_array_ultera_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialPCNPhasedArrayUltera, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialPCNPhasedArrayUltera, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_pcn_phased_array_ultera_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_pcn_phased_array_ultera_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN()
                obj.event = event
                obj.candidate = candidate
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.examTitle = self.request.POST['examTitle']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.exam_title = self.request.POST['examTitle']
              
                obj.specific_theory = self.request.POST['specific_theory']
                sample3 = Samples.objects.filter(id=self.request.POST['sample1_analysis']).first()
                obj.sample1_analysis = sample3
                sample4 = Samples.objects.filter(id=self.request.POST['sample1_collection']).first()
                obj.sample1_collection = sample4
                sample5 = Samples.objects.filter(id=self.request.POST['sample2_analysis']).first()
                obj.sample2_analysis = sample5
                sample6 = Samples.objects.filter(id=self.request.POST['sample2_collection']).first()
                obj.sample2_collection = sample6
                sample7 = Samples.objects.filter(id=self.request.POST['sample3_analysis']).first()
                obj.sample3_analysis = sample7
                sample8 = Samples.objects.filter(id=self.request.POST['sample3_collection']).first()
                obj.sample3_collection = sample8
                sample9 = Samples.objects.filter(id=self.request.POST['written_instruction']).first()
                obj.written_instruction = sample9
                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/exam_material_phaied_array_ultera_pcn_summary.html',context=context)



class PCNPhasedArrayUltrasonicMaterialSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_phaied_array_ultera_pcn_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PCNPhasedArrayUltrasonicMaterialSummary, self).get_context_data()
        events = Event.objects.all()
        exams = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.all()
        examCount = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context






class DeletePhasedArrayResultL2(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP
    success_url = reverse_lazy('exam_certification:cswipphasedarrayresultsummary_')



class NewExamResultCSWIPPhasedArrayUltrasonic(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_phased_array_l2_exam_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamResultCSWIPPhasedArrayUltrasonic, self).get_context_data()
        exams = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamResultCSWIPPhasedArrayUltrasonic, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                context['exam'] = exam

                return render(request, 'certificates/new_phased_array_l2_exam_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                print(self.request.POST['exam_ID'])
                exam = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.filter(id=self.request.POST['exam_ID']).first()
                obj = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.general_theory = self.request.POST['general_theory']
                obj.specific_theory = self.request.POST['specific_theory']
                obj.sample1_analysis = self.request.POST['sample1_analysis']
                obj.sample1_collection = self.request.POST['sample1_collection']
                obj.sample2_analysis = self.request.POST['sample2_analysis']
                obj.sample2_collection = self.request.POST['sample2_collection']
                obj.sample3_analysis = self.request.POST['sample3_analysis']
                obj.sample3_collection = self.request.POST['sample3_collection']
                obj.written_instruction = self.request.POST['written_instruction']
                obj.remark = self.request.POST['remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:cswipphasedarrayresultsummary_')
            return redirect('exam_certification:cswipphasedarrayresultsummary_')




class CSWIPPhasedArrayUltrasonic_Result_Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_cswip_phased_array_ultra_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CSWIPPhasedArrayUltrasonic_Result_Summary, self).get_context_data()
        events = Event.objects.all()
        exams = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.all()
        examCount = Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context






class DeleteCSWIPPhasedAraayUltera(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP
    success_url = reverse_lazy('exam_certification:examscwipphasedarraysummary_')



class NewExamMaterialCSWIPPhasedArrayUltera(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_cswip_phased_array_ultera_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialCSWIPPhasedArrayUltera, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialCSWIPPhasedArrayUltera, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_cswip_phased_array_ultera_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_cswip_phased_array_ultera_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP()
                obj.event = event
                obj.candidate = candidate
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.examTitle = self.request.POST['examTitle']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.exam_title = self.request.POST['examTitle']
                print(self.request.POST['general_theory'])
                obj.general_theory = self.request.POST['general_theory']
                obj.specific_theory = id=self.request.POST['specific_theory']
                sample3 = Samples.objects.filter(id=self.request.POST['sample1_analysis']).first()
                obj.sample1_analysis = sample3
                sample4 = Samples.objects.filter(id=self.request.POST['sample1_collection']).first()
                obj.sample1_collection = sample4
                sample5 = Samples.objects.filter(id=self.request.POST['sample2_analysis']).first()
                obj.sample2_analysis = sample5
                sample6 = Samples.objects.filter(id=self.request.POST['sample2_collection']).first()
                obj.sample2_collection = sample6
                sample7 = Samples.objects.filter(id=self.request.POST['sample3_analysis']).first()
                obj.sample3_analysis = sample7
                sample8 = Samples.objects.filter(id=self.request.POST['sample3_collection']).first()
                obj.sample3_collection = sample8
                sample9 = Samples.objects.filter(id=self.request.POST['written_instruction']).first()
                obj.written_instruction = sample9
                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/exam_material_phaied_array_ultera_summary.html',context=context)



class CSWIPPhasedArrayUltrasonicSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_phaied_array_ultera_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CSWIPPhasedArrayUltrasonicSummary, self).get_context_data()
        events = Event.objects.all()
        exams = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.all()
        examCount = ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context






class DeletePaintingInspectionResult2(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = BGAS_CSWIP_PaintingInspectorResult
    success_url = reverse_lazy('exam_certification:paintinginspectionresultsummary_')


class NewExamResultPaintingInspection(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_painting_inspection_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamResultPaintingInspection, self).get_context_data()
        exams = BGAS_CSWIP_PaintingInspectorMaterial.objects.all()
        result_list = BGAS_CSWIP_PaintingInspectorResult.objects.all()
        print("Here")
        context['result_list'] = result_list
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamResultPaintingInspection, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = BGAS_CSWIP_PaintingInspectorMaterial.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                result_list = BGAS_CSWIP_PaintingInspectorResult.objects.all()
                context['result_list'] = result_list
                context['exam'] = exam
                return render(request, 'certificates/new_painting_inspection_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                exam = BGAS_CSWIP_PaintingInspectorMaterial.objects.filter(id=self.request.POST['examID']).first()
                obj = BGAS_CSWIP_PaintingInspectorResult()
                obj.event = event
                obj.candidate = candidate
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.exam = exam
                obj.general_theory = self.request.POST['general_theory']
                obj.practical = self.request.POST['practical']
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.remark = self.request.POST['remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()
                # if not request.POST.get('previouseID', '') == '':
                #     print("Exist")
                #     previousID = self.request.POST['previouseID'].split('-')[0]
                #     pre_result = CSWIPWeldingInspector3_1Result.objects.filter(id= previousID).first()
                #     print(pre_result)
                #
                #     repeat_obj = CSWIPWeldingInspector3_1ResultIntermadiate()
                #     repeat_obj.candidate = candidate
                #     repeat_obj.primary = pre_result
                #     repeat_obj.secondry = obj
                #     repeat_obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = BGAS_CSWIP_PaintingInspectorResult.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:paintinginspectionresultsummary_')
            return redirect('exam_certification:paintinginspectionresultsummary_')




class PaintingInspectionSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/painting_inspection_result_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PaintingInspectionSummary, self).get_context_data()
        events = Event.objects.all()
        exams = BGAS_CSWIP_PaintingInspectorResult.objects.all()
        examCount = BGAS_CSWIP_PaintingInspectorResult.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context


class DeletePaintingInspectionMaterial(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = BGAS_CSWIP_PaintingInspectorMaterial
    success_url = reverse_lazy('exam_certification:exampaintinginspectionsummary_')


class NewBGAS_CSWIP_PaintingInspector(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_painting_inspection_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewBGAS_CSWIP_PaintingInspector, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewBGAS_CSWIP_PaintingInspector, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_painting_inspection_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_painting_inspection_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = BGAS_CSWIP_PaintingInspectorMaterial()
                obj.event = event
                obj.candidate = candidate
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.customerID = self.request.POST['customerID']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                # obj.file = self.request.FILEs['file']
                obj.exam_title = self.request.POST['examTitle']
                obj.general_theory = self.request.POST['general_theory']
                obj.practical = self.request.POST['practical']



                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = BGAS_CSWIP_PaintingInspectorMaterial.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/painting_inspection_summary.html',context=context)



class BGAS_CSWIP_PaintingInspectorSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/painting_inspection_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BGAS_CSWIP_PaintingInspectorSummary, self).get_context_data()
        events = Event.objects.all()
        exams = BGAS_CSWIP_PaintingInspectorMaterial.objects.all()
        examCount = BGAS_CSWIP_PaintingInspectorMaterial.objects.count()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context






class DeleteCSWIPExamResult322(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = CSWIPWeldingInspector3_2_2_Result
    success_url = reverse_lazy('exam_certification:examscwip322resultsummary_')


class NewExamResultSwip322(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_cswip_3_2_2_exam_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamResultSwip322, self).get_context_data()
        exams = CSWIPWeldingInspector3_2_2ExamMaterial.objects.all()
        result_list = CSWIPWeldingInspector3_2_2_Result.objects.all()
        print("Here")
        context['result_list'] = result_list
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamResultSwip322, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = CSWIPWeldingInspector3_2_2ExamMaterial.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                result_list = CSWIPWeldingInspector3_2_2_Result.objects.all()
                context['result_list'] = result_list
                context['exam'] = exam
                return render(request, 'certificates/new_cswip_3_2_2_exam_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                exam = CSWIPWeldingInspector3_2_2ExamMaterial.objects.filter(id=self.request.POST['examID']).first()
                obj = CSWIPWeldingInspector3_2_2_Result()
                obj.event = event
                obj.candidate = candidate
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.exam = exam
                obj.general_theory_s = self.request.POST['general_theory_s']
                obj.ndt_s = self.request.POST['ndt_s']
                obj.symbols_s = self.request.POST['symbols_s']
                obj.scenario_s = self.request.POST['scenario_s']
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.remark = self.request.POST['remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()
                # if not request.POST.get('previouseID', '') == '':
                #     print("Exist")
                #     previousID = self.request.POST['previouseID'].split('-')[0]
                #     pre_result = CSWIPWeldingInspector3_1Result.objects.filter(id= previousID).first()
                #     print(pre_result)
                #
                #     repeat_obj = CSWIPWeldingInspector3_1ResultIntermadiate()
                #     repeat_obj.candidate = candidate
                #     repeat_obj.primary = pre_result
                #     repeat_obj.secondry = obj
                #     repeat_obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = CSWIPWeldingInspector3_2_2_Result.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examscwip322summary_')
            return redirect('exam_certification:examscwip322summary_')




class CSWIPExamResult322Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_cswip_3_2_2_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CSWIPExamResult322Summary, self).get_context_data()
        events = Event.objects.all()
        exams = CSWIPWeldingInspector3_2_2_Result.objects.all()
        examCount = CSWIPWeldingInspector3_2_2_Result.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context




class DeleteCSWIPExamMaterial322(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = CSWIPWeldingInspector3_2_2ExamMaterial
    success_url = reverse_lazy('exam_certification:examscwip322summary_')


class NewCSWIPExamMaterial322(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_cswip_3_2_2_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewCSWIPExamMaterial322, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewCSWIPExamMaterial322, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_cswip_3_2_2_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_cswip_3_2_2_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = CSWIPWeldingInspector3_2_2ExamMaterial()
                obj.event = event
                obj.candidate = candidate
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.customerID = self.request.POST['customerID']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                # obj.file = self.request.FILEs['file']
                obj.exam_title = self.request.POST['examTitle']
                obj.general_theory_s = self.request.POST['general_theory_s']
                obj.ndt_s = self.request.POST['ndt_s']
                obj.symbols_s = self.request.POST['symbols_s']
                obj.scenario_s = self.request.POST['scenario_s']


                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = CSWIPWeldingInspector3_2_2ExamMaterial.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/exam_material_cswip_3_2_2_summary.html',context=context)




class CSWIPExamMaterial322Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_cswip_3_2_2_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CSWIPExamMaterial322Summary, self).get_context_data()
        events = Event.objects.all()
        exams = CSWIPWeldingInspector3_2_2ExamMaterial.objects.all()
        examCount = CSWIPWeldingInspector3_2_2ExamMaterial.objects.count()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context



class DeleteCSWIPExamResult321(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = CSWIPWeldingInspector3_2_1_Result
    success_url = reverse_lazy('exam_certification:examscwip321resultsummary_')


class NewExamResultSwip321(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_cswip_3_2_1_exam_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamResultSwip321, self).get_context_data()
        exams = CSWIPWeldingInspector3_2_1ExamMaterial.objects.all()
        result_list = CSWIPWeldingInspector3_2_1_Result.objects.all()
        print("Here")
        context['result_list'] = result_list
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamResultSwip321, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = CSWIPWeldingInspector3_2_1ExamMaterial.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                result_list = CSWIPWeldingInspector3_2_1_Result.objects.all()
                context['result_list'] = result_list
                context['exam'] = exam
                return render(request, 'certificates/new_cswip_3_2_1_exam_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                exam = CSWIPWeldingInspector3_2_1ExamMaterial.objects.filter(id=self.request.POST['examID']).first()
                obj = CSWIPWeldingInspector3_2_1_Result()
                obj.event = event
                obj.candidate = candidate
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.exam = exam
                obj.general_theory_s = self.request.POST['general_theory_s']
                obj.ndt_s = self.request.POST['ndt_s']
                obj.symbols_s = self.request.POST['symbols_s']
                obj.scenario_s = self.request.POST['scenario_s']
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.remark = self.request.POST['remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()
                # if not request.POST.get('previouseID', '') == '':
                #     print("Exist")
                #     previousID = self.request.POST['previouseID'].split('-')[0]
                #     pre_result = CSWIPWeldingInspector3_1Result.objects.filter(id= previousID).first()
                #     print(pre_result)
                #
                #     repeat_obj = CSWIPWeldingInspector3_1ResultIntermadiate()
                #     repeat_obj.candidate = candidate
                #     repeat_obj.primary = pre_result
                #     repeat_obj.secondry = obj
                #     repeat_obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = CSWIPWeldingInspector3_2_1_Result.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examscwip321resultsummary_')
            return redirect('exam_certification:examscwip321resultsummary_')





class CSWIPExamResult321Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_cswip_3_2_1_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CSWIPExamResult321Summary, self).get_context_data()
        events = Event.objects.all()
        exams = CSWIPWeldingInspector3_2_1_Result.objects.all()
        examCount = CSWIPWeldingInspector3_2_1_Result.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context



class DeleteCSWIPExamMaterial321(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = CSWIPWeldingInspector3_2_1ExamMaterial
    success_url = reverse_lazy('exam_certification:examscwip321summary_')

class NewCSWIPExamMaterial321(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_cswip_3_2_1_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewCSWIPExamMaterial321, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewCSWIPExamMaterial321, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_cswip_3_2_1_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_cswip_3_2_1_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = CSWIPWeldingInspector3_2_1ExamMaterial()
                obj.event = event
                obj.candidate = candidate
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.customerID = self.request.POST['customerID']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                # obj.file = self.request.FILEs['file']
                obj.exam_title = self.request.POST['examTitle']
                obj.general_theory_s = self.request.POST['general_theory_s']
                obj.ndt_s = self.request.POST['ndt_s']
                obj.symbols_s = self.request.POST['symbols_s']
                obj.scenario_s = self.request.POST['scenario_s']


                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = CSWIPWeldingInspector3_2_1ExamMaterial.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/exam_material_cswip_3_2_1_summary.html',context=context)





class CSWIPExamMaterial321Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_cswip_3_2_1_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CSWIPExamMaterial321Summary, self).get_context_data()
        events = Event.objects.all()
        exams = CSWIPWeldingInspector3_2_1ExamMaterial.objects.all()
        examCount = CSWIPWeldingInspector3_2_1ExamMaterial.objects.count()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context


class ExamCSWIP31ResultSummaryByID(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/cswip_31_exam_result_byID.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamCSWIP31ResultSummaryByID, self).get_context_data()
        print(self.kwargs['id'])
        exam = CSWIPWeldingInspector3_1Result.objects.filter(id=self.kwargs['id']).first()
        finalResult =None
        final_deadline_date =None
        action=None
        re_exams =""
        remark =''
        #
        if exam.general_paper == 'Failed'  or exam.technology_paper == 'Failed'  or exam.plate_paper == 'Failed'   or exam.pipe_paper == 'Failed'   or exam.macro_paper == 'Failed'    :
            finalResult = "Failed"
            final_deadline_date = exam.event.start_exam_date + relativedelta(months=+12)
            second_email_date = exam.event.start_exam_date + relativedelta(months=+6)
            third_email_date = exam.event.start_exam_date + relativedelta(months=+10)
            action='Re-test'
        else:
            finalResult = "Passed"

            second_email_date = exam.event.start_exam_date + relativedelta(months=+54)
            third_email_date = exam.event.start_exam_date + relativedelta(months=+114)
            action = 'Renewal'

        if exam.general_paper == 'Failed':
            remark ='Candidate can participate to General Paper re-exam once,'
        if exam.technology_paper == 'Failed':
            remark = remark + str('Candidate can participate to Technology Paper re-exam once,')
        if exam.plate_paper == 'Failed':
            remark = remark +  str('Candidate can participate to Plant Paper re-exam two time,')
        if exam.pipe_paper == 'Failed':
            remark = remark +  str('Candidate can participate to Pipe Paper re-exam two time,')
        if exam.macro_paper == 'Failed':
            remark = remark +  str('Candidate can participate to Macro Paper re-exam two time,')



        #
        # if exam.cswip_pcn == 'CSWIP':
        #     if exam.general_theory == 'Failed' :
        #         re_exams = "General Theory,"
        #     if exam.specific_theory == 'Failed' :
        #         re_exams = str(re_exams) + "Specific Theory,"
        #     if exam.sample1_analysis == 'Failed'  :
        #         re_exams = str(re_exams) + "Sample1 data Analysis,"
        #     if exam.sample1_collection == 'Failed'  :
        #         re_exams = str(re_exams) + "Sample1 data Collection,"
        #     if exam.sample2_analysis == 'Failed' :
        #         re_exams = str(re_exams) + "Sample2 data Analysis,"
        #     if exam.sample2_collection == 'Failed'  :
        #         re_exams = str(re_exams) + "Sample2 data Collection,"
        #     if exam.sample3_analysis == 'Failed'  :
        #         re_exams = str(re_exams) + "Sample3 data Analysis,"
        #     if exam.sample3_collection == 'Failed'  :
        #         re_exams = str(re_exams) + "Sample3 data Collection,"
        #     if exam.written_instruction == 'Failed' :
        #         re_exams = str(re_exams) + "Written data Instruction,"
        #
        # elif exam.cswip_pcn == 'PCN':
        #     if exam.general_theory == 'Failed'  or exam.specific_theory == 'Failed'  :
        #         re_exams = "General Theory,Specific Theory"
        #     elif exam.sample1_analysis == 'Failed'  or exam.sample1_collection == 'Failed'  or exam.sample2_analysis== 'Failed'  or exam.sample2_collection == 'Failed'  or exam.sample3_collection == 'Failed'  or exam.sample3_analysis == 'Failed'  or exam.written_instruction == 'Failed'  :
        #         re_exams = str(
        #             re_exams) + "Sample1 data Analysis,Sample1 data Collection,Sample2 data Analysis,Sample2 data Collection,Sample3 data Analysis,Sample3 data Collection,Written data Instruction"


        repeat_list = CSWIPWeldingInspector3_1ResultIntermadiate.objects.filter(candidate = exam.candidate)
        repeat_first = CSWIPWeldingInspector3_1Result.objects.filter(id=repeat_list.first().primary.id).first()
        print(repeat_list)
        print(repeat_list.count())
        print("Here")
        for item in repeat_list:
            print(item.secondry.id)
        print("Here")
        # result_list = CSWIPWeldingInspector3_1Result.objects.filter(id=repeat_obj)
        # result_list = repeat_obj

        print(repeat_list)

        context['repeat_list'] = repeat_list
        context['repeat_first'] = repeat_first
        context['exam'] = exam
        context['finalResult'] = finalResult
        # context['re_exams'] = re_exams
        context['final_deadline_date'] = final_deadline_date
        context['second_email_date'] = second_email_date
        context['third_email_date'] = third_email_date
        context['action'] = action
        context['remark'] = remark

        return context



class DeleteCSWIPExamResult31(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = CSWIPWeldingInspector3_1Result
    success_url = reverse_lazy('exam_certification:examscwip31resultsummary_')


class NewExamResultSwip31(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_cswip_31_exam_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamResultSwip31, self).get_context_data()
        exams = CSWIPWeldingInspector3_1ExamMaterial.objects.all()
        result_list = CSWIPWeldingInspector3_1Result.objects.all()
        print("Here")
        context['result_list'] = result_list
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamResultSwip31, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = CSWIPWeldingInspector3_1ExamMaterial.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                result_list = CSWIPWeldingInspector3_1Result.objects.all()
                context['result_list'] = result_list
                context['exam'] = exam
                return render(request, 'certificates/new_cswip_31_exam_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                exam = CSWIPWeldingInspector3_1ExamMaterial.objects.filter(id=self.request.POST['examID']).first()
                obj = CSWIPWeldingInspector3_1Result()
                obj.event = event
                obj.candidate = candidate
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.exam = exam
                obj.general_paper = self.request.POST['general_paper']
                obj.technology_paper = self.request.POST['technology_paper']
                obj.plate_paper = self.request.POST['plate_paper']
                obj.pipe_paper = self.request.POST['pipe_paper']
                obj.macro_paper = self.request.POST['macro_paper']
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.remark = self.request.POST['remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()
                if not request.POST.get('previouseID', '') == '':
                    print("Exist")
                    previousID = self.request.POST['previouseID'].split('-')[0]
                    pre_result = CSWIPWeldingInspector3_1Result.objects.filter(id= previousID).first()
                    print(pre_result)

                    repeat_obj = CSWIPWeldingInspector3_1ResultIntermadiate()
                    repeat_obj.candidate = candidate
                    repeat_obj.primary = pre_result
                    repeat_obj.secondry = obj
                    repeat_obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = CSWIPWeldingInspector3_1Result.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examscwip31resultsummary_')
            return redirect('exam_certification:examscwip31resultsummary_')



class CSWIPExamResult31Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_cswip_31_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CSWIPExamResult31Summary, self).get_context_data()
        events = Event.objects.all()
        exams = CSWIPWeldingInspector3_1Result.objects.all()
        examCount = CSWIPWeldingInspector3_1Result.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context



class DeleteCSWIPExamMaterial31(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = CSWIPWeldingInspector3_1ExamMaterial
    success_url = reverse_lazy('exam_certification:examscwip31summary_')


class CSWIPExamMaterial31Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_cswip_31_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CSWIPExamMaterial31Summary, self).get_context_data()
        events = Event.objects.all()
        exams = CSWIPWeldingInspector3_1ExamMaterial.objects.all()
        examCount = CSWIPWeldingInspector3_1ExamMaterial.objects.count()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context


class NewCSWIPExamMaterial31(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_cswip_31_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewCSWIPExamMaterial31, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewCSWIPExamMaterial31, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)


                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_cswip_31_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_cswip_31_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = CSWIPWeldingInspector3_1ExamMaterial()
                obj.event = event
                obj.candidate = candidate
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.examTitle = self.request.POST['examTitle']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                # obj.file = self.request.FILEs['file']
                obj.exam_title = self.request.POST['examTitle']
                obj.general_paper = self.request.POST['general_paper']
                obj.technology_paper = self.request.POST['technology_paper']
                obj.plate_paper = self.request.POST['plate_paper']

                obj.pipe_paper = self.request.POST['pipe_paper']
                obj.macro_paper = self.request.POST['macro_paper']

                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = CSWIPWeldingInspector3_1ExamMaterial.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/exam_material_cswip_31_summary.html',context=context)




class DeleteExamTofdL3Material(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = ExamMaterialTofdL3
    success_url = reverse_lazy('exam_certification:examtofdl3summary_')


class ExamMaterialTofdL3IMSForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/tofd_l3_ims_form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamMaterialTofdL3IMSForm, self).get_context_data()
        form =ExamMaterialTofdL3.objects.filter(id=self.kwargs['id']).first()
        context['form'] = form
        return context





class NewExamMaterialTofdL3(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_tofd_l3_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialTofdL3, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialTofdL3, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_tofd_l3_material.html', context)


            elif 'submit_tofd' in request.POST:
                print("Submit TOFD")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialTofdL3()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['customerID']


                obj.tofd_scheme = self.request.POST['tofd_scheme']
                if not request.POST.get('tofd_exam_date', '') == '':
                    obj.tofd_exam_date = datetime.datetime.strptime(self.request.POST['tofd_exam_date'], '%m/%d/%Y')
                obj.tofd_ndtl3 = self.request.POST['tofd_ndtl3']
                obj.tofd_pautl2 = self.request.POST['tofd_pautl2']
                obj.tofd_practical_exam = self.request.POST['tofd_practical_exam']
                obj.tofd_basic_a1 = self.request.POST['tofd_basic_a1']
                obj.tofd_basic_a2 = self.request.POST['tofd_basic_a2']
                obj.tofd_basic_b_part_1 = self.request.POST['tofd_basic_b_part_1']
                obj.tofd_basic_b_part_2 = self.request.POST['tofd_basic_b_part_2']
                obj.tofd_basic_b_part_3 = self.request.POST['tofd_basic_b_part_3']
                obj.tofd_basic_b_part_4 = self.request.POST['tofd_basic_b_part_4']
                obj.tofd_main_c_1 = self.request.POST['tofd_main_c_1']
                obj.tofd_main_c_2 = self.request.POST['tofd_main_c_2']
                obj.tofd_main_c_3 = self.request.POST['tofd_main_c_3']
                obj.tofd_delivery_method = self.request.POST['tofd_delivery_method']
                obj.tofd_lecturer = self.request.POST['tofd_lecturer']
                obj.tofd_invigilator = self.request.POST['tofd_invigilator']
                obj.tofd_venue = self.request.POST['tofd_venue']
                obj.tofd_remark = self.request.POST['tofd_remarks']

                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialTofdL3.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                return redirect('exam_certification:examtofdl3summary_')
            elif 'submit_pcn_tofd' in request.POST:
                print("Submit PCN TOFD")
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialTofdL3()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['pcn_tofd_l3_customerID']
                obj.pcn_tofd_l3_scheme = self.request.POST['pcn_tofd_l3_scheme']
                if not request.POST.get('pcn_tofd_l3_exam_date', '') == '':
                    obj.pcn_tofd_l3_exam_date = datetime.datetime.strptime(self.request.POST['pcn_tofd_l3_exam_date'], '%m/%d/%Y')
                obj.pcn_tofd_l3_ndtl3 = self.request.POST['pcn_tofd_l3_ndtl3']
                obj.pcn_tofd_l3_pautl2 = self.request.POST['pcn_tofd_l3_pautl2']
                obj.pcn_tofd_l3_practical_exam = self.request.POST['pcn_tofd_l3_practical_exam']
                obj.pcn_tofd_l3_basic_a1 = self.request.POST['pcn_tofd_l3_basic_a1']
                obj.pcn_tofd_l3_basic_a2 = self.request.POST['pcn_tofd_l3_basic_a2']
                obj.pcn_tofd_l3_basic_b_part_1 = self.request.POST['pcn_tofd_l3_basic_b_part_1']
                obj.pcn_tofd_l3_basic_b_part_2 = self.request.POST['pcn_tofd_l3_basic_b_part_2']
                obj.pcn_tofd_l3_basic_b_part_3 = self.request.POST['pcn_tofd_l3_basic_b_part_3']
                obj.pcn_tofd_l3_basic_b_part_4 = self.request.POST['pcn_tofd_l3_basic_b_part_4']
                obj.pcn_tofd_l3_main_d = self.request.POST['pcn_tofd_l3_main_d']
                obj.pcn_tofd_l3_main_e = self.request.POST['pcn_tofd_l3_main_e']
                obj.pcn_tofd_l3_main_f = self.request.POST['pcn_tofd_l3_main_f']
                obj.pcn_tofd_l3_delivery_method = self.request.POST['pcn_tofd_l3_delivery_method']
                obj.pcn_tofd_l3_lecturer = self.request.POST['pcn_tofd_l3_lecturer']
                obj.pcn_tofd_l3_invigilator = self.request.POST['pcn_tofd_l3_invigilator']
                obj.pcn_tofd_l3_venue = self.request.POST['pcn_tofd_l3_venue']
                obj.pcn_tofd_l3_remark = self.request.POST['pcn_tofd_l3_remark']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialTofdL3.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                return redirect('exam_certification:examtofdl3summary_')

                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialPAUTL2.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                return redirect('exam_certification:examl3summary_')
        # return render(request, 'certificates/exam_material_l3_summary.html',context=context)
        return redirect('exam_certification:examtofdl3summary_')





class ExamMaterialTofdL3Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_tofd_l3_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamMaterialTofdL3Summary, self).get_context_data()
        events = Event.objects.all()
        exams = ExamMaterialTofdL3.objects.all()
        examCount = ExamMaterialTofdL3.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context




class NewExamResultPautL2(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_paut_l2_exam_result.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamResultPautL2, self).get_context_data()
        exams = ExamMaterialPAUTL2.objects.all()
        candidates = TesCandidate.objects.all()
        context['exams'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamResultPautL2, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(request.POST['examID'])
                exam = ExamMaterialPAUTL2.objects.filter(id=self.request.POST['examID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                context['exam'] = exam

                return render(request, 'certificates/new_paut_l2_exam_result.html', context)
            elif 'submit' in request.POST:
                print("Submit")


                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()
                exam = ExamMaterialPAUTL2.objects.filter(id=self.request.POST['examID']).first()
                obj = ExamResultPautL2()
                obj.event = event
                obj.candidate = candidate
                obj.exam = exam
                # obj.result = self.request.POST['result']
                # obj.explanation = self.request.POST['explanation']
                obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.general_theory = self.request.POST['general_theory']
                obj.specific_theory = self.request.POST['specific_theory']
                obj.sample1_analysis = self.request.POST['sample1_analysis']
                obj.sample1_collection = self.request.POST['sample1_collection']
                obj.sample2_analysis = self.request.POST['sample2_analysis']
                obj.sample2_collection = self.request.POST['sample2_collection']
                obj.sample3_analysis = self.request.POST['sample3_analysis']
                obj.sample3_collection = self.request.POST['sample3_collection']
                obj.written_instruction = self.request.POST['written_instruction']
                obj.remark = self.request.POST['remarks']
                if bool(request.FILES.get('myFile', False)) == True:
                    obj.file = self.request.FILES['myFile']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamResultPautL2.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examresultsummary_')
            return redirect('exam_certification:examresultsummary_')


class ExamResultSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_result_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamResultSummary, self).get_context_data()
        events = Event.objects.all()
        exams = ExamResultPautL2.objects.all()
        examCount = ExamResultPautL2.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context



class ExamResultSummaryByID(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/paut_l2_exam_result_byID.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamResultSummaryByID, self).get_context_data()
        print(self.kwargs['id'])
        exam = ExamResultPautL2.objects.filter(id=self.kwargs['id']).first()
        finalResult =None
        final_deadline_date =None
        action=None
        re_exams =""

        if exam.general_theory == 'Failed'  or exam.specific_theory == 'Failed'  or exam.sample1_analysis == 'Failed'   or exam.sample1_collection == 'Failed'   or exam.sample2_analysis == 'Failed'  or exam.sample2_collection == 'Failed'   or exam.sample3_analysis == 'Failed'   or exam.sample3_collection == 'Failed'  or exam.written_instruction == 'Failed'  :
            finalResult = "Failed"
            final_deadline_date = exam.event.start_exam_date + relativedelta(months=+12)
            second_email_date = exam.event.start_exam_date + relativedelta(months=+6)
            third_email_date = exam.event.start_exam_date + relativedelta(months=+10)
            action='Re-test'
        else:
            finalResult = "Passed"

            second_email_date = exam.event.start_exam_date + relativedelta(months=+54)
            third_email_date = exam.event.start_exam_date + relativedelta(months=+114)
            action = 'Renewal'


        if exam.cswip_pcn == 'CSWIP':
            if exam.general_theory == 'Failed' :
                re_exams = "General Theory,"
            if exam.specific_theory == 'Failed' :
                re_exams = str(re_exams) + "Specific Theory,"
            if exam.sample1_analysis == 'Failed'  :
                re_exams = str(re_exams) + "Sample1 data Analysis,"
            if exam.sample1_collection == 'Failed'  :
                re_exams = str(re_exams) + "Sample1 data Collection,"
            if exam.sample2_analysis == 'Failed' :
                re_exams = str(re_exams) + "Sample2 data Analysis,"
            if exam.sample2_collection == 'Failed'  :
                re_exams = str(re_exams) + "Sample2 data Collection,"
            if exam.sample3_analysis == 'Failed'  :
                re_exams = str(re_exams) + "Sample3 data Analysis,"
            if exam.sample3_collection == 'Failed'  :
                re_exams = str(re_exams) + "Sample3 data Collection,"
            if exam.written_instruction == 'Failed' :
                re_exams = str(re_exams) + "Written data Instruction,"

        elif exam.cswip_pcn == 'PCN':
            if exam.general_theory == 'Failed'  or exam.specific_theory == 'Failed'  :
                re_exams = "General Theory,Specific Theory"
            elif exam.sample1_analysis == 'Failed'  or exam.sample1_collection == 'Failed'  or exam.sample2_analysis== 'Failed'  or exam.sample2_collection == 'Failed'  or exam.sample3_collection == 'Failed'  or exam.sample3_analysis == 'Failed'  or exam.written_instruction == 'Failed'  :
                re_exams = str(
                    re_exams) + "Sample1 data Analysis,Sample1 data Collection,Sample2 data Analysis,Sample2 data Collection,Sample3 data Analysis,Sample3 data Collection,Written data Instruction"

        import datetime


        context['exam'] = exam
        context['finalResult'] = finalResult
        context['re_exams'] = re_exams
        context['final_deadline_date'] = final_deadline_date
        context['second_email_date'] = second_email_date
        context['third_email_date'] = third_email_date
        context['action'] = action

        return context




class DeleteExamL3Material(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = ExamMaterialL3
    success_url = reverse_lazy('exam_certification:examl3summary_')



class ExamMaterialL3IMSForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/l3_ims_form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamMaterialL3IMSForm, self).get_context_data()
        form =ExamMaterialL3.objects.filter(id=self.kwargs['id']).first()
        context['form'] = form
        return context


class NewExamMaterialL3(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_l3_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialL3, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialL3, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_l3_material.html', context)
            elif 'submit_paut' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialL3()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['customerID']
                obj.paut_scheme = self.request.POST['paut_scheme']
                if not request.POST.get('paut_exam_date', '') == '':
                    obj.exam_date = datetime.datetime.strptime(self.request.POST['paut_exam_date'], '%m/%d/%Y')
                obj.paut_ndtl3 = self.request.POST['paut_ndtl3']
                obj.paut_pautl2 = self.request.POST['paut_pautl2']
                obj.paut_practical_exam = self.request.POST['paut_practical_exam']
                obj.paut_basic_a1 = self.request.POST['paut_basic_a1']
                obj.paut_basic_a2 = self.request.POST['paut_basic_a2']
                obj.paut_basic_b_part_1 = self.request.POST['paut_basic_b_part_1']
                obj.paut_basic_b_part_2 = self.request.POST['paut_basic_b_part_2']
                obj.paut_basic_b_part_3 = self.request.POST['paut_basic_b_part_3']
                obj.paut_basic_b_part_4 = self.request.POST['paut_basic_b_part_4']
                obj.paut_main_c_1 = self.request.POST['paut_main_c_1']
                obj.paut_main_c_2 = self.request.POST['paut_main_c_2']
                obj.paut_main_c_3 = self.request.POST['paut_main_c_3']
                obj.paut_delivery_method = self.request.POST['paut_delivery_method']
                obj.paut_lecturer = self.request.POST['paut_lecturer']
                obj.paut_invigilator = self.request.POST['paut_invigilator']
                obj.paut_venue = self.request.POST['paut_venue']
                obj.paut_remark = self.request.POST['paut_remarks']
                obj.save()
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialPAUTL2.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_material_l3_summary.html', context=context)
                return redirect('exam_certification:examl3summary_')


            elif 'submit_pcn_paut' in request.POST:
                print("Submit PCN PAUT")
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialL3()
                obj.event = event
                obj.candidate = candidate
                obj.customerID = self.request.POST['pcn_paut_l3_customerID']
                obj.pcn_paut_l3_scheme = self.request.POST['pcn_paut_l3_scheme']
                if not request.POST.get('pcn_paut_exam_l3_date', '') == '':
                    obj.pcn_paut_l3_exam_date = datetime.datetime.strptime(self.request.POST['pcn_paut_exam_l3_date'], '%m/%d/%Y')
                obj.pcn_paut_l3_ndtl3 = self.request.POST['pcn_paut_l3_ndtl3']
                obj.pcn_paut_l3_pautl2 = self.request.POST['pcn_paut_l3_pautl2']
                obj.pcn_paut_l3_practical_exam = self.request.POST['pcn_paut_l3_practical_exam']
                obj.pcn_paut_l3_basic_a1 = self.request.POST['pcn_paut_l3_basic_a1']
                obj.pcn_paut_l3_basic_a2 = self.request.POST['pcn_paut_l3_basic_a2']
                obj.pcn_paut_l3_basic_b_part_1 = self.request.POST['pcn_paut_l3_basic_b_part_1']
                obj.pcn_paut_l3_basic_b_part_2 = self.request.POST['pcn_paut_l3_basic_b_part_2']
                obj.pcn_paut_l3_basic_b_part_3 = self.request.POST['pcn_paut_l3_basic_b_part_3']
                obj.pcn_paut_l3_basic_b_part_4 = self.request.POST['pcn_paut_l3_basic_b_part_4']
                obj.pcn_paut_l3_main_d = self.request.POST['pcn_paut_l3_main_d']
                obj.pcn_paut_l3_main_e = self.request.POST['pcn_paut_l3_main_e']
                obj.pcn_paut_l3_main_f = self.request.POST['pcn_paut_l3_main_f']
                obj.pcn_paut_l3_delivery_method = self.request.POST['pcn_paut_l3_delivery_method']
                obj.pcn_paut_l3_lecturer = self.request.POST['pcn_paut_l3_lecturer']
                obj.pcn_paut_l3_invigilator = self.request.POST['pcn_paut_l3_invigilator']
                obj.pcn_paut_l3_venue = self.request.POST['pcn_paut_l3_venue']
                obj.pcn_paut_l3_remark = self.request.POST['pcn_paut_l3_remark']
                obj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialPAUTL2.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                return redirect('exam_certification:examl3summary_')
        # return render(request, 'certificates/exam_material_l3_summary.html',context=context)



class ExamMaterialL3Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_l3_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamMaterialL3Summary, self).get_context_data()
        events = Event.objects.all()
        exams = ExamMaterialL3.objects.all()
        examCount = ExamMaterialL3.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context






class DeleteExamPAUTL2(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = ExamMaterialPAUTL2
    success_url = reverse_lazy('exam_certification:exampautl2summary_')


class ExamMaterialPAUTL2Summary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_PAUTL2_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamMaterialPAUTL2Summary, self).get_context_data()
        events = Event.objects.all()
        exams = ExamMaterialPAUTL2.objects.all()
        examCount = ExamMaterialPAUTL2.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context



class NewExamMaterialPautl2ByID(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_pautl2_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialPautl2ByID, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialPautl2ByID, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_pautl2_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialPAUTL2()
                obj.event = event
                obj.candidate = candidate
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                # obj.exam_revision = self.request.POST['revision']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.general_theory = self.request.POST['general_theory']
                obj.specific_theory = self.request.POST['specific_theory']
                obj.sample1_analysis = self.request.POST['sample1_analysis']
                obj.sample1_collection = self.request.POST['sample1_collection']
                obj.sample2_analysis = self.request.POST['sample2_analysis']
                obj.sample2_collection = self.request.POST['sample2_collection']
                obj.sample3_analysis = self.request.POST['sample3_analysis']
                obj.sample3_collection = self.request.POST['sample3_collection']
                obj.written_instruction = self.request.POST['written_instruction']
                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialPAUTL2.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/exam_material_PAUTL2_summary.html',context=context)



class NewExamMaterialPautl2(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_pautl2_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialPautl2, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialPautl2, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_pautl2_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialPAUTL2()
                obj.event = event
                obj.candidate = candidate
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.examTitle = self.request.POST['examTitle']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.exam_title = self.request.POST['examTitle']
                print(self.request.POST['general_theory'])
                sample1 = Samples.objects.filter(id=self.request.POST['general_theory']).first()
                obj.general_theory = sample1
                sample2 = Samples.objects.filter(id=self.request.POST['specific_theory']).first()
                obj.specific_theory = sample2
                sample3 = Samples.objects.filter(id=self.request.POST['sample1_analysis']).first()
                obj.sample1_analysis = sample3
                sample4 = Samples.objects.filter(id=self.request.POST['sample1_collection']).first()
                obj.sample1_collection = sample4
                sample5 = Samples.objects.filter(id=self.request.POST['sample2_analysis']).first()
                obj.sample2_analysis = sample5
                sample6 = Samples.objects.filter(id=self.request.POST['sample2_collection']).first()
                obj.sample2_collection = sample6
                sample7 = Samples.objects.filter(id=self.request.POST['sample3_analysis']).first()
                obj.sample3_analysis = sample7
                sample8 = Samples.objects.filter(id=self.request.POST['sample3_collection']).first()
                obj.sample3_collection = sample8
                sample9 = Samples.objects.filter(id=self.request.POST['written_instruction']).first()
                obj.written_instruction = sample9
                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialPAUTL2.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/exam_material_PAUTL2_summary.html',context=context)


class DeleteExamTofd(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = ExamMaterialTOFDModel1
    success_url = reverse_lazy('exam_certification:examtofdsummary_')



class NewExamMaterialTofd(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_tofd_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialTofd, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        samples =Samples.objects.all()
        context['samples'] = samples
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialTofd, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                events = Event.objects.filter(candidate=candidate)

                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = candidate

                return render(request, 'certificates/new_tofd_material.html', context)

            elif 'updateInfo-event' in request.POST:
                print("updateInfo event")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                # candidates = TesCandidate.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['candidate'] = TesCandidate.objects.filter(
                    id=self.request.POST['candidate_inner_ID'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_tofd_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialTOFDModel1()
                obj.event = event
                obj.candidate = candidate
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                # obj.exam_revision = self.request.POST['revision']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                obj.exam_title = self.request.POST['examTitle']
                # obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.general_theory = self.request.POST['general_theory']
                obj.specific_theory = self.request.POST['specific_theory']
                sample = Samples.objects.filter(id=self.request.POST['sample1']).first()
                obj.sample1 = sample
                sample = Samples.objects.filter(id=self.request.POST['sample2']).first()
                obj.sample2 = sample
                sample = Samples.objects.filter(id=self.request.POST['data_file_1']).first()
                obj.data_file_1 = sample
                sample = Samples.objects.filter(id=self.request.POST['data_file_2']).first()
                obj.data_file_2 = sample
                sample = Samples.objects.filter(id=self.request.POST['data_file_3']).first()
                obj.data_file_3 = sample
                sample = Samples.objects.filter(id=self.request.POST['data_file_4']).first()
                obj.data_file_4 = sample
                # sample = Samples.objects.filter(id=self.request.POST['data_file_5']).first()
                # obj.data_file_5 = sample
                sample =Samples.objects.filter(id=self.request.POST['written_instruction']).first()
                obj.written_instruction = sample
                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialTOFDModel1.objects.all()
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/exam_material_tofd_summary.html',context=context)


class ExamMaterialTofdSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_tofd_result_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamMaterialTofdSummary, self).get_context_data()
        events = Event.objects.all()
        exams = ExamMaterialTOFDModel1.objects.all()
        examCount = ExamMaterialTOFDModel1.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context

class NewExamMaterialPiWi(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_piwi_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialPiWi, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialPiWi, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo")
                print(self.request.POST['event'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event.id)
                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                context['event'] = event

                return render(request, 'certificates/new_piwi_material.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                obj = ExamMaterialPiWiModel()
                obj.event = event
                obj.candidate = candidate
                obj.exam_date = datetime.datetime.strptime(self.request.POST['exam_date'], '%m/%d/%Y')
                obj.exam_revision = self.request.POST['revision']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialPiWiModel.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/exam_material_piwi_summary.html',context=context)


class DeleteExamPiWi(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = ExamMaterialPiWiModel
    success_url = reverse_lazy('exam_certification:exampiwisummary_')


class ExamMaterialPiWiSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_piwi_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamMaterialPiWiSummary, self).get_context_data()
        events = Event.objects.all()
        exams = ExamMaterialPiWiModel.objects.all()
        examCount = ExamMaterialPiWiModel.objects.count()
        context['events'] = events
        context['exams'] = exams
        context['examCount'] = examCount
        return context

class ExamMaterialPiWi(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_pi_wi.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ExamMaterialPiWi, self).get_context_data()
        exams = ExamMaterialPiWiModel.objects.all()
        context['exams'] = exams
        return context




class CSWIPCertificateSummayView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/cswip_cer_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CSWIPCertificateSummayView, self).get_context_data()
        certificates = CSWIPCertificateAttendance.objects.all()
        cerCount = CSWIPCertificateAttendance.objects.count()
        context['certificates'] = certificates
        context['cerCount'] = cerCount
        return context

class NewCswipCertificateAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_cswip_candidate.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewCswipCertificateAttendance, self).get_context_data()
        candidates = TesCandidate.objects.all()
        products = CswipCertificateProduct.objects.all()
        context['candidates'] = candidates
        context['products'] = products
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':

            print("Form was sent!")
            print(self.request.POST['candidate'].split('-')[0])
            candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
            product = CswipCertificateProduct.objects.filter(id=self.request.POST['product']).first()

            obj = CSWIPCertificateAttendance()
            obj.candidate = candidate
            obj.name = candidate.first_name + " " + candidate.last_name
            obj.file = self.request.FILES['file']
            obj.product = product
            obj.save()


        return redirect('exam_certification:swipcersummary_')

class DeleteCswipCertificate(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = CSWIPCertificateAttendance
    success_url = reverse_lazy('exam_certification:swipcersummary_')


class PCNCertificateSummayView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/pcn_cer_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PCNCertificateSummayView, self).get_context_data()
        certificates = PcnCertificateAttendance.objects.all()
        cerCount = PcnCertificateAttendance.objects.count()
        context['certificates'] = certificates
        context['cerCount'] = cerCount
        return context


class NewPcnCertificateAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_pcn_candidate.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewPcnCertificateAttendance, self).get_context_data()
        candidates = TesCandidate.objects.all()
        products = PcnCertificateProduct.objects.all()
        context['candidates'] = candidates
        context['products'] = products
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':

            print("Form was sent!")
            print(self.request.POST['candidate'].split('-')[0])
            candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
            product = PcnCertificateProduct.objects.filter(id=self.request.POST['product']).first()
            print(product)
            obj = PcnCertificateAttendance()
            obj.candidate = candidate
            obj.name = candidate.first_name + " " + candidate.last_name
            obj.file = self.request.FILES['file']
            obj.product = product
            obj.save()


        return redirect('exam_certification:pcncersummary_')



class DeletePcnCertificate(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = PcnCertificateAttendance
    success_url = reverse_lazy('exam_certification:pcncersummary_')


class CertificateAttendanceView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/cer_attendance.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CertificateAttendanceView, self).get_context_data()
        # certificateType = CertificateType.objects.all()
        # context['certificateType'] = certificateType
        return context

class FinalCertificateAttendanceView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/certificate_of_attendance.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FinalCertificateAttendanceView, self).get_context_data()
        candidate = TesCandidate.objects.filter(id=self.kwargs['canID']).first()
        event = Event.objects.filter(id=self.kwargs['eventID']).first()
        form = CertificateAttendance.objects.filter(Q(candidate=candidate) & Q(event=event)).first()
        print(form)
        context['form'] = form
        return context
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print('uploadFormBack')
            candidate = TesCandidate.objects.filter(id=self.kwargs['canID']).first()
            event = Event.objects.filter(id=self.kwargs['eventID']).first()
            obj = CertificateAttendance.objects.filter(Q(candidate=candidate) & Q(event=event)).first()
            obj.file = request.FILES['pdfFile']
            obj.save()
        return redirect('exam_certification:cersummary_')

class NewCertificateAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_attendance.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewCertificateAttendance, self).get_context_data()
        candidates = TesCandidate.objects.all()
        events = Event.objects.all()
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':

            print("Form was sent!")
            print(self.request.POST['candidate'].split('-')[0])
            candidate = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()

            event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
            # if CertificateAttendance.objects.filter(Q(candidate=candidate) & Q(event=event)).count() > 0:
            #     obj = CertificateAttendance.objects.filter(Q(candidate=candidate) & Q(event=event)).first()
            #     obj.candidate = candidate
            #     obj.event = event
            #     obj.name = candidate.first_name + " " + candidate.last_name
            #     obj.authorized_signatory = self.request.POST['authorized_signatory']
            #     obj.course_duration = self.request.POST['course_duration']
            #     obj.cer_number = self.request.POST['certiﬁcate_number']
            #     obj.issue_date = datetime.datetime.strptime(self.request.POST['issue_date'], '%m/%d/%Y')
            #     obj.save()
            # else:
            obj = CertificateAttendance()
            obj.candidate = candidate
            obj.event = event
            obj.name = candidate.first_name + " " + candidate.last_name
            obj.authorized_signatory = "Tahir Rizwan"
            if not request.POST.get('course_duration', '') == '':
                obj.course_duration = self.request.POST['course_duration']
            obj.cer_number = self.request.POST['certiﬁcate_number']
            # if not request.FILES.get('file', None) == None:
            # if request.FILES.get('myFile', True):
            if bool(request.FILES.get('myFile', False)) == True:
                obj.file = self.request.FILES['myFile']
            if not request.POST.get('issue_date', '') == '':
                obj.issue_date = datetime.datetime.strptime(self.request.POST['issue_date'], '%m/%d/%Y')
            obj.save()

        return redirect('exam_certification:cersummary_')


class DeleteCertificateAttendance(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = CertificateAttendance
    success_url = reverse_lazy('exam_certification:cersummary_')

class CertificateSummayView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/cer_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CertificateSummayView, self).get_context_data()
        certificateAttendances = CertificateAttendance.objects.all()
        cerCount = CertificateAttendance.objects.count()
        context['certificateAttendances'] = certificateAttendances
        context['cerCount'] = cerCount
        return context
