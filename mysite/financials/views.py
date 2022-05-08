from django.shortcuts import render,redirect
from  financials.models import EventCandidatePayment
from django.contrib.auth.mixins import LoginRequiredMixin
from authorization.sidebarmixin import SidebarMixin
from training.models import TesCandidate
from django.views.generic import View, TemplateView
from training.models import TesCandidate,Event
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
# Create your views here.


class PaymentDeleteView(SidebarMixin, LoginRequiredMixin,DeleteView):
    model = EventCandidatePayment
    success_url = reverse_lazy('financials:allpayments_')


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
                context['event'] = event
                context['candidate_sel'] = candidate_sel


                return render(request, 'financials/new_payment.html', context)
            elif 'submit' in request.POST:
                print("Submit")
                print(self.request.POST['eventID'].split('-')[0])
                event = Event.objects.filter(id=self.request.POST['eventID'].split('-')[0]).first()
                candidate = TesCandidate.objects.filter(id=self.request.POST['candidateID'].split('-')[0]).first()

                payObj = EventCandidatePayment()
                if not request.POST.get('self', None) == None:
                    print("Self")
                    payObj.sponsor_status = False
                    payObj.candidate = candidate
                    payObj.event = event

                elif not request.POST.get('company', None) == None:
                    print("Company")
                    payObj.sponsor_status = True
                    payObj.candidate = candidate
                    payObj.event = event
                    payObj.company_name = request.POST['companyName']
                    payObj.company_address = request.POST['comAddress']
                    payObj.post_code = request.POST['postCode']
                    payObj.phone = request.POST['phone']
                    payObj.fax = request.POST['fax']
                    payObj.contact_name = request.POST['contactName']
                    payObj.email = request.POST['email']

                payObj.save()

                events = Event.objects.all()
                candidates = TesCandidate.objects.all()

                candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
                group_name = self.request.user.groups.values_list('name', flat=True).first()
                context['group_name'] = group_name
                context['candidate'] = candidate
                context['events'] = events
                context['candidate'] = TesCandidate.objects.filter(user=request.user).first()
                context['event'] = event

                context['candidates'] = candidates

                return redirect('financials:newpayment_')
            return redirect('financials:newpayment_')





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

            if bool(request.FILES.get('invoiced_file', False)) == True:
                payObj.invoiced_file = self.request.FILES['invoiced_file']

            if bool(request.FILES.get('recipients_file', False)) == True:
                payObj.recipients_file = self.request.FILES['recipients_file']
            payObj.save()


            candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
            group_name = self.request.user.groups.values_list('name', flat=True).first()
            payment = EventCandidatePayment.objects.filter(id=self.kwargs['id']).first()
            context['group_name'] = group_name
            context['candidate'] = candidate
            context['payment'] = payment
            return render(request, 'financials/update_payment.html', context)


