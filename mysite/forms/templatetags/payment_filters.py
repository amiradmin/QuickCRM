from django import template
register = template.Library()
from training.models import  TesCandidate, Event
from financials.models import EventCandidatePayment
from django.contrib.sites.models import Site
from django.db.models import Q
from django import template
register = template.Library()

@register.simple_tag
def multiple_args_tag(eventID, canID):
    event = Event.objects.filter(id=eventID).first()
    candidate = TesCandidate.objects.filter(id=canID).first()
    counter = EventCandidatePayment.objects.filter(Q(event=event) & Q(candidate=candidate)).count()
    if counter > 0:
        obj = EventCandidatePayment.objects.filter(Q(event=event) & Q(candidate=candidate)).first()
        return obj.payment_status

    else:
        return 'Not Invoiced'



@register.simple_tag
def payment_url(eventID, canID):
    event = Event.objects.filter(id=eventID).first()
    candidate = TesCandidate.objects.filter(id=canID).first()
    counter = EventCandidatePayment.objects.filter(Q(event=event) & Q(candidate=candidate)).count()
    if counter > 0:
        obj = EventCandidatePayment.objects.filter(Q(event=event) & Q(candidate=candidate)).first()
        return Site.objects.get_current().domain + '/financials/updatepayment/'+ str(obj.id)
    else:
        return ''



#
# @register.tag(name='payment')
# def payment(eventID,canID):
#     return eventID

# @register.filter(name='payment')
# def payment(id):
#     """Convert a 10 character string into (xxx) xxx-xxxx."""
#
#     return 'paid:' + id
#

