from django.shortcuts import render, redirect
from exam_certification.models import (CertificateAttendance,ExamMaterialL3,ExamMaterialPAUTL2,ExamMaterialTOFDModel1,
                                       PcnCertificateAttendance,CSWIPCertificateAttendance,PcnCertificateProduct,
                                       CswipCertificateProduct,ExamMaterialPiWiModel,ExamResultPautL2,ExamMaterialTofdL3 )

from training.models import TesCandidate
from django.contrib.auth.mixins import LoginRequiredMixin
from authorization.sidebarmixin import SidebarMixin
from django.views.generic import View, TemplateView
from training.models import TesCandidate,Event
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from dateutil.relativedelta import *
from django.db.models import Q
import datetime
# Create your views here.


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
                obj = ExamResultPautL2()
                obj.event = event
                obj.candidate = candidate
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
                    obj.paut_exam_date = datetime.datetime.strptime(self.request.POST['paut_exam_date'], '%m/%d/%Y')
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


class DeleteExamTofd(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = ExamMaterialTOFDModel1
    success_url = reverse_lazy('exam_certification:examtofdsummary_')



class NewExamMaterialTofd(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_tofd_material.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewExamMaterialTofd, self).get_context_data()
        events = Event.objects.all()
        candidates =TesCandidate.objects.all()
        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewExamMaterialTofd, self).get_context_data()
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
                obj.exam_revision = self.request.POST['revision']
                obj.lecturer = self.request.POST['lecturer']
                obj.invigilator = self.request.POST['invigilator']
                obj.remark = self.request.POST['remarks']
                obj.customerID = self.request.POST['customerID']
                obj.examTitle = self.request.POST['examTitle']
                obj.cswip_pcn = self.request.POST['cswip_pcn']
                obj.general_theory = self.request.POST['general_theory']
                obj.specific_theory = self.request.POST['specific_theory']
                obj.sample1 = self.request.POST['sample1']
                obj.sample2 = self.request.POST['sample2']
                obj.data_file_1 = self.request.POST['data_file_1']
                obj.data_file_2 = self.request.POST['data_file_2']
                obj.data_file_3 = self.request.POST['data_file_3']
                obj.data_file_4 = self.request.POST['data_file_4']
                obj.data_file_5 = self.request.POST['data_file_5']
                obj.written_instruction = self.request.POST['written_instruction']
                obj.save()


                events = Event.objects.all()
                candidates = TesCandidate.objects.all()
                exams = ExamMaterialTOFDModel1.objects.all()
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return render(request, 'certificates/exam_material_tofd_summary.html',context=context)


class ExamMaterialTofdSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/exam_material_tofd_summary.html"

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
