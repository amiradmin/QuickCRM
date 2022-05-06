from django.shortcuts import render
from  financials.models import EventCandidatePayment
from django.contrib.auth.mixins import LoginRequiredMixin
from authorization.sidebarmixin import SidebarMixin
from training.models import TesCandidate
from django.views.generic import View, TemplateView
from training.models import TesCandidate,Event
# Create your views here.


class EventCandidatePaymentView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "financials/payment_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventCandidatePaymentView, self).get_context_data()
        payments = EventCandidatePayment.objects.all()
        candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] = candidate
        context['payments'] = payments
        return context




class NewPayment(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "financials/new_payment.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewPayment, self).get_context_data()
        event = Event.objects.all()
        candidates = TesCandidate.objects.all()
        candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] = candidate

        context['event'] = exams
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewPayment, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo' in request.POST:
                print("updateInfo 2")
                print(request.POST['exam_ID'])
                exam = ExamMaterialTOFDModel1.objects.filter(id=self.request.POST['exam_ID'].split('-')[0]).first()
                # print(self.kwargs['id'])
                print(exam)
                candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
                group_name = self.request.user.groups.values_list('name', flat=True).first()
                context['group_name'] = group_name
                context['candidate'] = candidate

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
                candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
                group_name = self.request.user.groups.values_list('name', flat=True).first()
                context['group_name'] = group_name
                context['candidate'] = candidate

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
                candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
                group_name = self.request.user.groups.values_list('name', flat=True).first()
                context['group_name'] = group_name
                context['candidate'] = candidate

                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates
                # return render(request, 'certificates/exam_result_summary.html',context=context)
                return redirect('exam_certification:examtofdl2cswipresultsummary_')
            return redirect('exam_certification:examtofdl2cswipresultsummary_')

