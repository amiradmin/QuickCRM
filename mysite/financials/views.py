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
        events = Event.objects.all()
        candidates = TesCandidate.objects.all()
        candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] = candidate

        context['events'] = events
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(NewPayment, self).get_context_data()
        if request.method == 'POST':
            if 'updateInfo-event' in request.POST:
                print("updateInfo event")
                event = Event.objects.filter(id=self.request.POST['event'].split('-')[0]).first()
                print(event)

                # candidates = TesCandidate.objects.all()
                candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
                group_name = self.request.user.groups.values_list('name', flat=True).first()
                context['group_name'] = group_name
                context['candidate'] = candidate
                context['event'] = event
                return render(request, 'financials/new_payment.html', context)

            elif 'updateInfo-candidate' in request.POST:
                print("updateInfo candidate")
                print(self.request.POST['candidate'].split('-')[0])
                candidate_sel = TesCandidate.objects.filter(id=self.request.POST['candidate'].split('-')[0]).first()
                event = Event.objects.filter(id=self.request.POST['event_inner_ID'].split('-')[0]).first()
                print(candidate_sel)
                # candidates = TesCandidate.objects.all()

                context['candidate_sel'] = candidate_sel
                candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
                group_name = self.request.user.groups.values_list('name', flat=True).first()
                context['group_name'] = group_name
                context['candidate'] = candidate


                return render(request, 'financials/new_payment.html', context)
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
                candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
                group_name = self.request.user.groups.values_list('name', flat=True).first()
                context['group_name'] = group_name
                context['candidate'] = candidate
                samples = Samples.objects.all()
                context['samples'] = samples
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event
                context['exams'] = exams
                context['candidates'] = candidates

                return redirect('exam_certification:examtofdl2cswipresultsummary_')
            return redirect('exam_certification:examtofdl2cswipresultsummary_')





class UpdatePayment(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "financials/update_payment.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdatePayment, self).get_context_data()
        payment = EventCandidatePayment.objects.filter(id=self.kwargs['id']).first()
        candidates = TesCandidate.objects.all()
        candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] = candidate

        context['payment'] = payment
        context['candidates'] = candidates
        return context

    def post(self, request, *args, **kwargs):
        context = super(UpdatePayment, self).get_context_data()
        if request.method == 'POST':

            print("Update")
            payObj = EventCandidatePayment.objects.filter(id=self.kwargs['id']).first()

            if not request.POST.get('done', None) == None:
                print("done")
                payObj.payment_status= 'Done'

            elif not request.POST.get('invoiced', None) == None:
                payObj.payment_status = 'Invoiced'
            elif not request.POST.get('notInvoiced', None) == None:
                payObj.payment_status = 'Not Invoiced'

            payObj.company_name = request.POST['companyName']
            payObj.company_address = request.POST['comAddress']
            payObj.post_code = request.POST['postCode']
            payObj.phone = request.POST['phone']
            payObj.fax = request.POST['fax']
            payObj.contact_name = request.POST['contactName']
            payObj.email = request.POST['email']
            payObj.save()


            candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
            group_name = self.request.user.groups.values_list('name', flat=True).first()
            payment = EventCandidatePayment.objects.filter(id=self.kwargs['id']).first()
            context['group_name'] = group_name
            context['candidate'] = candidate
            context['payment'] = payment
            return render(request, 'financials/update_payment.html', context)


