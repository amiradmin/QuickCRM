from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from forms.models import (Forms, TwiEnrolmentForm, General, BGAsExperienceForm, PSL30LogExp, NdtTechnique, FormList,
                          PSL30InitialForm, NDT15AExperienceVerification, CurrentFormerCertification,
                          ExperienceClaimed, NDTCovid19, PSL57B, PSL57A, empHistory, VisionTest,
                          TesFrmExaminationAttendance,TesAttCandidate,
                          TesLecFeedbackFrom, TrainingAttendance, TwiTrainingFeedback, TwiExamFeedback, TesFrmCandidate
                          )
from django.db.models import Count
from classes.db import FormDb
from training.models import FormsList, TesCandidate, Event, Category, FormsList as Guideline
from django.contrib.auth.mixins import LoginRequiredMixin
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from django.db.models import Q
import datetime
from authorization.sidebarmixin import SidebarMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from contacts.models import Contact


# Create your views here.

class TwiEnrolment(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/reg_forms/twi_enrolment_S.html"
    candidateID = None

    def get_context_data(self):
        context = super(TwiEnrolment, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events

        self.candidateID = 50
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            if 'enrolment' in request.POST:
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()
                obj = TwiEnrolmentForm()
                obj.eventID = eventID
                obj.candidate = candidate
                obj.twiCandidateID = request.POST['twiCandidateID']
                obj.eventName = request.POST['eventName']
                # obj.eventDate = datetime.datetime.strptime(request.POST['form3_1'], '%m/%d/%Y')
                obj.firstName = request.POST['firstName']
                obj.middleName = request.POST['middleName']
                obj.lastName = request.POST['lastName']
                day = request.POST['day']
                month = request.POST['month']
                year = request.POST['year']
                birdDay = month + '/' + day + '/' + year
                obj.birthOfDate = datetime.datetime.strptime(birdDay, '%m/%d/%Y')
                obj.permanentPrivateAddress = request.POST['permanentPrivateAddress']
                obj.Postcode = request.POST['Postcode']
                obj.CarRegNo = request.POST['CarRegNo']
                obj.privateTel = request.POST['privateTel']
                obj.emergencyTel = request.POST['emergencyTel']
                obj.email = request.POST['email']
                obj.correspondenceAddress = request.POST['correspondenceAddress']
                obj.invoiceAddress = request.POST['invoiceAddress']
                obj.sponsoringCompanyAndaddress = request.POST['sponsoringCompanyAndaddress']
                obj.sponsorPostcode = request.POST['sponsorPostcode']
                obj.sponsorContactName = request.POST['sponsorContactName']
                obj.sponsorTel = request.POST['sponsorTel']
                obj.sponsorFax = request.POST['sponsorFax']
                obj.sponsorEmail = request.POST['sponsorEmail']
                obj.PCN_BGASApprovalNumber = request.POST['PCN_BGASApprovalNumber']
                obj.currentCSWIPQualifications = request.POST['currentCSWIPQualifications']
                obj.plantInspectionRequirements = request.POST['plantInspectionRequirements']
                obj.VerifierName = request.POST['VerifierName']
                obj.VerifierCompanyPosition = request.POST['VerifierCompanyPosition']
                # obj.VerifierProfessionalRelation = request.POST['VerifierProfessionalRelation']
                obj.VerifierTelephone = request.POST['VerifierTelephone']
                obj.VerifierEmail = request.POST['VerifierEmail']
                # obj.experienceRequirements = request.POST['experienceRequirements']
                obj.otherExaminationsTitle = request.POST['otherExaminationsTitle']
                obj.bookingRef = request.POST['bookingRef']
                obj.VerifierDate = datetime.datetime.strptime(request.POST['VerifierDate'], '%m/%d/%Y')

                # obj.GDPRstatement = request.POST['form37_1']

                #
                #
                if not request.POST.get('Calgary', None) == None:
                    obj.venue ='Calgary'

                if not request.POST.get('Edmonton', None) == None:
                    obj.venue ='Edmonton'

                if not request.POST.get('Brazil', None) == None:
                    obj.venue ='Brazil'

                if not request.POST.get('Toronto', None) == None:
                    obj.venue ='Toronto'

                if not request.POST.get('FortErie', None) == None:
                   obj.venue ='Fort Erie'

                if not request.POST.get('USA', None) == None:
                    obj.venue ='USA'

                if not request.POST.get('Quebec', None) == None:
                    obj.venue ='Quebec'

                if not request.POST.get('Vancouver', None) == None:
                    obj.venue ='Vancouver'

                if not request.POST.get('New Brunswick', None) == None:
                    obj.venue ='New Brunswick'
                #
                if not request.POST.get('diabilityYes', None) == None:
                    obj.disability = True
                if request.POST.get('diabilityNo', None) == None:
                    obj.disability = False
                #
                if not request.POST.get('weldingSociety', None) == None:
                    obj.weldingSociety = True
                if not request.POST.get('twiEmployee', None) == None:
                    obj.twiEmployee = True
                #
                if not request.POST.get('compSponser', None) == None:
                    obj.sponsorStatus = True
                if not request.POST.get('selfSponser', None) == None:
                    obj.sponsorStatus = True
                #
                if not request.POST.get('GDPRstatement', None) == None:
                    obj.GDPRstatement = True
                #
                tempTearAbout = ''
                if not request.POST.get('twiWebsite', None) == None:
                    tempTearAbout = 'TWI Corporate Website'
                if not request.POST.get('CSWIPweb', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'CSWIP Website'
                if not request.POST.get('emailMarketing', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Email marketing'
                if not request.POST.get('Bulletin', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Bulletin / Connect'
                if not request.POST.get('Google', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Google search'
                if not request.POST.get('Other', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Other (please specify)'
                if not request.POST.get('Linkedin', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'LinkedIn'
                if not request.POST.get('Facebook', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Facebook'
                if not request.POST.get('NDTnews', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'NDT News / Insight'
                if not request.POST.get('Exhib', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Exhibitions / Events'
                if not request.POST.get('WorkOfMouth', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Word of Mouth'
                obj.hearAbout = tempTearAbout
                #
                if not request.POST.get('Initial', None) == None:
                    obj.examinationType = 'Initial'
                if not request.POST.get('supplementary', None) == None:
                    obj.examinationType = 'supplementary'
                if not request.POST.get('renewal', None) == None:
                    obj.examinationType = 'renewal'
                if not request.POST.get('bridging', None) == None:
                    obj.examinationType = 'bridging'
                if not request.POST.get('retest', None) == None:
                    obj.examinationType = 'retest of a previously failed examination'
                #
                if not request.POST.get('CSWIP', None) == None:
                    obj.examinationBody = 'CSWIP'
                if not request.POST.get('PCN', None) == None:
                    obj.examinationBody = 'PCN'
                if not request.POST.get('AWS', None) == None:
                    obj.examinationBody = 'AWS'
                if not request.POST.get('BGAS', None) == None:
                    obj.examinationBody = 'BGAS'
                if not request.POST.get('ASNT', None) == None:
                    obj.examinationBody = 'ASNT'

                #
                if not request.POST.get('VWI', None) == None:
                    obj.CSWIPWeldingexamination = 'VWI (3.0)'
                if not request.POST.get('WI', None) == None:
                    obj.CSWIPWeldingexamination = 'WI (3.1)'
                if not request.POST.get('SWI', None) == None:
                    obj.CSWIPWeldingexamination = 'SWI (3.2.1)'
                if not request.POST.get('SWI3', None) == None:
                    obj.CSWIPWeldingexamination = 'SWI (3.2.2) '
                if not request.POST.get('AWSCSWIP', None) == None:
                    obj.CSWIPWeldingexamination = 'AWSCSWIP'
                #
                if not request.POST.get('Endorsement', None) == None:
                    obj.CSWIPWeldingexamination = 'Endorsement'
                if not request.POST.get('Instructor', None) == None:
                    obj.CSWIPWeldingexamination = 'Instructor'
                if not request.POST.get('Supervisor', None) == None:
                    obj.CSWIPWeldingexamination = 'Supervisor'
                if not request.POST.get('QC', None) == None:
                    obj.CSWIPWeldingexamination = 'QC Coordinator'
                if not request.POST.get('ASME', None) == None:
                    obj.CSWIPWeldingexamination = 'ASME IX'
                #
                if not request.POST.get('WI31weld', None) == None:
                    obj.experience = 'WI(3.1) - Welding Inspector for a minimum of 3 years with experience related to the duties and responsibilities listed in Clause 1.2.2 under qualified supervision, independently verified.'
                if not request.POST.get('WI31Visual', None) == None:
                    obj.experience = 'WI (3.1) - Certified Visual Welding Inspector for a minimum of 2 years with job responsibilities in the areas listed in 1.2.1 and 1.2.2.'
                if not request.POST.get('WIWeldingInspector', None) == None:
                    obj.experience = 'WI (3.1) - Welding Instructor or Welding Foreman/Supervisor for a minimum of 1 year.'
                if not request.POST.get('SWIcertificate', None) == None:
                    obj.experience = 'SWI (3.2.1 & 3.2.2) - Certified Welding Inspector for a minimum of 2 years with job responsibilities in the areas listed in 1.2.1, 1.2.2 and 1.2.3. '
                if not request.POST.get('SWI5year', None) == None:
                    obj.experience = 'SWI (3.2.1 & 3.2.2) - 5 years\' authenticated experience related to the duties and responsibilities listed in Clause 1.2.3, independently verified.'

                if not request.POST.get('WeldingQC', None) == None:
                    obj.experience = 'Welding QC coordinator - A current valid CSWIP 3.2 Senior Welding Inspector certification plus three years documented experience related to the duties and responsibilities or an international equivalent.'
                if not request.POST.get('CurrentValid', None) == None:
                    obj.experience = 'Welding QC coordinator - A current valid CSWIP 3.1 Welding Inspector with 10 year’s documented experience related to the duties and responsibilities or an international equivalent. '
                if not request.POST.get('HoldCurrent', None) == None:
                    obj.experience = 'ASME IX - Hold current valid Senior Welding Inspector or international equivalent.'
                if not request.POST.get('ASMECer', None) == None:
                    obj.experience = 'ASME IX - Certified Welding Inspector with five years relevant verified work experience or international equivalent '
                if not request.POST.get('ASMEhnc', None) == None:
                    obj.experience = 'ASME IX - A HNC in Welding Fabrication'
                if not request.POST.get('ASMEWorking', None) == None:
                    obj.experience = 'ASME IX - Working in quality control function related to welding activities with five years of verified working experience (this could relate to a CSWIP WI (3.1) holder'
                #
                #
                if not request.POST.get('31U', None) == None:
                    obj.underwaterInspectionExam = '3.1U'
                if not request.POST.get('32U', None) == None:
                    obj.underwaterInspectionExam = '3.2U'
                if not request.POST.get('33U', None) == None:
                    obj.underwaterInspectionExam = '3.3U'
                if not request.POST.get('34U', None) == None:
                    obj.underwaterInspectionExam = '3.4U'
                if not request.POST.get('A-SCAN', None) == None:
                    obj.underwaterInspectionExam = 'A-SCAN'
                if not request.POST.get('Concrete', None) == None:
                    obj.underwaterInspectionExam = 'Concrete'

                #
                if not request.POST.get('PT', None) == None:
                    obj.NDTexamination = 'PT'
                if not request.POST.get('MT', None) == None:
                    obj.NDTexamination = 'MT'
                if not request.POST.get('VT', None) == None:
                    obj.NDTexamination = 'VT'
                if not request.POST.get('ET', None) == None:
                    obj.NDTexamination = 'ET'
                if not request.POST.get('ACFM', None) == None:
                    obj.NDTexamination = 'ACFM'
                #
                if not request.POST.get('RT', None) == None:
                    obj.NDTexamination = 'RT'
                if not request.POST.get('Rad', None) == None:
                    obj.NDTexamination = 'Rad Interpret'
                if not request.POST.get('CR', None) == None:
                    obj.NDTexamination = 'CR/DR'
                if not request.POST.get('CRI', None) == None:
                    obj.NDTexamination = 'CRI/DRI'
                if not request.POST.get('BRS', None) == None:
                    obj.NDTexamination = 'BRS'
                if not request.POST.get('RPS', None) == None:
                    obj.NDTexamination = 'RPS'

                if not request.POST.get('UT', None) == None:
                    obj.NDTexamination = 'UT'
                if not request.POST.get('PAUT', None) == None:
                    obj.NDTexamination = 'PAUT'
                if not request.POST.get('TOFD', None) == None:
                    obj.NDTexamination = 'TOFD'
                if not request.POST.get('AUT', None) == None:
                    obj.NDTexamination = 'AUT'
                if not request.POST.get('UTCM', None) == None:
                    obj.NDTexamination = 'UTCM'
                if not request.POST.get('PACM', None) == None:
                    obj.NDTexamination = 'PACM'
                #
                if not request.POST.get('Appreciation', None) == None:
                    obj.NDTexamination = 'Appreciation'
                if not request.POST.get('Basic', None) == None:
                    obj.NDTexamination = 'Basic'
                if not request.POST.get('Phasor', None) == None:
                    obj.NDTexamination = 'Phasor DM'
                #
                if not request.POST.get('Level1', None) == None:
                    obj.NDTexaminationLevel = 'Level 1'
                if not request.POST.get('Level2', None) == None:
                    obj.NDTexaminationLevel = 'Level 2'
                if not request.POST.get('Level3', None) == None:
                    obj.NDTexaminationLevel = 'Level 3'
                #
                if not request.POST.get('General', None) == None:
                    obj.NDTIndustrySector = 'General'
                if not request.POST.get('Welds', None) == None:
                    obj.NDTIndustrySector = 'Welds'
                if not request.POST.get('Castings', None) == None:
                    obj.NDTIndustrySector = 'Castings'
                if not request.POST.get('Wrought', None) == None:
                    obj.NDTIndustrySector = 'Wrought'
                if not request.POST.get('Forgings', None) == None:
                    obj.NDTIndustrySector = 'Forgings'
                if not request.POST.get('Tubes', None) == None:
                    obj.NDTIndustrySector = 'Tubes & Pipes'
                if not request.POST.get('Aero', None) == None:
                    obj.NDTIndustrySector = 'Aero'
                #
                #
                if not request.POST.get('31', None) == None:
                    obj.NDTexaminationCategories = '3.1'
                if not request.POST.get('32', None) == None:
                    obj.NDTexaminationCategories = '3.2'
                if not request.POST.get('37', None) == None:
                    obj.NDTexaminationCategories = '3.7'
                if not request.POST.get('38', None) == None:
                    obj.NDTexaminationCategories = '3.8'
                if not request.POST.get('39', None) == None:
                    obj.NDTexaminationCategories = '3.9'
                if not request.POST.get('Critical', None) == None:
                    obj.NDTexaminationCategories = 'Critical sizing'
                #
                #
                if not request.POST.get('plantLevel1', None) == None:
                    obj.plantInspectionLevel = 'Level 1'
                if not request.POST.get('plantLevel2', None) == None:
                    obj.plantInspectionLevel = 'Level 2'
                if not request.POST.get('plantLevel3', None) == None:
                    obj.plantInspectionLevel = 'Level 3'
                if not request.POST.get('Endorsement', None) == None:
                    obj.plantInspectionLevel = 'Endorsement'
                #
                if not request.POST.get('IHoldCurrent', None) == None:
                    obj.plantInspectionLevel1 = 'I hold current approved NDT Level 2 (ACCP, CSWIP, PCN or ASNT) in two methods, one of which must be Ultrasonic'
                if not request.POST.get('IholdCSWIP', None) == None:
                    obj.plantInspectionLevel1 = 'I hold CSWIP Welding Inspector or higher'
                if not request.POST.get('IholdHNC', None) == None:
                    obj.plantInspectionLevel1 = 'I hold HNC in Mechanical Engineering or equivalent'
                if not request.POST.get('Ihaveminimum', None) == None:
                    obj.plantInspectionLevel1 = 'I have a minimum of Five years, assessed and authenticated industry experience in this field (Mature Entry Route), a verified CV can be supplied – Must be Authenticated by Line Manager'

                if not request.POST.get('IholdvalidLevel', None) == None:
                    obj.plantInspectionLevel2 = 'I hold a valid Level 1 Plant Inspector approval'
                if not request.POST.get('IHaveSuccessfully', None) == None:
                    obj.plantInspectionLevel2 = 'I have successfully completed the Level 1 exams as a pre entry requirement'

                if not request.POST.get('Plastic', None) == None:
                    obj.otherExaminationsTitleRequired = 'Plastic welding'
                if not request.POST.get('Offshore', None) == None:
                    obj.otherExaminationsTitleRequired = 'Offshore visual Inspector'
                if not request.POST.get('BGAS', None) == None:
                    obj.otherExaminationsTitleRequired = 'BGAS'

                obj.save()
                formObj = FormsList.objects.filter(id=1).first()

                # mainCanID = request.POST['mainCanID']
                # print(mainCanID)
                # candidateObj = TesCandidate.objects.filter(id = 1050896).first()
                # print(candidateObj.first_name)
                candidate.forms.add(formObj)

                formListObj = FormList()
                formListObj.name = obj.__class__.__name__
                formListObj.event = event
                formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = obj.id
                formListObj.save()

                return redirect('forms:updatetwienroment_' , id=obj.id)


            else:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                print(canID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                self.candidateID = candidate.id
                print(self.candidateID)
                context = super(TwiEnrolment, self).get_context_data()
                context['candidate'] = candidate
                context['category'] = category
                context['event'] = event
                context['guideline'] = guideline

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/reg_forms/twi_enrolment_S.html', context)


class DeleteTwiEnrolment(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = TwiEnrolmentForm
    success_url = reverse_lazy('forms:allenrolmentform_')


class UpdateTwiEnrolment(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/reg_forms/update_twi_enrolment.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(UpdateTwiEnrolment, self).get_context_data()
        id = self.kwargs['id']
        form = TwiEnrolmentForm.objects.filter(id=id).first()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):

        if request.method == 'POST':
            if 'mainForm' in request.POST:
                # eventID = request.POST['eventID']
                # categoryID = request.POST['categoryID']
                # guidelineID = request.POST['guidelineID']
                # category = Category.objects.filter(id=categoryID).first()
                # guideline = Guideline.objects.filter(id=guidelineID).first()
                # event = Event.objects.filter(id=eventID).first()
                # candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()
                obj = TwiEnrolmentForm.objects.filter(id=id).first()
                # obj.eventID = eventID
                # obj.candidate = candidate
                # obj.eventID = eventID
                # obj.candidate = candidate
                obj.twiCandidateID = request.POST['twiCandidateID']
                obj.eventName = request.POST['eventName']
                # obj.eventDate = datetime.datetime.strptime(request.POST['form3_1'], '%m/%d/%Y')
                obj.firstName = request.POST['firstName']
                obj.middleName = request.POST['middleName']
                obj.lastName = request.POST['lastName']
                day = request.POST['day']
                month = request.POST['month']
                year = request.POST['year']
                birdDay = month + '/' + day + '/' + year
                obj.birthOfDate = datetime.datetime.strptime(birdDay, '%m/%d/%Y')
                obj.permanentPrivateAddress = request.POST['permanentPrivateAddress']
                obj.Postcode = request.POST['Postcode']
                obj.CarRegNo = request.POST['CarRegNo']
                obj.privateTel = request.POST['privateTel']
                obj.emergencyTel = request.POST['emergencyTel']
                obj.email = request.POST['email']
                obj.correspondenceAddress = request.POST['correspondenceAddress']
                obj.invoiceAddress = request.POST['invoiceAddress']
                obj.sponsoringCompanyAndaddress = request.POST['sponsoringCompanyAndaddress']
                obj.sponsorPostcode = request.POST['sponsorPostcode']
                obj.sponsorContactName = request.POST['sponsorContactName']
                obj.sponsorTel = request.POST['sponsorTel']
                obj.sponsorFax = request.POST['sponsorFax']
                obj.sponsorEmail = request.POST['sponsorEmail']
                obj.PCN_BGASApprovalNumber = request.POST['PCN_BGASApprovalNumber']
                obj.currentCSWIPQualifications = request.POST['currentCSWIPQualifications']
                obj.plantInspectionRequirements = request.POST['plantInspectionRequirements']
                obj.VerifierName = request.POST['VerifierName']
                obj.VerifierCompanyPosition = request.POST['VerifierCompanyPosition']
                # obj.VerifierProfessionalRelation = request.POST['VerifierProfessionalRelation']
                obj.VerifierTelephone = request.POST['VerifierTelephone']
                obj.VerifierEmail = request.POST['VerifierEmail']
                # obj.experienceRequirements = request.POST['experienceRequirements']
                obj.otherExaminationsTitle = request.POST['otherExaminationsTitle']
                obj.bookingRef = request.POST['bookingRef']
                obj.VerifierDate = datetime.datetime.strptime(request.POST['VerifierDate'], '%m/%d/%Y')

                # obj.GDPRstatement = request.POST['form37_1']

                #
                #
                if not request.POST.get('Calgary', None) == None:
                    obj.venue = 'Calgary'

                if not request.POST.get('Edmonton', None) == None:
                    obj.venue = 'Edmonton'

                if not request.POST.get('Brazil', None) == None:
                    obj.venue = 'Brazil'

                if not request.POST.get('Toronto', None) == None:
                    obj.venue = 'Toronto'

                if not request.POST.get('FortErie', None) == None:
                    obj.venue = 'Fort Erie'

                if not request.POST.get('USA', None) == None:
                    obj.venue = 'USA'

                if not request.POST.get('Quebec', None) == None:
                    obj.venue = 'Quebec'

                if not request.POST.get('Vancouver', None) == None:
                    obj.venue = 'Vancouver'

                if not request.POST.get('New Brunswick', None) == None:
                    obj.venue = 'New Brunswick'
                #
                if not request.POST.get('diabilityYes', None) == None:
                    obj.disability = True
                if request.POST.get('diabilityNo', None) == None:
                    obj.disability = False
                #
                if not request.POST.get('weldingSociety', None) == None:
                    obj.weldingSociety = True
                if not request.POST.get('twiEmployee', None) == None:
                    obj.twiEmployee = True
                #
                if not request.POST.get('compSponser', None) == None:
                    obj.sponsorStatus = True
                if not request.POST.get('selfSponser', None) == None:
                    obj.sponsorStatus = True
                #
                if not request.POST.get('GDPRstatement', None) == None:
                    obj.GDPRstatement = True
                #
                tempTearAbout = ''
                if not request.POST.get('twiWebsite', None) == None:
                    tempTearAbout = 'TWI Corporate Website'
                if not request.POST.get('CSWIPweb', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'CSWIP Website'
                if not request.POST.get('emailMarketing', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Email marketing'
                if not request.POST.get('Bulletin', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Bulletin / Connect'
                if not request.POST.get('Google', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Google search'
                if not request.POST.get('Other', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Other (please specify)'
                if not request.POST.get('Linkedin', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'LinkedIn'
                if not request.POST.get('Facebook', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Facebook'
                if not request.POST.get('NDTnews', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'NDT News / Insight'
                if not request.POST.get('Exhib', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Exhibitions / Events'
                if not request.POST.get('WorkOfMouth', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Word of Mouth'
                obj.hearAbout = tempTearAbout
                #
                if not request.POST.get('Initial', None) == None:
                    obj.examinationType = 'Initial'
                if not request.POST.get('supplementary', None) == None:
                    obj.examinationType = 'supplementary'
                if not request.POST.get('renewal', None) == None:
                    obj.examinationType = 'renewal'
                if not request.POST.get('bridging', None) == None:
                    obj.examinationType = 'bridging'
                if not request.POST.get('retest', None) == None:
                    obj.examinationType = 'retest of a previously failed examination'
                #
                if not request.POST.get('CSWIP', None) == None:
                    obj.examinationBody = 'CSWIP'
                if not request.POST.get('PCN', None) == None:
                    obj.examinationBody = 'PCN'
                if not request.POST.get('AWS', None) == None:
                    obj.examinationBody = 'AWS'
                if not request.POST.get('BGAS', None) == None:
                    obj.examinationBody = 'BGAS'
                if not request.POST.get('ASNT', None) == None:
                    obj.examinationBody = 'ASNT'

                #
                if not request.POST.get('VWI', None) == None:
                    obj.CSWIPWeldingexamination = 'VWI (3.0)'
                if not request.POST.get('WI', None) == None:
                    obj.CSWIPWeldingexamination = 'WI (3.1)'
                if not request.POST.get('SWI', None) == None:
                    obj.CSWIPWeldingexamination = 'SWI (3.2.1)'
                if not request.POST.get('SWI3', None) == None:
                    obj.CSWIPWeldingexamination = 'SWI (3.2.2) '
                if not request.POST.get('AWSCSWIP', None) == None:
                    obj.CSWIPWeldingexamination = 'AWSCSWIP'
                #
                if not request.POST.get('Endorsement', None) == None:
                    obj.CSWIPWeldingexamination = 'Endorsement'
                if not request.POST.get('Instructor', None) == None:
                    obj.CSWIPWeldingexamination = 'Instructor'
                if not request.POST.get('Supervisor', None) == None:
                    obj.CSWIPWeldingexamination = 'Supervisor'
                if not request.POST.get('QC', None) == None:
                    obj.CSWIPWeldingexamination = 'QC Coordinator'
                if not request.POST.get('ASME', None) == None:
                    obj.CSWIPWeldingexamination = 'ASME IX'
                #
                if not request.POST.get('WI31weld', None) == None:
                    obj.experience = 'WI(3.1) - Welding Inspector for a minimum of 3 years with experience related to the duties and responsibilities listed in Clause 1.2.2 under qualified supervision, independently verified.'
                if not request.POST.get('WI31Visual', None) == None:
                    obj.experience = 'WI (3.1) - Certified Visual Welding Inspector for a minimum of 2 years with job responsibilities in the areas listed in 1.2.1 and 1.2.2.'
                if not request.POST.get('WIWeldingInspector', None) == None:
                    obj.experience = 'WI (3.1) - Welding Instructor or Welding Foreman/Supervisor for a minimum of 1 year.'
                if not request.POST.get('SWIcertificate', None) == None:
                    obj.experience = 'SWI (3.2.1 & 3.2.2) - Certified Welding Inspector for a minimum of 2 years with job responsibilities in the areas listed in 1.2.1, 1.2.2 and 1.2.3. '
                if not request.POST.get('SWI5year', None) == None:
                    obj.experience = 'SWI (3.2.1 & 3.2.2) - 5 years\' authenticated experience related to the duties and responsibilities listed in Clause 1.2.3, independently verified.'

                if not request.POST.get('WeldingQC', None) == None:
                    obj.experience = 'Welding QC coordinator - A current valid CSWIP 3.2 Senior Welding Inspector certification plus three years documented experience related to the duties and responsibilities or an international equivalent.'
                if not request.POST.get('CurrentValid', None) == None:
                    obj.experience = 'Welding QC coordinator - A current valid CSWIP 3.1 Welding Inspector with 10 year’s documented experience related to the duties and responsibilities or an international equivalent. '
                if not request.POST.get('HoldCurrent', None) == None:
                    obj.experience = 'ASME IX - Hold current valid Senior Welding Inspector or international equivalent.'
                if not request.POST.get('ASMECer', None) == None:
                    obj.experience = 'ASME IX - Certified Welding Inspector with five years relevant verified work experience or international equivalent '
                if not request.POST.get('ASMEhnc', None) == None:
                    obj.experience = 'ASME IX - A HNC in Welding Fabrication'
                if not request.POST.get('ASMEWorking', None) == None:
                    obj.experience = 'ASME IX - Working in quality control function related to welding activities with five years of verified working experience (this could relate to a CSWIP WI (3.1) holder'
                #
                #
                if not request.POST.get('31U', None) == None:
                    obj.underwaterInspectionExam = '3.1U'
                if not request.POST.get('32U', None) == None:
                    obj.underwaterInspectionExam = '3.2U'
                if not request.POST.get('33U', None) == None:
                    obj.underwaterInspectionExam = '3.3U'
                if not request.POST.get('34U', None) == None:
                    obj.underwaterInspectionExam = '3.4U'
                if not request.POST.get('A-SCAN', None) == None:
                    obj.underwaterInspectionExam = 'A-SCAN'
                if not request.POST.get('Concrete', None) == None:
                    obj.underwaterInspectionExam = 'Concrete'

                #
                if not request.POST.get('PT', None) == None:
                    obj.NDTexamination = 'PT'
                if not request.POST.get('MT', None) == None:
                    obj.NDTexamination = 'MT'
                if not request.POST.get('VT', None) == None:
                    obj.NDTexamination = 'VT'
                if not request.POST.get('ET', None) == None:
                    obj.NDTexamination = 'ET'
                if not request.POST.get('ACFM', None) == None:
                    obj.NDTexamination = 'ACFM'
                #
                if not request.POST.get('RT', None) == None:
                    obj.NDTexamination = 'RT'
                if not request.POST.get('Rad', None) == None:
                    obj.NDTexamination = 'Rad Interpret'
                if not request.POST.get('CR', None) == None:
                    obj.NDTexamination = 'CR/DR'
                if not request.POST.get('CRI', None) == None:
                    obj.NDTexamination = 'CRI/DRI'
                if not request.POST.get('BRS', None) == None:
                    obj.NDTexamination = 'BRS'
                if not request.POST.get('RPS', None) == None:
                    obj.NDTexamination = 'RPS'

                if not request.POST.get('UT', None) == None:
                    obj.NDTexamination = 'UT'
                if not request.POST.get('PAUT', None) == None:
                    obj.NDTexamination = 'PAUT'
                if not request.POST.get('TOFD', None) == None:
                    obj.NDTexamination = 'TOFD'
                if not request.POST.get('AUT', None) == None:
                    obj.NDTexamination = 'AUT'
                if not request.POST.get('UTCM', None) == None:
                    obj.NDTexamination = 'UTCM'
                if not request.POST.get('PACM', None) == None:
                    obj.NDTexamination = 'PACM'
                #
                if not request.POST.get('Appreciation', None) == None:
                    obj.NDTexamination = 'Appreciation'
                if not request.POST.get('Basic', None) == None:
                    obj.NDTexamination = 'Basic'
                if not request.POST.get('Phasor', None) == None:
                    obj.NDTexamination = 'Phasor DM'
                #
                if not request.POST.get('Level1', None) == None:
                    obj.NDTexaminationLevel = 'Level 1'
                if not request.POST.get('Level2', None) == None:
                    obj.NDTexaminationLevel = 'Level 2'
                if not request.POST.get('Level3', None) == None:
                    obj.NDTexaminationLevel = 'Level 3'
                #
                if not request.POST.get('General', None) == None:
                    obj.NDTIndustrySector = 'General'
                if not request.POST.get('Welds', None) == None:
                    obj.NDTIndustrySector = 'Welds'
                if not request.POST.get('Castings', None) == None:
                    obj.NDTIndustrySector = 'Castings'
                if not request.POST.get('Wrought', None) == None:
                    obj.NDTIndustrySector = 'Wrought'
                if not request.POST.get('Forgings', None) == None:
                    obj.NDTIndustrySector = 'Forgings'
                if not request.POST.get('Tubes', None) == None:
                    obj.NDTIndustrySector = 'Tubes & Pipes'
                if not request.POST.get('Aero', None) == None:
                    obj.NDTIndustrySector = 'Aero'
                #
                #
                if not request.POST.get('31', None) == None:
                    obj.NDTexaminationCategories = '3.1'
                if not request.POST.get('32', None) == None:
                    obj.NDTexaminationCategories = '3.2'
                if not request.POST.get('37', None) == None:
                    obj.NDTexaminationCategories = '3.7'
                if not request.POST.get('38', None) == None:
                    obj.NDTexaminationCategories = '3.8'
                if not request.POST.get('39', None) == None:
                    obj.NDTexaminationCategories = '3.9'
                if not request.POST.get('Critical', None) == None:
                    obj.NDTexaminationCategories = 'Critical sizing'
                #
                #
                if not request.POST.get('plantLevel1', None) == None:
                    obj.plantInspectionLevel = 'Level 1'
                if not request.POST.get('plantLevel2', None) == None:
                    obj.plantInspectionLevel = 'Level 2'
                if not request.POST.get('plantLevel3', None) == None:
                    obj.plantInspectionLevel = 'Level 3'
                if not request.POST.get('Endorsement', None) == None:
                    obj.plantInspectionLevel = 'Endorsement'
                #
                if not request.POST.get('IHoldCurrent', None) == None:
                    obj.plantInspectionLevel1 = 'I hold current approved NDT Level 2 (ACCP, CSWIP, PCN or ASNT) in two methods, one of which must be Ultrasonic'
                if not request.POST.get('IholdCSWIP', None) == None:
                    obj.plantInspectionLevel1 = 'I hold CSWIP Welding Inspector or higher'
                if not request.POST.get('IholdHNC', None) == None:
                    obj.plantInspectionLevel1 = 'I hold HNC in Mechanical Engineering or equivalent'
                if not request.POST.get('Ihaveminimum', None) == None:
                    obj.plantInspectionLevel1 = 'I have a minimum of Five years, assessed and authenticated industry experience in this field (Mature Entry Route), a verified CV can be supplied – Must be Authenticated by Line Manager'

                if not request.POST.get('IholdvalidLevel', None) == None:
                    obj.plantInspectionLevel2 = 'I hold a valid Level 1 Plant Inspector approval'
                if not request.POST.get('IHaveSuccessfully', None) == None:
                    obj.plantInspectionLevel2 = 'I have successfully completed the Level 1 exams as a pre entry requirement'

                if not request.POST.get('Plastic', None) == None:
                    obj.otherExaminationsTitleRequired = 'Plastic welding'
                if not request.POST.get('Offshore', None) == None:
                    obj.otherExaminationsTitleRequired = 'Offshore visual Inspector'
                if not request.POST.get('BGAS', None) == None:
                    obj.otherExaminationsTitleRequired = 'BGAS'


                obj.save()

                return redirect('forms:allenrolmentform_')

            if 'uploadFormBack' in request.POST:
                print('uploadFormBack')
                obj = TwiEnrolmentForm.objects.filter(id=id).first()
                obj.uploadedForm = request.FILES['pdfFile']
                obj.save()
                return redirect('forms:allenrolmentform_')

class TwiEnrolmentReg(TemplateView):
    template_name = "forms/reg_forms/twi_enrolment_reg.html"
    candidateID = None

    def get_context_data(self, id, *args, **kwargs):
        context = super(TwiEnrolmentReg, self).get_context_data()
        self.candidateID = self.kwargs['id']
        print("Get : " + str(id))
        return context

    def post(self, request, id, *args, **kwargs):

        if request.method == 'POST':
            if 'enrolment' in request.POST:
                print("Post: " + str(id))
                print("Amir")
                # eventID = request.POST['eventID']
                candidate = TesCandidate.objects.filter(id=id).first()
                obj = TwiEnrolmentForm()
                # obj.eventID = eventID
                obj.candidate = candidate
                obj.twiCandidateID = request.POST['twiCandidateID']
                obj.eventName = request.POST['eventName']
                obj.eventDate = datetime.datetime.strptime(request.POST['eventDate'], '%m/%d/%Y')
                obj.firstName = request.POST['lastName']
                obj.middleName = request.POST['middleName']
                obj.lastName = request.POST['firstName']
                day = request.POST['day']
                month = request.POST['month']
                year = request.POST['year']
                birdDay = day + '/' + month + '/' + year
                obj.birthOfDate = datetime.datetime.strptime(birdDay, '%m/%d/%Y')
                # obj.permanentPrivateAddress = request.POST['form15_1']
                # obj.Postcode = request.POST['form18_1']
                # obj.CarRegNo = request.POST['form19_1']
                # obj.privateTel = request.POST['form20_1']
                # obj.emergencyTel = request.POST['form21_1']
                # obj.email = request.POST['form22_1']
                # obj.correspondenceAddress = request.POST['form28_1']
                # obj.invoiceAddress = request.POST['form38_1']
                # obj.sponsoringCompanyAndaddress = request.POST['form40_1']
                # obj.sponsorPostcode = request.POST['form43_1']
                # obj.sponsorContactName = request.POST['form44_1']
                # obj.sponsorTel = request.POST['form45_1']
                # obj.sponsorFax = request.POST['form46_1']
                # obj.sponsorEmail = request.POST['form47_1']
                # obj.PCN_BGASApprovalNumber = request.POST['form11_2']
                # obj.currentCSWIPQualifications = request.POST['form12_2']
                obj.VerifierDate = request.POST['VerifierDate']
                # # obj.GDPRstatement = request.POST['form37_1']

                # if not request.POST.get('form54_1', None) == None:
                #     obj.venue = 'Calgary'
                #
                # if not request.POST.get('form56_1', None) == None:
                #     obj.venue = 'Edmonton'
                #
                # if not request.POST.get('form12_1', None) == None:
                #     obj.venue = 'Brazil'
                #
                # if not request.POST.get('form55_1', None) == None:
                #     obj.venue = 'Toronto'
                #
                # if not request.POST.get('form57_1', None) == None:
                #     obj.venue = 'Fort Erie'
                #
                # if not request.POST.get('form13_1', None) == None:
                #     obj.venue = 'USA'
                #
                # if not request.POST.get('form10_1', None) == None:
                #     obj.venue = 'Quebec'
                #
                # if not request.POST.get('form11_1', None) == None:
                #     obj.venue = 'Vancouver'
                #
                # if not request.POST.get('form14_1', None) == None:
                #     obj.venue = 'New Brunswick'
                #
                # if not request.POST.get('diabilityYes', None) == None:
                #     obj.disability = True
                # if request.POST.get('diabilityNo', None) == None:
                #     obj.disability = False
                #
                # if not request.POST.get('form58_1', None) == None:
                #     obj.weldingSociety = True
                # if not request.POST.get('form59_1', None) == None:
                #     obj.twiEmployee = True
                #
                # if not request.POST.get('compSponser', None) == None:
                #     obj.sponsorStatus = True
                # if not request.POST.get('selfSponser', None) == None:
                #     obj.sponsorStatus = True
                #
                # if not request.POST.get('form37_1', None) == None:
                #     obj.GDPRstatement = True
                #
                # tempTearAbout = ''
                # if not request.POST.get('form29_1', None) == None:
                #     tempTearAbout = 'TWI Corporate Website '
                # if not request.POST.get('form30_1', None) == None:
                #     tempTearAbout = tempTearAbout + ' - ' + 'CSWIP Website'
                # if not request.POST.get('form31_1', None) == None:
                #     tempTearAbout = tempTearAbout + ' - ' + 'Email marketing '
                # if not request.POST.get('form32_1', None) == None:
                #     tempTearAbout = tempTearAbout + ' - ' + 'Bulletin / Connect '
                # if not request.POST.get('form33_1', None) == None:
                #     tempTearAbout = tempTearAbout + ' - ' + 'Google search'
                # if not request.POST.get('form34_1', None) == None:
                #     tempTearAbout = tempTearAbout + ' - ' + 'Other (please specify)'
                # if not request.POST.get('form23_1', None) == None:
                #     tempTearAbout = tempTearAbout + ' - ' + 'LinkedIn'
                # if not request.POST.get('form24_1', None) == None:
                #     tempTearAbout = tempTearAbout + ' - ' + 'Facebook'
                # if not request.POST.get('form25_1', None) == None:
                #     tempTearAbout = tempTearAbout + ' - ' + 'NDT News / Insight'
                # if not request.POST.get('form26_1', None) == None:
                #     tempTearAbout = tempTearAbout + ' - ' + 'Exhibitions / Events'
                # if not request.POST.get('form27_1', None) == None:
                #     tempTearAbout = tempTearAbout + ' - ' + 'Word of Mouth'
                # obj.hearAbout = tempTearAbout
                #
                # if not request.POST.get('form1_2', None) == None:
                #     obj.examinationType = 'Initial'
                # if not request.POST.get('form2_2', None) == None:
                #     obj.examinationType = 'supplementary'
                # if not request.POST.get('form3_2', None) == None:
                #     obj.examinationType = 'renewal'
                # if not request.POST.get('form4_2', None) == None:
                #     obj.examinationType = 'bridging'
                # if not request.POST.get('form5_2', None) == None:
                #     obj.examinationType = 'retest of a previously failed examination'
                #
                # if not request.POST.get('form6_2', None) == None:
                #     obj.examinationBody = 'CSWIP'
                # if not request.POST.get('form7_2', None) == None:
                #     obj.examinationBody = 'PCN'
                # if not request.POST.get('form8_2', None) == None:
                #     obj.examinationBody = 'AWS'
                # if not request.POST.get('form9_2', None) == None:
                #     obj.examinationBody = 'BGAS'
                # if not request.POST.get('form10_2', None) == None:
                #     obj.examinationBody = 'ASNT'

                obj.save()
                print("Here 3")

                formObj = FormList()
                formObj.name = "TWI Enrolment Form"
                formObj.candidate = candidate
                formObj.save()

                print("Start Mailing")
                msg = EmailMessage()

                asparagus_cid = make_msgid()
                msg.add_alternative("""\
   <style type="text/css">
    body {width: 600px;margin: 0 auto;}
    table {border-collapse: collapse;}
    table, td {mso-table-lspace: 0pt;mso-table-rspace: 0pt;}
    img {-ms-interpolation-mode: bicubic;}
  </style>
     <style type="text/css">
    body, p, div {
      font-family: inherit;
      font-size: 14px;
    }
    body {
      color: #000000;
    }
    body a {
      color: #1188E6;
      text-decoration: none;
    }
    p { margin: 0; padding: 0; }
    table.wrapper {
      width:100% !important;
      table-layout: fixed;
      -webkit-font-smoothing: antialiased;
      -webkit-text-size-adjust: 100%;
      -moz-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }
    img.max-width {
      max-width: 100% !important;
    }
    .column.of-2 {
      width: 50%;
    }
    .column.of-3 {
      width: 33.333%;
    }
    .column.of-4 {
      width: 25%;
    }
    @media screen and (max-width:480px) {
      .preheader .rightColumnContent,
      .footer .rightColumnContent {
        text-align: left !important;
      }
      .preheader .rightColumnContent div,
      .preheader .rightColumnContent span,
      .footer .rightColumnContent div,
      .footer .rightColumnContent span {
        text-align: left !important;
      }
      .preheader .rightColumnContent,
      .preheader .leftColumnContent {
        font-size: 80% !important;
        padding: 5px 0;
      }
      table.wrapper-mobile {
        width: 100% !important;
        table-layout: fixed;
      }
      img.max-width {
        height: auto !important;
        max-width: 100% !important;
      }
      a.bulletproof-button {
        display: block !important;
        width: auto !important;
        font-size: 80%;
        padding-left: 0 !important;
        padding-right: 0 !important;
      }
      .columns {
        width: 100% !important;
      }
      .column {
        display: block !important;
        width: 100% !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
      }
    }
  </style>
                 <body>
      <center class="wrapper" data-link-color="#1188E6" data-body-style="font-size:14px; font-family:inherit; color:#000000; background-color:#f0f0f0;">
        <div class="webkit">
          <table cellpadding="0" cellspacing="0" border="0" width="100%" class="wrapper" bgcolor="#f0f0f0">
            <tbody><tr>
              <td valign="top" bgcolor="#f0f0f0" width="100%">
                <table width="100%" role="content-container" class="outer" align="center" cellpadding="0" cellspacing="0" border="0">
                  <tbody><tr>
                    <td width="100%">
                      <table width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tbody><tr>
                          <td>
                            <!--[if mso]>
    <center>
    <table><tr><td width="600">
  <![endif]-->
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%; max-width:600px;" align="center">
                                      <tbody><tr>
                                        <td role="modules-container" style="padding:0px 0px 0px 0px; color:#000000; text-align:left;" bgcolor="#FFFFFF" width="100%" align="left"><table class="module preheader preheader-hide" role="module" data-type="preheader" border="0" cellpadding="0" cellspacing="0" width="100%" style="display: none !important; mso-hide: all; visibility: hidden; opacity: 0; color: transparent; height: 0; width: 0;">
    <tbody><tr>
      <td role="module-content">
        <p></p>
      </td>
    </tr>
  </tbody></table>
                                          <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:30px 0px 30px 20px;" bgcolor="#4d5171">
    <tbody>
      <tr role="module-content">
        <td height="100%" valign="top">
          <table class="column" width="560" style="width:560px; border-spacing:0; border-collapse:collapse; margin:0px 10px 0px 10px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="">
            <tbody>
              <tr>
                <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="a169501c-69eb-4f62-ad93-ac0150abdf03">
    <tbody>
      <tr>
        <td style="font-size:6px; line-height:10px; padding:0px 0px 0px 0px;" valign="top" align="left">
          <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px;" width="154" alt="" data-proportionally-constrained="true" data-responsive="false" src="http://185.231.59.78:8000/static/images/TES%20Canada%20Logo_PNG.png" >
        </td>
      </tr>
    </tbody>
  </table></td>
              </tr>
            </tbody>
          </table>

        </td>
      </tr>
    </tbody>
  </table>
                                          <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="080768f5-7b16-4756-a254-88cfe5138113">
    <tbody>
      <tr>
        <td style="padding:30px 30px 0px 30px; line-height:36px; text-align:inherit; background-color:#4d5171;" height="100%" valign="top" bgcolor="#4d5171" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="color: #ffffff; font-size: 18px; font-family: inherit">Dear """ + candidate.first_name + """ """ + candidate.last_name + """</span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="cddc0490-36ba-4b27-8682-87881dfbcc14">
    <tbody>
      <tr>
        <td style="padding:18px 30px 18px 30px; line-height:22px; text-align:inherit; background-color:#4d5171;" height="100%" valign="top" bgcolor="#4d5171" role="module-content"><div><div style="font-family: inherit; text-align: inherit"><span style="color: #ffffff; font-size: 15px">
            Thank you for registering with the TES Canada Booking System.<br>
            Kind Regards<br><br>
            TES Canada Customer Support<br>
            This is an automated email sent by the TES Canada Booking System. Please do not reply To this email. For assistance please contact TES Canada Customer Support


        </span></div><div></div></div></td>
      </tr>
    </tbody>
  </table>
                                          <table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="cd669415-360a-41a6-b4b4-ca9e149980b3">
      <tbody>
        <tr>
          <td align="center" bgcolor="#4d5171" class="outer-td" style="padding:10px 0px 40px 0px;">
            <table border="0" cellpadding="0" cellspacing="0" class="wrapper-mobile" style="text-align:center;">
              <tbody>
                <tr>
                <td align="center" bgcolor="#ffc94c" class="inner-td" style="border-radius:6px; font-size:16px; text-align:center; background-color:inherit;">

                </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
                                          <table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="c5a3c312-4d9d-44ff-9fce-6a8003caeeca">
    <tbody>
      <tr>
        <td style="padding:0px 20px 0px 20px;" role="module-content" height="100%" valign="top" bgcolor="#4d5171">
          <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="1px" style="line-height:1px; font-size:1px;">
            <tbody>
              <tr>
                <td style="padding:0px 0px 1px 0px;" bgcolor="#ffc94c"></td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
                                          <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="eb301547-da19-441f-80a1-81e1b56e64ad">
    <tbody>
      <tr>
        <td style="padding:30px 0px 18px 0px; line-height:22px; text-align:inherit; background-color:#4d5171;" height="100%" valign="top" bgcolor="#4d5171" role="module-content"><div><div style="font-family: inherit; text-align: center"><span style="color: #ffc94c; font-size: 20px; font-family: inherit"><strong></strong></span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="2931446b-8b48-42bd-a70c-bffcfe784680">
    <tbody>
      <tr>
        <td style="padding:0px 0px 10px 0px;" role="module-content" bgcolor="#4d5171">
        </td>
      </tr>
    </tbody>
  </table>



                    </td>
                  </tr>
                </tbody></table>
              </td>
            </tr>
          </tbody></table>
        </div>
      </center>


</body>






                """, subtype='html')

                fromEmail = 'registration@tescan.ca'
                toEmail = obj.email

                msg['Subject'] = 'Tescan Registration Dept.'
                msg['From'] = fromEmail
                msg['To'] = toEmail
                msg['Cc'] = 'customersupportdesk@tescan.ca'

                s = smtplib.SMTP('mail.tescan.ca', 26)
                s.starttls()
                s.login(fromEmail, 'A^f[Xoi+)ngh')
                s.send_message(msg)
                s.quit()

                # email = EmailMessage(
                #     'Tescan Registration Dept.',
                #     'Dear {}! Registration is done successfully. '.format(obj.firstName),
                #     'registration@tescan.ca',
                #     [obj.email],
                #     ['nima.vakilotojjar@tescan.ca'],
                #
                # )
                # email.send()
                print("End Mailing")
                return redirect('accounting:suceess_')


            else:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                print(canID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                self.candidateID = candidate.id
                print(self.candidateID)
                context = super(TwiEnrolment, self).get_context_data()
                context['candidate'] = candidate
                context['event'] = event

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/reg_forms/twi_enrolment.html', context)


class AllEnrolmentForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_forms_enrolment.html"

    def get_context_data(self):
        context = super(AllEnrolmentForm, self).get_context_data()
        forms = TwiEnrolmentForm.objects.all()
        adminStatus = False
        for g in self.request.user.groups.all():
            if g.name == 'super_admin' or g.name == 'training_admin':
                adminStatus = True
        context['adminStatus'] = adminStatus
        context['forms'] = forms
        return context


class AllBGASForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_bgas_form.html"

    def get_context_data(self):
        context = super(AllBGASForm, self).get_context_data()
        forms = BGAsExperienceForm.objects.all()
        context['forms'] = forms
        return context

class DeleteBGAS(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = BGAsExperienceForm
    success_url = reverse_lazy('forms:allbgasform_')


class NewForm(TemplateView):
    template_name = "forms/new_form.html"

    def get_context_data(self):
        context = super(NewForm, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context

    # def post(self, request, *args, **kwargs):

    #     if request.method == 'POST':

    #         formName =request.POST['formName']
    #         jsonCode =request.POST['jsonCode']
    #         formNameDb = formName.replace(' ','_')
    #         data = json.loads(jsonCode)
    #         fields = []

    #         obj = Forms()
    #         obj.name=formName
    #         obj.dbName = 'tesform_'+formNameDb
    #         obj.save()

    #         for item in data:
    #             if item['type'] == 'text' :

    #                 name = item['name']
    #                 label = item['label']
    #                 required = item['required']
    #                 tempDict ={}
    #                 tempDict['name']=name.replace('-','_')
    #                 tempDict['label']=label
    #                 tempDict['required']=required
    #                 fields.append(tempDict)

    #                 fieldObj = Field()
    #                 fieldObj.name = name
    #                 fieldObj.type = 'VARCHAR(256)'
    #                 fieldObj.require = required
    #                 fieldObj.label = label
    #                 fieldObj.save()

    #                 obj.fields.add(fieldObj)

    #         formObj = FormDb()
    #         formObj.TableGenerator(formNameDb,fields)

    #     return redirect('forms:all_')
    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            print('Here')
            if request.FILES.get('file', False):
                pdfFile = request.FILES['file']
                print(pdfFile)

        return redirect('forms:all_')


class NewBGASExperienceForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/general/bgas.html"

    def get_context_data(self):
        context = super(BGASExperienceForm, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("Post Here")
                canID = request.POST['mainCanID']
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()

                bgasObj = BGAsExperienceForm()
                bgasObj.candidate = candidate
                bgasObj.event = event
                # bgasObj.evenID =event.id
                bgasObj.firstName = candidate.first_name
                bgasObj.lastName = candidate.last_name
                bgasObj.middleName = candidate.middleName

                bgasObj.sponsorCcmpany = request.POST['sponsorCcmpany']
                bgasObj.sponsorName = request.POST['sponsorName']
                bgasObj.sponsorAddress = request.POST['sponsorAddress']
                bgasObj.VerifierName = request.POST['verifierName']
                bgasObj.VerifierCompany = request.POST['verifierCompany']
                bgasObj.VerifierPosition = request.POST['verifierPosition']
                bgasObj.VerifierTelephone = request.POST['verifierTel']
                bgasObj.VerifierEmail = request.POST['verifiermail']
                bgasObj.VerifierDate = datetime.datetime.strptime(request.POST['verifierDate'], '%m/%d/%Y')
                bgasObj.PreCertificationExperience = request.POST['PreCertificationExperience']

                bgasObj.save()

                formListObj = FormList()
                formListObj.name = bgasObj.__class__.__name__
                formListObj.event = event
                formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = bgasObj.id
                formListObj.save()

                return redirect('forms:updatebgasexpform_',id=bgasObj.id )


            elif 'selector' in request.POST:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                candidate = TesCandidate.objects.filter(id=canID).first()

                event = Event.objects.filter(id=eventID).first()
                self.candidateID = candidate.id
                twiEnrolmentForm = TwiEnrolmentForm.objects.filter(candidate=candidate).first()
                context = super(BGASExperienceForm, self).get_context_data()
                context['candidate'] = candidate
                context['event'] = event
                context['category'] = category
                context['guideline'] = guideline
                context['twiEnrolmentForm'] = twiEnrolmentForm

                # return redirect('forms:jaegertofdl2_' ,context)
                return render(request, 'forms/general/bgas.html', context)


class UpdateBGASExperienceForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/general/update_bgas.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateBGASExperienceForm, self).get_context_data()
        form = BGAsExperienceForm.objects.filter(id=self.kwargs['id']).first()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("Post Here")


                bgasObj = BGAsExperienceForm.objects.filter(id = self.kwargs['id']).first()


                # bgasObj.sponsorCcmpany = request.POST['fullName']
                bgasObj.sponsorCcmpany = request.POST['sponsorCcmpany']
                bgasObj.sponsorName = request.POST['sponsorName']
                bgasObj.sponsorAddress = request.POST['sponsorAddress']
                bgasObj.VerifierName = request.POST['verifierName']
                bgasObj.VerifierCompany = request.POST['verifierCompany']
                bgasObj.VerifierPosition = request.POST['verifierPosition']
                bgasObj.VerifierTelephone = request.POST['verifierTel']
                bgasObj.VerifierEmail = request.POST['verifiermail']
                bgasObj.VerifierDate = datetime.datetime.strptime(request.POST['verifierDate'], '%m/%d/%Y')
                bgasObj.PreCertificationExperience = request.POST['PreCertificationExperience']

                bgasObj.save()

                return redirect('forms:allbgasform_')

            if 'uploadFormBack' in request.POST:
                print('uploadFormBack')
                obj = BGAsExperienceForm.objects.filter(id=self.kwargs['id']).first()
                obj.file = request.FILES['pdfFile']
                obj.save()
                return redirect('forms:allbgasform_')

                # return redirect('forms:jaegertofdl2_' ,context)
        return render(request, 'forms/general/bgas.html')

class PSL57AFOrmView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/reg_forms/PSL-57A_Initial_exam_application_S.html"

    def get_context_data(self):
        context = super(PSL57AFOrmView, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:

                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                print("===> here")
                guidelineID = request.POST['guidelineID']
                print(guidelineID)
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()

                mainObj = PSL57A()
                mainObj.candidate = candidate
                mainObj.event = event
                mainObj.category = category
                mainObj.guideline = guideline
                mainObj.cerAddress = request.POST['cerAddress']
                mainObj.pslCerAddress = request.POST['pslCerAddress']
                mainObj.phone = request.POST['phone']
                mainObj.pclNumber = request.POST['pclNumber']
                mainObj.email = request.POST['email']
                mainObj.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%m/%d/%Y')
                mainObj.currentEmploymentDetails = request.POST['currentEmploymentDetails']
                mainObj.candidatePosition = request.POST['currentEmploymentPosition']
                mainObj.employmentStatus = request.POST['currentEmploymentStatus']
                mainObj.preCerTraining = request.POST['preCerTraining']
                mainObj.preCerTrainingDate = request.POST['preCerTrainingDate']
                mainObj.iroductsIndustrySector = request.POST['iroductsIndustrySector']

                if not request.POST.get('contactMe', None) == None:
                    mainObj.contactMe = True
                else:
                    mainObj.contactMe = True

                if request.POST.get('gender', None) == 'Male':
                    mainObj.gender = 'M'
                elif request.POST.get('gender', None) == 'Female':
                    mainObj.gender = 'M'

                if not request.POST.get('et', None) == None:
                    mainObj.NDTMethod = 'ET'

                if not request.POST.get('mt', None) == None:
                    mainObj.NDTMethod = 'MT'

                if not request.POST.get('pt', None) == None:
                    mainObj.NDTMethod = 'PT'

                if not request.POST.get('rt', None) == None:
                    mainObj.NDTMethod = 'RT'

                if not request.POST.get('ri', None) == None:
                    mainObj.NDTMethod = 'RI'
                if not request.POST.get('ut', None) == None:
                    mainObj.NDTMethod = 'UT'
                if not request.POST.get('vt', None) == None:
                    mainObj.NDTMethod = 'VT'
                if not request.POST.get('crt', None) == None:
                    mainObj.NDTMethod = 'CRT'
                if not request.POST.get('tofd', None) == None:
                    mainObj.NDTMethod = 'TOFD'
                if not request.POST.get('paut', None) == None:
                    mainObj.NDTMethod = 'PAUT'

                if not request.POST.get('levelOne', None) == None:
                    mainObj.NDTLevel = 'level 1'
                if not request.POST.get('levelTwo', None) == None:
                    mainObj.NDTLevel = 'level 2'
                if not request.POST.get('levelThree', None) == None:
                    mainObj.NDTLevel = 'level 3'

                if not request.POST.get('basicRadio', None) == None:
                    mainObj.radiationSafety = 'Basic Radiation Safety'
                if not request.POST.get('supervisorProtection', None) == None:
                    mainObj.radiationProtectionSup = 'Radiation protection supervisor'

                if not request.POST.get('visa', None) == None:
                    mainObj.creditCardPayment = 'Visa'
                if not request.POST.get('masterCard', None) == None:
                    mainObj.creditCardPayment = 'Master Card'
                if not request.POST.get('amex', None) == None:
                    mainObj.creditCardPayment = 'Amex'
                if not request.POST.get('switch', None) == None:
                    mainObj.creditCardPayment = 'Switch'

                mainObj.ndtMethod = request.POST['ndtOther']
                mainObj.ifLevel3 = request.POST['ifLevel3']
                # mainObj.basicRadiationSafty = request.POST['basicRadiationSafty']
                # mainObj.radiationProtectionSupervisor = request.POST['radiationProtectionSupervisor']
                mainObj.cerCategory = request.POST['cerCategory']
                mainObj.preferredExaminationDateVenue = request.POST['preferredExaminationDateVenue']

                mainObj.claimDuration = request.POST['claimDuration']
                mainObj.verClaimAddress = request.POST['verClaimAddress']
                # mainObj.dateOfCourse  = request.POST['dateOfCourse']
                mainObj.sponsorName = request.POST['sponsorName']
                mainObj.sponsorCompany = request.POST['sponsorCompany']
                mainObj.sponsorPhone = request.POST['sponsorPhone']

                mainObj.testCenterExamDate = datetime.datetime.strptime(request.POST['testCenterExamDate'], '%m/%d/%Y')
                mainObj.testCenterExaminer = request.POST['testCenterExaminer']
                mainObj.testCenterPaymentReceived = request.POST['testCenterPaymentReceived']
                mainObj.testCenterVenue = request.POST['testCenterVenue']
                mainObj.testCenterModerator = request.POST['testCenterModerator']
                mainObj.testCenterResultRef = request.POST['testCenterResultRef']
                mainObj.testCenterExamCompleteColsed = request.POST['testCenterExamCompleteColsed']

                mainObj.nameAddressInvoice = request.POST['nameAddressInvoice']
                mainObj.accommodation = request.POST['accommodation']
                mainObj.paymentMethod = request.POST['paymentMethod']
                mainObj.nameResponsible = request.POST['nameResponsible']
                mainObj.companyOrderReference = request.POST['companyOrderReference']
                mainObj.issueExpiryDates = datetime.datetime.strptime(request.POST['issueExpiryDates'], '%m/%d/%Y')
                mainObj.NameOnCard = request.POST['NameOnCard']
                mainObj.cardNumber = request.POST['cardNumber']
                mainObj.securityCode = request.POST['securityCode']
                mainObj.addressCreditCardHolder = request.POST['addressCreditCardHolder']
                mainObj.categoriesOfCertification = request.POST['cerCategory']
                mainObj.preferredExaminationDateVenu = request.POST['preferredExaminationDateVenue']
                mainObj.debit = request.POST['debit']

                # mainObj.creditCardPayment = request.POST['creditCardPayment']

                mainObj.save()

                # formObj = FormList()
                # formObj.name = "PSL-57A Initial exam application"
                # formObj.candidate = candidate
                # formObj.event = event
                # formObj.category = category
                # formObj.guideline = guideline

                if not request.POST.get('comfirmation', None) == None:
                    formObj.status = True

                # formObj.save()

                return redirect('forms:allpsl57A_')


            elif 'selector' in request.POST:
                print('Here SA Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canCanID']
                eventID = request.POST['eventEvID']

                guidelineID = request.POST['guidelineGID']
                categoryID = request.POST['categoryCatID']
                print(guidelineID)
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                candidate = TesCandidate.objects.filter(id=canID).first()

                context = super(PSL57AFOrmView, self).get_context_data()
                context['candidate'] = candidate
                context['event'] = event
                context['guideline'] = guideline
                context['category'] = category

                # return redirect('forms:jaegertofdl2_' ,context)
                return render(request, "forms/reg_forms/PSL-57A_Initial_exam_application_S.html", context)


class AllPSL57AFOrmView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_psl_57a.html"

    def get_context_data(self):
        context = super(AllPSL57AFOrmView, self).get_context_data()
        forms = PSL57A.objects.all()

        context['forms'] = forms
        return context


class DeletePSL57AForm(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = PSL57A
    success_url = reverse_lazy('forms:allpsl57A_')


class AllBGASinitialForms(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_psl30_inintal_forms.html"

    def get_context_data(self):
        context = super(AllBGASinitialForms, self).get_context_data()
        forms = PSL30InitialForm.objects.all()

        context['forms'] = forms
        return context


class UpdatePSL57AForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/reg_forms/update_PSL-57A_Initial.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdatePSL57AForm, self).get_context_data()
        form = PSL57A.objects.filter(id=self.kwargs['id']).first()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:

                mainObj = PSL57A.objects.filter(id=self.kwargs['id']).first()
                mainObj.candidate = candidate
                mainObj.event = event
                mainObj.cerAddres = request.POST['cerAddres']
                mainObj.pslCerAddres = request.POST['pslCerAddres']
                mainObj.phone = request.POST['phone']
                mainObj.pslNumber = request.POST['pslNumber']
                mainObj.email = request.POST['email']
                mainObj.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%d/%m/%Y')
                mainObj.currentEmploymentPosition = request.POST['currentEmploymentPosition']
                mainObj.currentEmploymentStatus = request.POST['currentEmploymentStatus']
                mainObj.preCerTraining = request.POST['preCerTraining']
                mainObj.preCerTrainingDate = datetime.datetime.strptime(request.POST['preCerTrainingDate'], '%d/%m/%Y')
                # mainObj.preCerTraining = request.POST['preCerTraining']

                if not request.POST.get('et', None) == None:
                    mainObj.ndtMethod = 'ET'

                if not request.POST.get('mt', None) == None:
                    mainObj.ndtMethod = 'MT'

                if not request.POST.get('pt', None) == None:
                    mainObj.ndtMethod = 'PT'

                if not request.POST.get('rt', None) == None:
                    mainObj.ndtMethod = 'RT'

                if not request.POST.get('ri', None) == None:
                    mainObj.ndtMethod = 'RI'
                if not request.POST.get('ut', None) == None:
                    mainObj.ndtMethod = 'UT'
                if not request.POST.get('vt', None) == None:
                    mainObj.ndtMethod = 'VT'
                if not request.POST.get('crt', None) == None:
                    mainObj.ndtMethod = 'CRT'
                if not request.POST.get('tofd', None) == None:
                    mainObj.ndtMethod = 'TOFD'
                if not request.POST.get('paut', None) == None:
                    mainObj.ndtMethod = 'PAUT'

                if not request.POST.get('levelOne', None) == None:
                    mainObj.level = 'level 1'
                if not request.POST.get('levelTwo', None) == None:
                    mainObj.level = 'level 2'
                if not request.POST.get('levelThree', None) == None:
                    mainObj.level = 'level 3'

                # mainObj.ndtMethod = request.POST['ndtOther']
                # mainObj.level3State = request.POST['ifLevel3']
                mainObj.basicRadiationSafty = request.POST['basicRadiationSafty']
                mainObj.radiationProtectionSupervisor = request.POST['radiationProtectionSupervisor']
                mainObj.cerCategory = request.POST['cerCategory']
                mainObj.preferredExaminationDateVenue = request.POST['preferredExaminationDateVenue']

                mainObj.save()

                # formObj = FormList()
                # formObj.name = "PSL-57A Initial exam application"
                # formObj.candidate = candidate
                # formObj.event = event
                # if not request.POST.get('comfirmation', None) == None:
                #     formObj.status = True
                #
                # formObj.save()

                return redirect('forms:allpsl57A_')


class MessageUpdatePSL57AForm(LoginRequiredMixin, TemplateView):
    template_name = "forms/reg_forms/update_PSL-57A_Initial.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MessageUpdatePSL57AForm, self).get_context_data()
        form = PSL57A.objects.filter(id=self.kwargs['id']).first()
        contactObj = Contact.objects.filter(id=self.kwargs['msgID']).first()
        contactObj.readFlag = True
        contactObj.save()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:

                mainObj = PSL57A.objects.filter(id=self.kwargs['id']).first()
                mainObj.candidate = candidate
                mainObj.event = event
                mainObj.cerAddres = request.POST['cerAddres']
                mainObj.pslCerAddres = request.POST['pslCerAddres']
                mainObj.phone = request.POST['phone']
                mainObj.pslNumber = request.POST['pslNumber']
                mainObj.email = request.POST['email']
                mainObj.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%d/%m/%Y')
                mainObj.currentEmploymentPosition = request.POST['currentEmploymentPosition']
                mainObj.currentEmploymentStatus = request.POST['currentEmploymentStatus']
                mainObj.preCerTraining = request.POST['preCerTraining']
                mainObj.preCerTrainingDate = datetime.datetime.strptime(request.POST['preCerTrainingDate'], '%d/%m/%Y')
                # mainObj.preCerTraining = request.POST['preCerTraining']

                if not request.POST.get('et', None) == None:
                    mainObj.ndtMethod = 'ET'

                if not request.POST.get('mt', None) == None:
                    mainObj.ndtMethod = 'MT'

                if not request.POST.get('pt', None) == None:
                    mainObj.ndtMethod = 'PT'

                if not request.POST.get('rt', None) == None:
                    mainObj.ndtMethod = 'RT'

                if not request.POST.get('ri', None) == None:
                    mainObj.ndtMethod = 'RI'
                if not request.POST.get('ut', None) == None:
                    mainObj.ndtMethod = 'UT'
                if not request.POST.get('vt', None) == None:
                    mainObj.ndtMethod = 'VT'
                if not request.POST.get('crt', None) == None:
                    mainObj.ndtMethod = 'CRT'
                if not request.POST.get('tofd', None) == None:
                    mainObj.ndtMethod = 'TOFD'
                if not request.POST.get('paut', None) == None:
                    mainObj.ndtMethod = 'PAUT'

                if not request.POST.get('levelOne', None) == None:
                    mainObj.level = 'level 1'
                if not request.POST.get('levelTwo', None) == None:
                    mainObj.level = 'level 2'
                if not request.POST.get('levelThree', None) == None:
                    mainObj.level = 'level 3'

                # mainObj.ndtMethod = request.POST['ndtOther']
                mainObj.level3State = request.POST['ifLevel3']
                mainObj.basicRadiationSafty = request.POST['basicRadiationSafty']
                mainObj.radiationProtectionSupervisor = request.POST['radiationProtectionSupervisor']
                mainObj.cerCategory = request.POST['cerCategory']
                mainObj.preferredExaminationDateVenue = request.POST['preferredExaminationDateVenue']

                mainObj.save()

                # formObj = FormList()
                # formObj.name = "PSL-57A Initial exam application"
                # formObj.candidate = candidate
                # formObj.event = event
                # if not request.POST.get('comfirmation', None) == None:
                #     formObj.status = True
                #
                # formObj.save()

                return redirect('forms:allpsl57A_')


class ViewPSL57AForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/reg_forms/view_PSL-57A_Initial.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ViewPSL57AForm, self).get_context_data()
        form = PSL57A.objects.filter(id=self.kwargs['id']).first()
        context['form'] = form
        return context


class MessagePSL30LogExperienceForm(LoginRequiredMixin, TemplateView):
    template_name = "forms/reg_forms/update_PSL_30_log_exper.html"

    def get_context_data(self, id, msgID):
        context = super(MessagePSL30LogExperienceForm, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name')

        events = Event.objects.all()
        print("Here Now one")
        contactObj = Contact.objects.filter(id=self.kwargs['msgID']).first()
        contactObj.readFlag = True
        contactObj.save()

        context['candidates'] = candidates
        context['events'] = events
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                # eventID = request.POST['eventID']
                print("Form")
                print(canID)
                print(eventID)
                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                event.candidate.add(candidate)

                mainObj = PSL30InitialForm()
                mainObj.candidate = candidate
                mainObj.event = event
                mainObj.cerAddres = request.POST['cerAddres']
                mainObj.pslCerAddres = request.POST['pslCerAddres']
                mainObj.phone = request.POST['phone']
                mainObj.pslNumber = request.POST['pslNumber']
                mainObj.email = request.POST['email']
                mainObj.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%d/%m/%Y')
                mainObj.currentEmploymentPosition = request.POST['currentEmploymentPosition']
                mainObj.currentEmploymentStatus = request.POST['currentEmploymentStatus']
                mainObj.preCerTraining = request.POST['preCerTraining']
                mainObj.preCerTrainingDate = datetime.datetime.strptime(request.POST['preCerTrainingDate'], '%d/%m/%Y')
                # mainObj.preCerTraining = request.POST['preCerTraining']

                if not request.POST.get('et', None) == None:
                    mainObj.ndtMethod = 'ET'

                if not request.POST.get('mt', None) == None:
                    mainObj.ndtMethod = 'MT'

                if not request.POST.get('pt', None) == None:
                    mainObj.ndtMethod = 'PT'

                if not request.POST.get('rt', None) == None:
                    mainObj.ndtMethod = 'RT'

                if not request.POST.get('ri', None) == None:
                    mainObj.ndtMethod = 'RI'
                if not request.POST.get('ut', None) == None:
                    mainObj.ndtMethod = 'UT'
                if not request.POST.get('vt', None) == None:
                    mainObj.ndtMethod = 'VT'
                if not request.POST.get('crt', None) == None:
                    mainObj.ndtMethod = 'CRT'
                if not request.POST.get('tofd', None) == None:
                    mainObj.ndtMethod = 'TOFD'
                if not request.POST.get('paut', None) == None:
                    mainObj.ndtMethod = 'PAUT'

                if not request.POST.get('levelOne', None) == None:
                    mainObj.level = 'level 1'
                if not request.POST.get('levelTwo', None) == None:
                    mainObj.level = 'level 2'
                if not request.POST.get('levelThree', None) == None:
                    mainObj.level = 'level 3'

                # mainObj.ndtMethod = request.POST['ndtOther']
                mainObj.level3State = request.POST['ifLevel3']
                mainObj.basicRadiationSafty = request.POST['basicRadiationSafty']
                mainObj.radiationProtectionSupervisor = request.POST['radiationProtectionSupervisor']
                mainObj.cerCategory = request.POST['cerCategory']
                mainObj.preferredExaminationDateVenue = request.POST['preferredExaminationDateVenue']

                mainObj.save()

                formObj = FormList()
                formObj.name = "PSL-57A Initial exam application"
                formObj.candidate = candidate
                formObj.event = event
                if not request.POST.get('comfirmation', None) == None:
                    formObj.status = True

                formObj.save()

                return redirect('forms:allpslinitialform_')


class PSL30LogExperienceForm(TemplateView):
    template_name = "forms/reg_forms/PSL_30_log_exper_S.html"

    def get_context_data(self):
        context = super(PSL30LogExperienceForm, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()
        adminStatus = False
        for g in self.request.user.groups.all():
            if g.name == 'super_admin' or g.name == 'training_admin':
                adminStatus = True
        context['adminStatus'] = adminStatus
        context['candidates'] = candidates
        context['guidelines'] = guidelines
        context['categories'] = categories
        context['events'] = events

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                canID = request.POST['mainCanID']
                eventID = request.POST['eventID']
                # eventID = request.POST['eventID']
                print("Form")
                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                pslObj = PSL30LogExp()
                pslObj.candidate = candidate
                pslObj.event = event
                # pslObj.fullName = request.POST['canName']
                pslObj.dateFrom = datetime.datetime.strptime(request.POST['dateFrom'], '%m/%d/%Y')
                pslObj.dateTo = datetime.datetime.strptime(request.POST['dateTo'], '%m/%d/%Y')
                pslObj.ndtMethod = request.POST['ndtMethod']
                pslObj.totalHours = request.POST['totalHours']
                pslObj.employingOrganisation = request.POST['employingOrganisation']
                pslObj.reviewerName = request.POST['reviewerName']
                pslObj.reviewerDate = datetime.datetime.strptime(request.POST['reviewerDate'], '%m/%d/%Y')
                pslObj.finalEmployerDeclarationName = request.POST['finalEmployerDeclarationName']
                pslObj.dateCandidateDeclaration = datetime.datetime.strptime(request.POST['dateCandidateDeclaration'],
                                                                             '%m/%d/%Y')
                pslObj.save()
                for idx, item in enumerate(range(0, 7)):
                    if not request.POST.get('techniqueCodeR'+str(idx), None) == None:
                        print(idx)
                        NdtTechniqueObj = NdtTechnique()
                        NdtTechniqueObj.candidate = candidate
                        NdtTechniqueObj.techniqueCode = request.POST['techniqueCodeR'+str(idx)]
                        NdtTechniqueObj.employerComponent = request.POST['employerComponentR'+str(idx)]
                        NdtTechniqueObj.ndtTask = request.POST['ndtTaskR'+str(idx)]
                        NdtTechniqueObj.experienceHours = request.POST['experienceHoursR'+str(idx)]
                        NdtTechniqueObj.experienceConfirmed = request.POST['experienceConfirmedR'+str(idx)]
                        NdtTechniqueObj.save()
                        pslObj.ndtTechnique.add(NdtTechniqueObj)




                return redirect('forms:allpslform_')

            else:
                print('Here Today Now')
                context = super(PSL30LogExperienceForm, self).get_context_data()
                canID = request.POST['cancanID']
                eventID = request.POST['eventEvID']
                categoryID = request.POST['categoryCatID']
                guidelineID = request.POST['guidelineLINID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                print(canID)
                print(eventID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                print(candidate.first_name)
                event = Event.objects.filter(id=eventID).first()
                self.candidateID = candidate.id
                twiEnrolmentForm = TwiEnrolmentForm.objects.filter(candidate=candidate).first()

                context['category'] = category
                context['guideline'] = guideline
                context['candidate'] = candidate
                context['event'] = event
                context['twiEnrolmentForm'] = twiEnrolmentForm

                # return redirect('forms:jaegertofdl2_' ,context)
                return render(request, 'forms/reg_forms/PSL_30_log_exper_S.html', context)


class AllPSL30LogForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_psl30log_forms.html"

    def get_context_data(self):
        context = super(AllPSL30LogForm, self).get_context_data()
        pslForms = PSL30LogExp.objects.all()
        adminStatus = False
        for g in self.request.user.groups.all():
            if g.name == 'super_admin' or g.name == 'training_admin':
                adminStatus = True
        context['adminStatus'] = adminStatus
        context['pslForms'] = pslForms

        return context


class DeletePSL30LogExperienceForm(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = PSL30LogExp
    success_url = reverse_lazy('forms:allpslform_')


class UpdatePSL30LogExperienceForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/reg_forms/update_PSL_30_log_exper.html"

    def get_context_data(self, id):
        context = super(UpdatePSL30LogExperienceForm, self).get_context_data()
        form = PSL30LogExp.objects.filter(id=self.kwargs['id']).first()
        context['form'] = form

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                canID = request.POST['canID']
                # eventID = request.POST['eventID']
                # eventID = request.POST['eventID']
                print("Form Today")
                candidate = TesCandidate.objects.filter(id=canID).first()
                # event = Event.objects.filter(id=eventID).first()
                pslObj = PSL30LogExp.objects.filter(id=self.kwargs['id']).first()
                # pslObj.candidate =candidate
                # pslObj.event =event
                pslObj.fullName = request.POST['canName']
                pslObj.dateFrom = datetime.datetime.strptime(request.POST['dateFrom'], '%m/%d/%Y')
                pslObj.dateTo = datetime.datetime.strptime(request.POST['dateTo'], '%m/%d/%Y')
                pslObj.ndtMethod = request.POST['NDTmethod']
                pslObj.totalHours = request.POST['totalHours']
                pslObj.employingOrganisation = request.POST['employingOrganisation']
                pslObj.reviewerName = request.POST['reviewerName']
                pslObj.reviewerDate = datetime.datetime.strptime(request.POST['reviewerDate'], '%m/%d/%Y')
                pslObj.finalEmployerDeclarationName = request.POST['finalEmployerDeclarationName']
                pslObj.dateCandidateDeclaration = datetime.datetime.strptime(request.POST['dateCandidateDeclaration'],
                                                                             '%m/%d/%Y')
                pslObj.save()

                if not request.POST.get('techniqueCodeR0', None) == None:
                    NdtTechniqueObj = NdtTechnique()
                    NdtTechniqueObj.candidate = candidate
                    NdtTechniqueObj.techniqueCode = request.POST['techniqueCodeR0']

                if not request.POST.get('employerComponentR0', None) == None:
                    NdtTechniqueObj.employerComponent = request.POST['employerComponentR0']

                if not request.POST.get('ndtTaskR0', None) == None:
                    NdtTechniqueObj.ndtTask = request.POST['ndtTaskR0']

                if not request.POST.get('experienceHoursR0', None) == None:
                    NdtTechniqueObj.experienceHours = request.POST['experienceHoursR0']

                if not request.POST.get('experienceConfirmedR0', None) == None:
                    NdtTechniqueObj.experienceConfirmed = request.POST['experienceConfirmedR0']

                if not request.POST.get('techniqueCodeR0', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                if not request.POST.get('techniqueCodeR1', None) == None:
                    NdtTechniqueObj = NdtTechnique()
                    NdtTechniqueObj.candidate = candidate
                    NdtTechniqueObj.techniqueCode = request.POST['techniqueCodeR1']

                if not request.POST.get('employerComponentR1', None) == None:
                    NdtTechniqueObj.employerComponent = request.POST['employerComponentR1']

                if not request.POST.get('ndtTaskR1', None) == None:
                    NdtTechniqueObj.ndtTask = request.POST['ndtTaskR1']

                if not request.POST.get('experienceHoursR1', None) == None:
                    NdtTechniqueObj.experienceHours = request.POST['experienceHoursR1']

                if not request.POST.get('experienceConfirmedR1', None) == None:
                    NdtTechniqueObj.experienceConfirmed = request.POST['experienceConfirmedR1']

                if not request.POST.get('techniqueCodeR1', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                if not request.POST.get('techniqueCodeR2', None) == None:
                    NdtTechniqueObj = NdtTechnique()
                    NdtTechniqueObj.candidate = candidate
                    NdtTechniqueObj.techniqueCode = request.POST['techniqueCodeR2']

                if not request.POST.get('employerComponentR2', None) == None:
                    NdtTechniqueObj.employerComponent = request.POST['employerComponentR2']

                if not request.POST.get('ndtTaskR2', None) == None:
                    NdtTechniqueObj.ndtTask = request.POST['ndtTaskR2']

                if not request.POST.get('experienceHoursR2', None) == None:
                    NdtTechniqueObj.experienceHours = request.POST['experienceHoursR2']
                if not request.POST.get('experienceConfirmedR2', None) == None:
                    NdtTechniqueObj.experienceConfirmed = request.POST['experienceConfirmedR2']

                if not request.POST.get('techniqueCodeR2', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                if not request.POST.get('techniqueCodeR3', None) == None:
                    NdtTechniqueObj = NdtTechnique()
                    NdtTechniqueObj.candidate = candidate
                    NdtTechniqueObj.techniqueCode = request.POST['techniqueCodeR3']

                if not request.POST.get('employerComponent3', None) == None:
                    NdtTechniqueObj.employerComponent = request.POST['employerComponentR3']

                if not request.POST.get('ndtTaskR3', None) == None:
                    NdtTechniqueObj.ndtTask = request.POST['ndtTaskR3']

                if not request.POST.get('experienceHoursR3', None) == None:
                    NdtTechniqueObj.experienceHours = request.POST['experienceHoursR3']

                if not request.POST.get('experienceConfirmedR3', None) == None:
                    NdtTechniqueObj.experienceConfirmed = request.POST['experienceConfirmedR3']

                if not request.POST.get('techniqueCodeR3', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                if not request.POST.get('techniqueCodeR4', None) == None:
                    NdtTechniqueObj = NdtTechnique()
                    NdtTechniqueObj.candidate = candidate
                    NdtTechniqueObj.techniqueCode = request.POST['techniqueCodeR4']

                if not request.POST.get('employerComponent4', None) == None:
                    NdtTechniqueObj.employerComponent = request.POST['employerComponentR4']

                if not request.POST.get('ndtTaskR4', None) == None:
                    NdtTechniqueObj.ndtTask = request.POST['ndtTaskR4']

                if not request.POST.get('experienceHoursR4', None) == None:
                    NdtTechniqueObj.experienceHours = request.POST['experienceHoursR4']

                if not request.POST.get('experienceConfirmedR4', None) == None:
                    NdtTechniqueObj.experienceConfirmed = request.POST['experienceConfirmedR4']

                if not request.POST.get('techniqueCodeR4', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                if not request.POST.get('techniqueCodeR4', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                if not request.POST.get('techniqueCodeR5', None) == None:
                    NdtTechniqueObj = NdtTechnique()
                    NdtTechniqueObj.candidate = candidate
                    NdtTechniqueObj.techniqueCode = request.POST['techniqueCodeR5']

                if not request.POST.get('employerComponentR5', None) == None:
                    NdtTechniqueObj.employerComponent = request.POST['employerComponentR5']

                if not request.POST.get('ndtTaskR5', None) == None:
                    NdtTechniqueObj.ndtTask = request.POST['ndtTaskR5']

                if not request.POST.get('experienceHoursR5', None) == None:
                    NdtTechniqueObj.experienceHours = request.POST['experienceHoursR5']

                if not request.POST.get('experienceConfirmedR5', None) == None:
                    NdtTechniqueObj.experienceConfirmed = request.POST['experienceConfirmedR5']

                if not request.POST.get('techniqueCodeR5', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                if not request.POST.get('techniqueCodeR6', None) == None:
                    NdtTechniqueObj = NdtTechnique()
                    NdtTechniqueObj.candidate = candidate
                    NdtTechniqueObj.techniqueCode = request.POST['techniqueCodeR6']

                if not request.POST.get('employerComponent6', None) == None:
                    NdtTechniqueObj.employerComponent = request.POST['employerComponentR6']

                if not request.POST.get('ndtTaskR6', None) == None:
                    NdtTechniqueObj.ndtTask = request.POST['ndtTaskR6']

                if not request.POST.get('experienceHoursR6', None) == None:
                    NdtTechniqueObj.experienceHours = request.POST['experienceHoursR6']

                if not request.POST.get('experienceConfirmedR6', None) == None:
                    NdtTechniqueObj.experienceConfirmed = request.POST['experienceConfirmedR6']

                if not request.POST.get('techniqueCodeR6', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                if not request.POST.get('techniqueCodeR6', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                if not request.POST.get('techniqueCodeR7', None) == None:
                    NdtTechniqueObj = NdtTechnique()
                    NdtTechniqueObj.candidate = candidate
                    NdtTechniqueObj.techniqueCode = request.POST['techniqueCodeR7']

                if not request.POST.get('employerComponent7', None) == None:
                    NdtTechniqueObj.employerComponent = request.POST['employerComponentR7']

                if not request.POST.get('ndtTaskR7', None) == None:
                    NdtTechniqueObj.ndtTask = request.POST['ndtTaskR7']

                if not request.POST.get('experienceHoursR7', None) == None:
                    NdtTechniqueObj.experienceHours = request.POST['experienceHoursR7']

                if not request.POST.get('experienceConfirmedR7', None) == None:
                    NdtTechniqueObj.experienceConfirmed = request.POST['experienceConfirmedR7']

                if not request.POST.get('techniqueCodeR7', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                if not request.POST.get('techniqueCodeR7', None) == None:
                    NdtTechniqueObj.save()
                    pslObj.ndtTechnique.add(NdtTechniqueObj)

                return redirect('forms:allpslform_')


class ViewPSL30LogExperienceForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/reg_forms/update_PSL_30_log_exper.html"

    def get_context_data(self, id):
        context = super(ViewPSL30LogExperienceForm, self).get_context_data()
        form = PSL30LogExp.objects.filter(id=self.kwargs['id']).first()
        context['form'] = form

        return context


class AllFormsList(SidebarMixin, TemplateView):
    template_name = "forms/all_forms_view.html"

    def get_context_data(self):
        context = super(AllFormsList, self).get_context_data()
        forms = Forms.objects.all()
        context['forms'] = forms
        return context


class AllForms(TemplateView):
    template_name = "forms/all_forms.html"

    def get_context_data(self):
        context = super(AllForms, self).get_context_data()
        forms = Forms.objects.all()
        context['forms'] = forms
        return context


class ViewForm(TemplateView):
    template_name = "forms/view_form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ViewForm, self).get_context_data()
        form = Forms.objects.filter(id=self.kwargs['id']).first()
        context['form'] = form
        return context


class ViewFormByID(TemplateView):
    template_name = "forms/reg_forms/twi_enrolment_by_id.html"

    def get_context_data(self, *args, **kwargs):
        """

        Args:
            *args:
            **kwargs:

        Returns:

        """
        context = super(ViewFormByID, self).get_context_data()
        canID = self.kwargs['id']
        candidate = TesCandidate.objects.filter(id=canID).first()
        print(canID)
        print(candidate.id)
        form = TwiEnrolmentForm.objects.filter(candidate=candidate).first()
        context['form'] = form
        return context


class ViewFormByFormID(SidebarMixin, TemplateView):
    template_name = "forms/reg_forms/twi_enrolment_by_id.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ViewFormByFormID, self).get_context_data()
        id = self.kwargs['id']

        print(id)

        form = TwiEnrolmentForm.objects.filter(id=id).first()
        context['form'] = form
        return context


class ViewFormByFormIDSum(SidebarMixin, TemplateView):
    template_name = "forms/reg_forms/twi_enrolment_by_id.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ViewFormByFormIDSum, self).get_context_data()
        print('Here')
        canID = self.kwargs['canID']
        eventID = self.kwargs['eventID']
        guideID = self.kwargs['guideID']
        catID = self.kwargs['catID']

        candidate = TesCandidate.objects.filter(id=canID).first()
        event = Event.objects.filter(id=eventID).first()
        guideline = Guideline.objects.filter(id=guideID).first()
        category = Category.objects.filter(id=catID).first()

        print(canID)
        print(eventID)
        print(guideID)
        print(catID)
        #
        formList = FormList.objects.filter(
            Q(event=event) & Q(guideline=guideline) & Q(category=category) & Q(candidate=candidate)).last()
        model_name = formList.name
        app_name = 'forms'
        from django.apps import apps
        twienrolmentform = apps.get_model(app_label=app_name, model_name=model_name)
        form = twienrolmentform.objects.filter(id=formList.FormID).first()

        context['form'] = form
        return context


class AllFormsFromPostgres(TemplateView):
    template_name = "forms/all_forms_postres.html"

    def get_context_data(self):
        context = super(AllFormsFromPostgres, self).get_context_data()
        formObj = FormDb()
        tList = formObj.TableLists()
        context['tList'] = tList
        return context


class sigDrawer(SidebarMixin, TemplateView):
    template_name = "forms/draw_sig.html"
    candidateID = None

    def get_context_data(self, *args, **kwargs):
        context = super(sigDrawer, self).get_context_data()

        return context


class uploadSignature(SidebarMixin, TemplateView):
    template_name = "forms/uploud_sig.html"
    candidateID = None

    def get_context_data(self, id, *args, **kwargs):
        context = super(uploadSignature, self).get_context_data()
        print(self.kwargs['id'])
        return context

    def post(self, request, id, *args, **kwargs):

        if request.method == 'POST':
            if request.FILES.get('imageFile', False):
                print(self.kwargs['id'])
                formObj = TwiEnrolmentForm.objects.filter(id=self.kwargs['id']).first()
                formObj.uploadedSign = request.FILES['imageFile']
                formObj.save()

        return redirect('forms:allenrolmentform_')


class formMap(TemplateView):
    template_name = "forms/form_map.html"

    def get_context_data(self, *args, **kwargs):
        context = super(formMap, self).get_context_data()
        tags = Category.objects.all()

        context['tags'] = tags
        return context


class FormMapByCatID(TemplateView):
    template_name = "forms/form_map_by_id.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FormMapByCatID, self).get_context_data()
        catID = self.kwargs['id']
        print(catID)
        tag = Category.objects.filter(id=catID).first()
        context['tag'] = tag
        return context


class UploadForm(SidebarMixin, TemplateView):
    template_name = "forms/uploud_form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UploadForm, self).get_context_data()
        context['id'] = self.kwargs['id']
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            formID = request.POST['formID']
            if request.FILES.get('myFile', False):
                print(formID)
                formObj = TwiEnrolmentForm.objects.filter(id=formID).first()
                formObj.uploadedForm = request.FILES['myFile']
                formObj.save()

        return redirect('forms:allenrolmentform_')


class EachFormMemebr(TemplateView):
    template_name = "forms/categoried_form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EachFormMemebr, self).get_context_data()
        eventID = self.kwargs['id']
        event = Event.objects.filter(id=eventID).first()
        general = General.objects.filter(event=event).first()
        form = TwiEnrolmentForm.objects.all()
        # canList = TesCandidate.objects.filter(forms=form)
        # context['canList'] = canList
        context['form'] = form
        context['general'] = general
        return context


class EventSummary(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/event_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventSummary, self).get_context_data()
        eventID = self.kwargs['id']
        twiForm = TwiEnrolmentForm.objects.filter(eventID=eventID)
        event = Event.objects.filter(id=eventID).first()
        # generalObj = General.objects.filter(event=event).first()
        eventConfirm = TwiEnrolmentForm.objects.filter(Q(eventID=eventID) & Q(confirmation=True))

        print('OK here')
        # tag = Category.objects.filter(id=event.formCategory.id).first()

        candidateList = event.candidate.all()
        # submitedList = generalObj.twiEnrolmentForm.all()
        list1 = []
        list2 = []
        for item in candidateList:
            print(item.tes_candidate_id)
            list1.append(item.tes_candidate_id)

        # print("====")
        # for item in submitedList:
        #     print(item.candidate.tes_candidate_id)
        #     list2.append(item.candidate.tes_candidate_id)

        resultList = list(set(list1).difference(list2))
        unsubmited = TesCandidate.objects.filter(tes_candidate_id__in=resultList)

        print(resultList)
        # context['tag'] = tag
        # context['form'] = generalObj.twiEnrolmentForm.all()
        context['event'] = event
        context['eventConfirm'] = eventConfirm
        # context['generalObj'] = generalObj
        context['unsubmited'] = unsubmited
        return context


class EventSummaryByFormId(SidebarMixin, TemplateView):
    template_name = "forms/event_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventSummaryByFormId, self).get_context_data()

        eventID = self.kwargs['eventID']
        catID = self.kwargs['catID']
        guideID = self.kwargs['guideID']
        # canID = self.kwargs['canID']
        print("Now")
        submitedList = None

        event = Event.objects.filter(id=eventID).first()
        category = Category.objects.filter(id=catID).first()
        guideline = Guideline.objects.filter(id=guideID).first()

        eventSubmit = FormList.objects.filter(Q(event=event) & Q(guideline=guideline) & Q(category=category))
        eventConfirm = FormList.objects.filter(
            Q(event=event) & Q(guideline=guideline) & Q(category=category) & Q(status=True))

        # tag = Category.objects.filter(id=catID).first()
        candidateList = event.candidate.all()

        submittedList1 = []
        allList = []
        for item in candidateList:
            print(item.tes_candidate_id)
            allList.append(item.tes_candidate_id)

        print("====")
        for item in eventSubmit:
            print(item.candidate.tes_candidate_id)
            submittedList1.append(item.candidate.tes_candidate_id)

        resultList = list(set(allList).difference(submittedList1))
        unsubmited = TesCandidate.objects.filter(tes_candidate_id__in=resultList)

        # context['tag'] = tag
        context['event'] = event
        context['eventConfirm'] = eventConfirm
        context['eventSubmit'] = eventSubmit
        # context['form'] = form
        context['unsubmited'] = unsubmited

        return context


class NDT15AExperienceVerificationView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/ndt/ndt_15_S.html"

    def get_context_data(self):
        context = super(NDT15AExperienceVerificationView, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()

                obj = NDT15AExperienceVerification()
                obj.candidate = candidate
                obj.category = category
                obj.guideline = guideline
                obj.event = event
                obj.descriptionOfExperience = request.POST['descriptionOfExperience']
                obj.date = datetime.datetime.strptime(request.POST['date'], '%m/%d/%Y')
                obj.nameJobTitle = request.POST['nameJobTitle']
                obj.companyName = request.POST['companyName']
                obj.supervisionActivity = request.POST['supervisionActivity']
                obj.verEmail = request.POST['verEmail']

                obj.verDate = datetime.datetime.strptime(request.POST['verDate'], '%m/%d/%Y')
                obj.save()

                if request.POST['methodLevel']:
                    objCurrent = CurrentFormerCertification()
                    objCurrent.methodLevel = request.POST['methodLevel']
                    objCurrent.SchemeCertifyingAuthority = request.POST['SchemeCertifyingAuthority']
                    objCurrent.ExpiryDate = datetime.datetime.strptime(request.POST['ExpiryDate'], '%m/%d/%Y')
                    objCurrent.save()
                    obj.currentFormerCertification.add(objCurrent)

                if request.POST['methodLevel2']:
                    objCurrent = CurrentFormerCertification()
                    objCurrent.methodLevel = request.POST['methodLevel2']
                    objCurrent.SchemeCertifyingAuthority = request.POST['SchemeCertifyingAuthority2']
                    objCurrent.ExpiryDate = datetime.datetime.strptime(request.POST['ExpiryDate2'], '%m/%d/%Y')
                    objCurrent.save()
                    obj.currentFormerCertification.add(objCurrent)

                if request.POST['claimedMethodLevel']:
                    objClaimed = ExperienceClaimed()
                    objClaimed.methodLevel = request.POST['claimedMethodLevel']
                    objClaimed.ExperienceClaimedSince = request.POST['ExperienceClaimedSince']
                    objClaimed.NumberOfNonths = request.POST['NumberOfNonths']
                    objClaimed.DateOfExamination = datetime.datetime.strptime(request.POST['DateOfExamination'],
                                                                              '%m/%d/%Y')
                    objClaimed.save()
                    obj.experienceClaimed.add(objClaimed)

                if request.POST['claimedMethodLevel2']:
                    objClaimed = ExperienceClaimed()
                    objClaimed.methodLevel = request.POST['claimedMethodLevel2']
                    objClaimed.ExperienceClaimedSince = request.POST['ExperienceClaimedSince2']
                    objClaimed.NumberOfNonths = request.POST['NumberOfNonths2']
                    objClaimed.DateOfExamination = datetime.datetime.strptime(request.POST['DateOfExamination2'],
                                                                              '%m/%d/%Y')
                    objClaimed.save()
                    obj.experienceClaimed.add(objClaimed)

                if request.POST['claimedMethodLevel3']:
                    objClaimed = ExperienceClaimed()
                    objClaimed.methodLevel = request.POST['claimedMethodLevel3']
                    objClaimed.ExperienceClaimedSince = request.POST['ExperienceClaimedSince3']
                    objClaimed.NumberOfNonths = request.POST['NumberOfNonths3']
                    objClaimed.DateOfExamination = datetime.datetime.strptime(request.POST['DateOfExamination3'],
                                                                              '%m/%d/%Y')
                    objClaimed.save()
                    obj.experienceClaimed.add(objClaimed)

                obj.descriptionOfExperience = request.POST['descriptionOfExperience']
                obj.date = request.POST['date']
                obj.nameJobTitle = request.POST['nameJobTitle']
                obj.companyName = request.POST['companyName']
                obj.supervisionActivity = request.POST['supervisionActivity']
                obj.verEmail = request.POST['verEmail']

                formListObj = FormList()
                formListObj.name = obj.__class__.__name__
                formListObj.event = event
                formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = obj.id
                formListObj.save()

                return redirect('forms:updatendt15_', id=obj.id)


            else:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                print(canID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                self.candidateID = candidate.id
                print(self.candidateID)
                context = super(NDT15AExperienceVerificationView, self).get_context_data()
                context['candidate'] = candidate
                context['category'] = category
                context['event'] = event
                context['guideline'] = guideline

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/ndt/ndt_15_S.html', context)


class DeleteNdt15A(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = NDT15AExperienceVerification
    success_url = reverse_lazy('forms:allndt15expver_')


class AllNDT15AExpVerView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/ndt/all_ndt_15.html"

    def get_context_data(self):
        context = super(AllNDT15AExpVerView, self).get_context_data()
        forms = NDT15AExperienceVerification.objects.all()
        context['forms'] = forms
        return context


class ViewNDT15FormByID(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/ndt/ndt_15_byid.html"

    def get_context_data(self, *args, **kwargs):
        """

        Args:
            *args:
            **kwargs:

        Returns:

        """
        context = super(ViewNDT15FormByID, self).get_context_data()
        formID = self.kwargs['id']
        form = NDT15AExperienceVerification.objects.filter(id=formID).last()
        context['form'] = form
        return context


class UpdateNDT15AExpVerView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/ndt/update_ndt_15.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(UpdateNDT15AExpVerView, self).get_context_data()
        formID = self.kwargs['id']
        form = NDT15AExperienceVerification.objects.filter(id=formID).last()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:

                obj = NDT15AExperienceVerification.objects.filter(id=id).first()
                obj.candidateID = request.POST['cancanID']
                obj.descriptionOfExperience = request.POST['descriptionOfExperience']
                obj.date = datetime.datetime.strptime(request.POST['date'], '%m/%d/%Y')
                obj.nameJobTitle = request.POST['nameJobTitle']
                obj.companyName = request.POST['companyName']
                obj.supervisionActivity = request.POST['supervisionActivity']
                obj.verEmail = request.POST['verEmail']
                obj.verDate = datetime.datetime.strptime(request.POST['verDate'], '%m/%d/%Y')
                obj.save()

                for idx, item in enumerate(range(0, 8)):
                    if not request.POST.get('methodLevel'+ str(idx+1), None) == None:
                        id = request.POST['id'+ str(idx+1)]
                        print(id)
                        print(request.POST['ExpiryDate' + str(idx + 1)])
                        objCur = CurrentFormerCertification.objects.filter(id=id).first()
                        objCur.methodLevel = request.POST['methodLevel'+ str(idx+1)]
                        objCur.SchemeCertifyingAuthority = request.POST['SchemeCertifyingAuthority'+ str(idx+1)]
                        objCur.ExpiryDate = datetime.datetime.strptime(request.POST['ExpiryDate' + str(idx + 1)], '%m/%d/%Y')
                        objCur.save()

                for idx, item in enumerate(range(0, 8)):
                    if not request.POST.get('claimedMethodLevel'+ str(idx+1), None) == None:
                        id = request.POST['expID'+ str(idx+1)]
                        print(id)
                        objExp = ExperienceClaimed.objects.filter(id=id).first()
                        objExp.methodLevel = request.POST['claimedMethodLevel'+ str(idx+1)]
                        objExp.ExperienceClaimedSince = request.POST['ExperienceClaimedSince'+ str(idx+1)]
                        objExp.NumberOfNonths = request.POST['NumberOfNonths'+ str(idx+1)]
                        objExp.ExpiryDate = datetime.datetime.strptime(request.POST['DateOfExamination' + str(idx + 1)], '%m/%d/%Y')
                        objExp.save()

                return redirect('forms:allndt15expver_')

            if 'uploadFormBack' in request.POST:
                print('uploadFormBack')
                obj = NDT15AExperienceVerification.objects.filter(id=id).first()
                obj.file = request.FILES['pdfFile']
                obj.save()
                return redirect('forms:allndt15expver_')

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/ndt/ndt_15.html', context)


class NDTCovid19View(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/ndt/covid_19_S.html"

    def get_context_data(self):
        context = super(NDTCovid19View, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("mainFOrm")
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                print(request.POST['mainCanID'])
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()

                obj = NDTCovid19()
                obj.candidate = candidate
                obj.category = category
                obj.guideline = guideline
                obj.event = event
                obj.candidateID = request.POST['cancanID']
                obj.candidateAdress = request.POST['candidateAddress']
                obj.candidateHomePhone = request.POST['candidateHomePhone']
                obj.fillingDate = datetime.datetime.strptime(request.POST['fillingDate'], '%m/%d/%Y')

                if not request.POST.get('case1yes', None) == None:
                    obj.confirmCase1 = True
                if not request.POST.get('case1No', None) == None:
                    obj.confirmCase1 = False

                if not request.POST.get('case2yes', None) == None:
                    obj.confirmCase2 = True
                if not request.POST.get('case2No', None) == None:
                    obj.confirmCase2 = False

                if not request.POST.get('case3yes', None) == None:
                    obj.confirmCase3 = True
                if not request.POST.get('case3No', None) == None:
                    obj.confirmCase3 = False

                if not request.POST.get('case4yes', None) == None:
                    obj.confirmCase4 = True
                if not request.POST.get('case4No', None) == None:
                    obj.confirmCase4 = False

                if not request.POST.get('case5yes', None) == None:
                    obj.confirmCase5 = True
                if not request.POST.get('case5No', None) == None:
                    obj.confirmCase5 = False

                if not request.POST.get('case6yes', None) == None:
                    obj.confirmCase6 = True
                if not request.POST.get('case6No', None) == None:
                    obj.confirmCase6 = False

                if not request.POST.get('medicalTravelCase1Yes', None) == None:
                    obj.medicalTravelCase1 = True
                if not request.POST.get('medicalTravelCase1No', None) == None:
                    obj.medicalTravelCase1 = False
                # obj.medicalHistory = request.POST['medicalHistory']

                if not request.POST.get('medicalTravelCase2Yes', None) == None:
                    obj.medicalTravelCase2 = True
                if not request.POST.get('medicalTravelCase2No', None) == None:
                    obj.medicalTravelCase2 = False
                # obj.temperature = request.POST['temperature']

                if not request.POST.get('medicalTravelCase3Yes', None) == None:
                    obj.medicalTravelCase3 = True
                if not request.POST.get('medicalTravelCase3No', None) == None:
                    obj.medicalTravelCase3 = False

                if not request.POST.get('medicalTravelCase4Yes', None) == None:
                    obj.medicalTravelCase4 = True
                if not request.POST.get('medicalTravelCase4No', None) == None:
                    obj.medicalTravelCase4 = False

                obj.outsideCountry = request.POST['outsideCountry']
                obj.temperature = request.POST['temperature']
                obj.medicalHistory = request.POST['medicalHistory']
                obj.afterEventDate = datetime.datetime.strptime(request.POST['afterEventDate'], '%m/%d/%Y')

                obj.save()

                formListObj = FormList()
                formListObj.name = obj.__class__.__name__
                formListObj.event = event
                formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = obj.id
                formListObj.save()


                return redirect('forms:updatecovid19_', id=obj.id)

            # if 'uploadFormBack' in request.POST:
            #     print('uploadFormBack')
            #
            #     file = request.FILES['file']
            #     print(file)
            #
            #     canID = request.POST['mainCanID']
            #     eventID = request.POST['eventID']
            #     categoryID = request.POST['categoryID']
            #     guidelineID = request.POST['guidelineID']
            #
            #
            #     candidate = TesCandidate.objects.filter(id=canID).first()
            #     event = Event.objects.filter(id=eventID).first()
            #     category = Category.objects.filter(id=categoryID).first()
            #     guideline = Guideline.objects.filter(id=guidelineID).first()
            #     context = super(NDTCovid19View, self).get_context_data()
            #     context['candidate'] = candidate
            #     context['category'] = category
            #     context['event'] = event
            #     context['guideline'] = guideline
            #
            # # return redirect('forms:jaegertofdl2_' ,context)
            #     return render(request, 'forms/ndt/covid_19_S.html', context)
            else:
                print('Here55')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['selectedEventID']
                categoryID = request.POST['selectedCategoryID']
                guidelineID = request.POST['seletedGuidelineID']
                print(guidelineID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                self.candidateID = candidate.id
                print(self.candidateID)
                context = super(NDTCovid19View, self).get_context_data()
                context['candidate'] = candidate
                context['category'] = category
                context['event'] = event
                context['guideline'] = guideline

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/ndt/covid_19_S.html', context)


class AllNDT15Covid19View(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/ndt/all_ndt_covid19.html"

    def get_context_data(self):
        context = super(AllNDT15Covid19View, self).get_context_data()
        forms = NDTCovid19.objects.all()
        context['forms'] = forms
        return context


class DeleteCovid19(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = NDTCovid19
    success_url = reverse_lazy('forms:allndtcovid19_')


class ViewNDTCovid19FormByID(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/ndt/covid_19_by_id.html"

    def get_context_data(self, *args, **kwargs):
        """

        Args:
            *args:
            **kwargs:

        Returns:

        """
        context = super(ViewNDTCovid19FormByID, self).get_context_data()
        formID = self.kwargs['id']
        form = NDTCovid19.objects.filter(id=formID).first()
        context['form'] = form
        return context


class UpdateNDTCovid19View(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/ndt/covid_19_update.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(UpdateNDTCovid19View, self).get_context_data()
        print("here")
        formID = self.kwargs['id']
        form = NDTCovid19.objects.filter(id=formID).first()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("Here")

                obj = NDTCovid19.objects.filter(id=id).first()
                obj.candidateID = request.POST['candidateID']
                obj.candidateAdress = request.POST['candidateAddress']
                obj.candidateHomePhone = request.POST['candidateHomePhone']
                obj.fillingDate = datetime.datetime.strptime(request.POST['fillingDate'], '%m/%d/%Y')

                if not request.POST.get('case1yes', None) == None:
                    obj.confirmCase1 = True
                if not request.POST.get('case1No', None) == None:
                    obj.confirmCase1 = False

                if not request.POST.get('case2yes', None) == None:
                    obj.confirmCase2 = True
                if not request.POST.get('case2No', None) == None:
                    obj.confirmCase2 = False

                if not request.POST.get('case3yes', None) == None:
                    obj.confirmCase3 = True
                if not request.POST.get('case3No', None) == None:
                    obj.confirmCase3 = False

                if not request.POST.get('case4yes', None) == None:
                    obj.confirmCase4 = True
                if not request.POST.get('case4No', None) == None:
                    obj.confirmCase4 = False

                if not request.POST.get('case5yes', None) == None:
                    obj.confirmCase5 = True
                if not request.POST.get('case5No', None) == None:
                    obj.confirmCase5 = False

                if not request.POST.get('case6yes', None) == None:
                    obj.confirmCase6 = True
                if not request.POST.get('case6No', None) == None:
                    obj.confirmCase6 = False

                if not request.POST.get('medicalTravelCase1Yes', None) == None:
                    obj.medicalTravelCase1 = True
                if not request.POST.get('medicalTravelCase1No', None) == None:
                    obj.medicalTravelCase1 = False
                obj.medicalHistory = request.POST['medicalHistory']

                if not request.POST.get('medicalTravelCase2Yes', None) == None:
                    obj.medicalTravelCase2 = True
                if not request.POST.get('medicalTravelCase2No', None) == None:
                    obj.medicalTravelCase2 = False
                obj.temperature = request.POST['temperature']

                if not request.POST.get('medicalTravelCase3Yes', None) == None:
                    obj.medicalTravelCase3 = True
                if not request.POST.get('medicalTravelCase3No', None) == None:
                    obj.medicalTravelCase3 = False

                if not request.POST.get('medicalTravelCase4Yes', None) == None:
                    obj.medicalTravelCase4 = True
                if not request.POST.get('medicalTravelCase4No', None) == None:
                    obj.medicalTravelCase4 = False

                obj.afterEventDate = datetime.datetime.strptime(request.POST['afterEventDate'], '%m/%d/%Y')

                obj.save()

                return redirect('forms:allndtcovid19_')

            if 'uploadFormBack' in request.POST:
                print('uploadFormBack')
                obj = NDTCovid19.objects.filter(id=id).first()
                obj.file = request.FILES['pdfFile']
                obj.save()
                return redirect('forms:allndtcovid19_')

                # return render(request, 'forms/ndt/covid_19_S.html', context)
            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/ndt/covid_19.html', context)


class MSGUpdateNDTCovid19View(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/ndt/covid_19_update.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(MSGUpdateNDTCovid19View, self).get_context_data()
        print("here")
        formID = self.kwargs['id']
        form = NDTCovid19.objects.filter(id=formID).first()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("Here")

                obj = NDTCovid19.objects.filter(id=id).first()
                obj.candidateID = request.POST['candidateID']
                obj.candidateAdress = request.POST['candidateAddress']
                obj.candidateHomePhone = request.POST['candidateHomePhone']
                obj.fillingDate = datetime.datetime.strptime(request.POST['fillingDate'], '%m/%d/%Y')

                if not request.POST.get('case1yes', None) == None:
                    obj.confirmCase1 = True
                if not request.POST.get('case1No', None) == None:
                    obj.confirmCase1 = False

                if not request.POST.get('case2yes', None) == None:
                    obj.confirmCase2 = True
                if not request.POST.get('case2No', None) == None:
                    obj.confirmCase2 = False

                if not request.POST.get('case3yes', None) == None:
                    obj.confirmCase3 = True
                if not request.POST.get('case3No', None) == None:
                    obj.confirmCase3 = False

                if not request.POST.get('case4yes', None) == None:
                    obj.confirmCase4 = True
                if not request.POST.get('case4No', None) == None:
                    obj.confirmCase4 = False

                if not request.POST.get('case5yes', None) == None:
                    obj.confirmCase5 = True
                if not request.POST.get('case5No', None) == None:
                    obj.confirmCase5 = False

                if not request.POST.get('case6yes', None) == None:
                    obj.confirmCase6 = True
                if not request.POST.get('case6No', None) == None:
                    obj.confirmCase6 = False

                if not request.POST.get('medicalTravelCase1Yes', None) == None:
                    obj.medicalTravelCase1 = True
                if not request.POST.get('medicalTravelCase1No', None) == None:
                    obj.medicalTravelCase1 = False
                obj.medicalHistory = request.POST['medicalHistory']

                if not request.POST.get('medicalTravelCase2Yes', None) == None:
                    obj.medicalTravelCase2 = True
                if not request.POST.get('medicalTravelCase2No', None) == None:
                    obj.medicalTravelCase2 = False
                obj.temperature = request.POST['temperature']

                if not request.POST.get('medicalTravelCase3Yes', None) == None:
                    obj.medicalTravelCase3 = True
                if not request.POST.get('medicalTravelCase3No', None) == None:
                    obj.medicalTravelCase3 = False

                if not request.POST.get('medicalTravelCase4Yes', None) == None:
                    obj.medicalTravelCase4 = True
                if not request.POST.get('medicalTravelCase4No', None) == None:
                    obj.medicalTravelCase4 = False

                obj.afterEventDate = datetime.datetime.strptime(request.POST['afterEventDate'], '%m/%d/%Y')

                obj.save()

                return redirect('forms:allndtcovid19_')

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/ndt/covid_19.html', context)


class NewPSL57B(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/reg_forms/psl_57B_S.html"

    def get_context_data(self):
        context = super(NewPSL57B, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()

                objPSL57 = PSL57B()
                objPSL57.candidate = candidate
                objPSL57.category = category
                objPSL57.guideline = guideline
                objPSL57.event = event

                if not request.POST.get('contactMe', None) == None:
                    objPSL57.contactMe = True
                if not request.POST.get('contactMe', None) == None:
                    objPSL57.contactMe = False

                objPSL57.cerAddress = request.POST['cerAddress']
                objPSL57.pslCerAddress = request.POST['pslCerAddress']
                objPSL57.phone = request.POST['phone']
                objPSL57.email = request.POST['email']
                objPSL57.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%m/%d/%Y')
                objPSL57.currentEmploymentDetails = request.POST['currentEmploymentDetails']
                objPSL57.candidatePosition = request.POST['currentEmploymentPosition']
                objPSL57.employmentStatus = request.POST['currentEmploymentStatus']
                objPSL57.examinationType = request.POST['examinationType']
                objPSL57.iroductsIndustrySector = request.POST['iroductsIndustrySector']

                if not request.POST.get('mt', None) == None:
                    objPSL57.NDTMethod = 'MT'

                if not request.POST.get('pt', None) == None:
                    objPSL57.NDTMethod = 'PT'

                if not request.POST.get('rt', None) == None:
                    objPSL57.NDTMethod = 'RT'

                if not request.POST.get('ri', None) == None:
                    objPSL57.NDTMethod = 'RI'

                if not request.POST.get('ui', None) == None:
                    objPSL57.NDTMethod = 'UI'

                if not request.POST.get('vt', None) == None:
                    objPSL57.NDTMethod = 'VT'

                if not request.POST.get('crt', None) == None:
                    objPSL57.NDTMethod = 'CRT'

                if not request.POST.get('tofd', None) == None:
                    objPSL57.NDTMethod = 'TOFD'

                if not request.POST.get('puat', None) == None:
                    objPSL57.NDTMethod = 'PAUT'

                if not request.POST.get('levelOne', None) == None:
                    objPSL57.NDTLevel = 'Level 1'

                if not request.POST.get('levelTwo', None) == None:
                    objPSL57.NDTLevel = 'Level 2'

                if not request.POST.get('levelThree', None) == None:
                    objPSL57.NDTLevel = 'Level 3'

                objPSL57.ifLevel3 = request.POST['ifLevel3']
                objPSL57.categoriesOfCertification = request.POST['categoriesOfCertification']
                objPSL57.recertification = request.POST['recertification']
                objPSL57.preferredExaminationDateVenu = request.POST['preferredExaminationDateVenue']

                objPSL57.nameAddressInvoice = request.POST['nameAddressInvoice']
                objPSL57.paymentMethod = request.POST['paymentMethod']


                if not request.POST.get('cheque', None) == None:
                    objPSL57.cheque = True
                objPSL57.nameResponsible = request.POST['nameResponsible']
                objPSL57.accommodation = request.POST['accommodation']
                objPSL57.companyOrderReference = request.POST['companyOrderReference']

                if not request.POST.get('visa', None) == None:
                    objPSL57.creditCardPayment = 'Visa'
                if not request.POST.get('masterCard', None) == None:
                    objPSL57.creditCardPayment = 'MasterCard'
                if not request.POST.get('amex', None) == None:
                    objPSL57.creditCardPayment = 'Amex'
                if not request.POST.get('switch', None) == None:
                    objPSL57.creditCardPayment = 'Switch'

                objPSL57.issueExpiryDates = datetime.datetime.strptime(request.POST['issueExpiryDates'], '%m/%d/%Y')
                objPSL57.NameOnCard = request.POST['NameOnCard']
                objPSL57.cardNumber = request.POST['cardNumber']
                objPSL57.securityCode = request.POST['securityCode']
                objPSL57.addressCreditCardHolder = request.POST['addressCreditCardHolder']
                objPSL57.debit = request.POST['debit']
                objPSL57.save()



                formListObj = FormList()
                formListObj.name = objPSL57.__class__.__name__
                formListObj.event = event
                formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = objPSL57.id
                formListObj.save()

                for idx,item in enumerate(range(0,4)):
                    if not request.POST.get('organisation'+str(idx), None) == None:
                        obj = empHistory()
                        obj.organisation = request.POST['organisation'+str(idx)]
                        obj.period = request.POST['period'+str(idx)]
                        obj.contactNamePhone = request.POST['contactNamePhone'+str(idx)]
                        obj.save()
                        objPSL57.emphistory.add(obj)


                return redirect('forms:allpsl57b_')


            else:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['cancanID']
                eventID = request.POST['eventٍEvID']
                categoryID = request.POST['categoryCatID']
                guidelineID = request.POST['guidelineGuiID']
                print(canID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                self.candidateID = candidate.id
                print(self.candidateID)
                context = super(NewPSL57B, self).get_context_data()
                context['candidate'] = candidate
                context['category'] = category
                context['event'] = event
                context['guideline'] = guideline

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/reg_forms/psl_57B_S.html', context)


class AllPSL57BView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_psl_57b.html"

    def get_context_data(self):
        context = super(AllPSL57BView, self).get_context_data()
        forms = PSL57B.objects.all()
        context['forms'] = forms
        return context


class DeletePSL57B(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = PSL57B
    success_url = reverse_lazy('forms:allpsl57b_')


class UpdatePSL57B(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/update_psl_57B.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(UpdatePSL57B, self).get_context_data()
        id = self.kwargs['id']
        form = PSL57B.objects.filter(id=id).first()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:

                objPSL57 = PSL57B.objects.filter(id=id).first()
                if not request.POST.get('contactMe', None) == None:
                    objPSL57.contactMe = True
                if not request.POST.get('contactMe', None) == None:
                    objPSL57.contactMe = False

                objPSL57.cerAddress = request.POST['cerAddress']
                objPSL57.pslCerAddress = request.POST['pslCerAddress']
                objPSL57.phone = request.POST['phone']
                objPSL57.email = request.POST['email']
                objPSL57.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%m/%d/%Y')
                objPSL57.currentEmploymentDetails = request.POST['currentEmploymentDetails']
                objPSL57.candidatePosition = request.POST['currentEmploymentPosition']
                objPSL57.employmentStatus = request.POST['currentEmploymentStatus']
                objPSL57.examinationType = request.POST['examinationType']
                objPSL57.iroductsIndustrySector = request.POST['iroductsIndustrySector']

                if not request.POST.get('MT', None) == None:
                    objPSL57.NDTMethod = 'MT'

                if not request.POST.get('PT', None) == None:
                    objPSL57.NDTMethod = 'PT'

                if not request.POST.get('RT', None) == None:
                    objPSL57.NDTMethod = 'RT'

                if not request.POST.get('RI', None) == None:
                    objPSL57.NDTMethod = 'RI'

                if not request.POST.get('UI', None) == None:
                    objPSL57.NDTMethod = 'UI'

                if not request.POST.get('VT', None) == None:
                    objPSL57.NDTMethod = 'VT'

                if not request.POST.get('CRT', None) == None:
                    objPSL57.NDTMethod = 'CRT'

                if not request.POST.get('TOFD', None) == None:
                    objPSL57.NDTMethod = 'TOFD'

                if not request.POST.get('PAUT', None) == None:
                    objPSL57.NDTMethod = 'PAUT'

                if not request.POST.get('one', None) == None:
                    objPSL57.NDTLevel = 'Level 1'

                if not request.POST.get('two', None) == None:
                    objPSL57.NDTLevel = 'Level 2'

                if not request.POST.get('three', None) == None:
                    objPSL57.NDTLevel = 'Level 3'

                objPSL57.ifLevel3 = request.POST['ifLevel3']
                objPSL57.categoriesOfCertification = request.POST['categoriesOfCertification']
                objPSL57.recertification = request.POST['recertification']
                objPSL57.preferredExaminationDateVenu = request.POST['preferredExaminationDateVenu']

                objPSL57.nameAddressInvoice = request.POST['nameAddressInvoice']
                objPSL57.paymentMethod = request.POST['paymentMethod']
                if not request.POST.get('cheque', None) == None:
                    objPSL57.cheque = True
                objPSL57.nameResponsible = request.POST['nameResponsible']
                objPSL57.accommodation = request.POST['accommodation']
                objPSL57.companyOrderReference = request.POST['companyOrderReference']

                if not request.POST.get('visa', None) == None:
                    objPSL57.creditCardPayment = 'Visa'
                if not request.POST.get('masterCard', None) == None:
                    objPSL57.creditCardPayment = 'MasterCard'
                if not request.POST.get('amex', None) == None:
                    objPSL57.creditCardPayment = 'Amex'
                if not request.POST.get('switch', None) == None:
                    objPSL57.creditCardPayment = 'Switch'

                objPSL57.issueExpiryDates = datetime.datetime.strptime(request.POST['issueExpiryDates'], '%m/%d/%Y')
                objPSL57.NameOnCard = request.POST['NameOnCard']
                objPSL57.cardNumber = request.POST['cardNumber']
                objPSL57.securityCode = request.POST['securityCode']
                objPSL57.addressCreditCardHolder = request.POST['addressCreditCardHolder']
                objPSL57.debit = request.POST['debit']
                objPSL57.save()

                if not request.POST.get('organisation1', None) == None:
                    historyObj = empHistory()
                    historyObj.organisation = request.POST['organisation1']
                    historyObj.period = request.POST['period1']
                    historyObj.contactNamePhone = request.POST['contactNamePhone1']
                    historyObj.save()
                    objPSL57.emphistory.add(historyObj)

                if not request.POST.get('organisation2', None) == None:
                    historyObj = empHistory()
                    historyObj.organisation = request.POST['organisation2']
                    historyObj.period = request.POST['period2']
                    historyObj.contactNamePhone = request.POST['contactNamePhone2']
                    historyObj.save()
                    objPSL57.emphistory.add(historyObj)

                if not request.POST.get('organisation3', None) == None:
                    historyObj = empHistory()
                    historyObj.organisation = request.POST['organisation3']
                    historyObj.period = request.POST['period3']
                    historyObj.contactNamePhone = request.POST['contactNamePhone3']
                    historyObj.save()
                    objPSL57.emphistory.add(historyObj)

                return redirect('forms:allpsl57b_')

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/psl_57B.html', context)


class ViewPSL57B(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/view_psl_57B.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(ViewPSL57B, self).get_context_data()
        id = self.kwargs['id']
        form = PSL57B.objects.filter(id=id).first()
        context['form'] = form
        return context


class NewVisionTest(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/vision_test.html"

    def get_context_data(self):
        context = super(NewVisionTest, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()

                visionObj = VisionTest()
                visionObj.candidate = candidate
                visionObj.category = category
                visionObj.guideline = guideline
                visionObj.event = event
                #
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =True
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =False

                visionObj.address = request.POST['candidateAdress']
                visionObj.phone = request.POST['candidateHomePhone']
                visionObj.email = request.POST['email']
                visionObj.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%m/%d/%Y')
                visionObj.employer = request.POST['employeer']
                visionObj.tumbling = request.POST['tumbling']

                if not request.POST.get('uncorrected', None) == None:
                    visionObj.nearVisionAcuity = 'UNCORRECTED'

                if not request.POST.get('corrected', None) == None:
                    visionObj.nearVisionAcuity = 'CORRECTED'

                if not request.POST.get('isNotAble', None) == None:
                    visionObj.nearVisionAcuity = 'IS NOT ABLE'

                if not request.POST.get('colorAccept', None) == None:
                    visionObj.colourPerception = 'ACCEPT'

                if not request.POST.get('colorReject', None) == None:
                    visionObj.colourPerception = 'REJECT'

                if not request.POST.get('shadeAccept', None) == None:
                    visionObj.shadesOfGrey = 'ACCEPT'

                if not request.POST.get('colorReject', None) == None:
                    visionObj.shadesOfGrey = 'shageReject'

                visionObj.recognisedOrganisation = request.POST['recognisedOrganisation']
                visionObj.recognisedName = request.POST['recognisedName']
                visionObj.recognisedPhone = request.POST['recognisedPhone']
                visionObj.recognisedLicenceNumber = request.POST['recognisedLicenceNumber']
                visionObj.recognisedDate = datetime.datetime.strptime(request.POST['recognisedDate'], '%m/%d/%Y')

                visionObj.save()

                formListObj = FormList()
                formListObj.name = visionObj.__class__.__name__
                formListObj.event = event
                formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = visionObj.id
                formListObj.save()

                return redirect('forms:updatevision_', id=visionObj.id)


            else:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                print(canID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                self.candidateID = candidate.id
                print(self.candidateID)
                context = super(NewVisionTest, self).get_context_data()
                context['candidate'] = candidate
                context['category'] = category
                context['event'] = event
                context['guideline'] = guideline

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/vision_test.html', context)


class AllVisionTestView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_vision_test.html"

    def get_context_data(self):
        context = super(AllVisionTestView, self).get_context_data()
        forms = VisionTest.objects.all()
        context['forms'] = forms
        return context


class DeleteVisionTest(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = VisionTest
    success_url = reverse_lazy('forms:allisiontest_')


class ViewVitionTest(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/vision_test_view.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(ViewVitionTest, self).get_context_data()
        id = self.kwargs['id']
        form = VisionTest.objects.filter(id=id).first()
        context['form'] = form
        return context


class updateVisionTest(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/vision_test_update.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(updateVisionTest, self).get_context_data()
        id = self.kwargs['id']
        form = VisionTest.objects.filter(id=id).first()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("Git Test")
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =True
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =False
                visionObj = VisionTest.objects.filter(id=id).first()
                visionObj.address = request.POST['address']
                visionObj.phone = request.POST['phone']
                visionObj.email = request.POST['email']
                visionObj.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%m/%d/%Y')
                visionObj.employer = request.POST['employer']
                visionObj.tumbling = request.POST['tumbling']

                if not request.POST.get('uncorrected', None) == None:
                    visionObj.nearVisionAcuity = 'UNCORRECTED'

                if not request.POST.get('corrected', None) == None:
                    visionObj.nearVisionAcuity = 'CORRECTED'

                if not request.POST.get('isNotAble', None) == None:
                    visionObj.nearVisionAcuity = 'IS NOT ABLE'

                if not request.POST.get('colorAccept', None) == None:
                    visionObj.colourPerception = 'ACCEPT'

                if not request.POST.get('colorReject', None) == None:
                    visionObj.colourPerception = 'REJECT'

                if not request.POST.get('shadeAccept', None) == None:
                    visionObj.shadesOfGrey = 'ACCEPT'

                if not request.POST.get('colorReject', None) == None:
                    visionObj.shadesOfGrey = 'REJECT'

                visionObj.recognisedOrganisation = request.POST['recognisedOrganisation']
                visionObj.recognisedName = request.POST['recognisedName']
                visionObj.recognisedPhone = request.POST['recognisedPhone']
                visionObj.recognisedLicenceNumber = request.POST['recognisedLicenceNumber']
                visionObj.recognisedDate = datetime.datetime.strptime(request.POST['recognisedDate'], '%m/%d/%Y')

                visionObj.save()

                return redirect('forms:allisiontest_')


            if 'uploadFormBack' in request.POST:
                print('uploadFormBack')
                obj = VisionTest.objects.filter(id=id).first()
                obj.file = request.FILES['pdfFile']
                obj.save()
                return redirect('forms:allisiontest_')


            return render(request, 'forms/vision_test.html', context)


class NewTesFrmExaminationAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/general/examination_attendance.html"

    def get_context_data(self):
        context = super(NewTesFrmExaminationAttendance, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("LOOK")
                eventID = request.POST['mainEventID']
                print(eventID)
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                # candidate = TesCandidate.objects.filter(id=request.POST['CanID']).first()

                examObj = TesFrmExaminationAttendance()
                # examObj.candidate =candidate
                examObj.category = category
                examObj.guideline = guideline
                examObj.event = event

                examObj.examTitleCode = request.POST['examTitleCode']
                examObj.venue = request.POST['venue']
                examObj.date = datetime.datetime.strptime(request.POST['date'], '%m/%d/%Y')
                examObj.invigilatorName = request.POST['invigilatorName']

                examObj.save()

                #

                for idx, item in enumerate(range(0, 2)):
                    print(idx)
                    fullName = request.POST["canName" + str(idx + 1)].split(' ')
                    print(fullName)
                    if len(fullName) == 2:
                        candidate = TesCandidate.objects.filter(
                            Q(first_name=fullName[0]) & Q(last_name=fullName[1])).first()
                        print(candidate.first_name)

                    elif len(fullName) == 3:
                        candidate = TesCandidate.objects.filter(
                            Q(first_name=fullName[0]) & Q(middleName=fullName[1]) & Q(last_name=fullName[2])).first()
                        print(candidate.first_name)

                    if candidate:
                        canObj = TesFrmCandidate()
                        canObj.candidate = candidate
                        canObj.testSequence = request.POST['testSequence' + str(idx + 1)]
                        canObj.methodOfExam = request.POST['methodOfExam' + str(idx + 1)]
                        canObj.scheme = request.POST['scheme' + str(idx + 1)]
                        canObj.remark = request.POST['remark' + str(idx + 1)]
                        canObj.save()
                        examObj.tesFrmCandidate.add(canObj)

                formListObj = FormList()
                formListObj.name = examObj.__class__.__name__
                formListObj.event = event
                # formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = examObj.id
                formListObj.save()

                return redirect('forms:updatetesfrmexamattend_', id=examObj.id)


            else:
                print('Here now')
                # if request.FILES.get('file', False):
                # canID = request.POST['canID']
                eventID = request.POST['eventId']
                print(eventID)
                categoryID = request.POST['categoryId']
                guidelineID = request.POST['guidelineId']
                # print(canID)

                # candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                # self.candidateID = candidate.id
                # print(self.candidateID)
                context = super(NewTesFrmExaminationAttendance, self).get_context_data()
                # context['candidate'] = candidate
                context['category'] = category
                context['event'] = event
                context['guideline'] = guideline

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/general/examination_attendance.html', context)


class AllTesFrmExaminationAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_TES-TES-FRM-008_examination_attendance.html"

    def get_context_data(self):
        context = super(AllTesFrmExaminationAttendance, self).get_context_data()
        forms = TesFrmExaminationAttendance.objects.all()
        context['forms'] = forms
        return context


class DeleteTesFrmExaminationAttendance(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = TesFrmExaminationAttendance
    success_url = reverse_lazy('forms:alltesfrmexamattend_')


class UpdateTesFrmExaminationAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/update_TES-TES-FRM-008_examination_attendance.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(UpdateTesFrmExaminationAttendance, self).get_context_data()
        id = self.kwargs['id']
        form = TesFrmExaminationAttendance.objects.filter(id=id).first()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("LOOK")

                # candidate = TesCandidate.objects.filter(id=request.POST['CanID']).first()

                examObj = TesFrmExaminationAttendance.objects.filter(id=self.kwargs['id']).first()
                # examObj.candidate =candidate


                examObj.examTitleCode = request.POST['examTitleCode']
                examObj.venue = request.POST['venue']
                examObj.date = datetime.datetime.strptime(request.POST['date'], '%m/%d/%Y')
                examObj.invigilatorName = request.POST['invigilatorName']

                examObj.save()

                #

                for idx, item in enumerate(range(0, 8)):
                    print(str(idx+1))
                    # print(request.POST.get('id', None))
                    if not request.POST.get('id'+str(idx+1), None) == None:
                        id = request.POST['id'+str(idx+1)]
                        # print(id)

                        fullName = request.POST["canName" + str(idx+1)].split(' ')
                        print(fullName)
                        if len(fullName) == 2:
                            candidate = TesCandidate.objects.filter(
                                Q(first_name=fullName[0]) & Q(last_name=fullName[1])).first()
                            print(candidate.first_name)

                        elif len(fullName) == 3:
                            candidate = TesCandidate.objects.filter(
                                Q(first_name=fullName[0]) & Q(middleName=fullName[1]) & Q(last_name=fullName[2])).first()
                            # print(candidate.first_name)
                        #
                        if candidate:
                            canObj = TesFrmCandidate.objects.filter(id=id).first()
                            canObj.candidate = candidate
                            canObj.testSequence = request.POST['testSequence' + str(idx + 1)]
                            canObj.methodOfExam = request.POST['methodOfExam' + str(idx + 1)]
                            canObj.scheme = request.POST['scheme' + str(idx + 1)]
                            canObj.remark = request.POST['remark' + str(idx + 1)]
                            canObj.save()
                            examObj.tesFrmCandidate.add(canObj)


                return redirect('forms:alltesfrmexamattend_')

            if 'uploadFormBack' in request.POST:
                print('uploadFormBack')
                obj = TesFrmExaminationAttendance.objects.filter(id=id).first()
                obj.file = request.FILES['pdfFile']
                obj.save()
                return redirect('forms:alltesfrmexamattend_')

            return render(request, 'forms/vision_test.html', context)


class ViewTesFrmExaminationAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/view_TES-TES-FRM-008_examination_attendance.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(ViewTesFrmExaminationAttendance, self).get_context_data()
        id = self.kwargs['id']
        form = VisionTest.objects.filter(id=id).first()
        context['form'] = form
        return context


class NewLecFeedbackForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/general/lecturer_feedback.html"

    def get_context_data(self):
        context = super(NewLecFeedbackForm, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()

                lecObj = TesLecFeedbackFrom()
                lecObj.candidate = candidate
                lecObj.category = category
                lecObj.guideline = guideline
                lecObj.event = event

                lecObj.courseName = event
                lecObj.lecturerName = request.POST['lecName']
                lecObj.location = request.POST['location']
                lecObj.startDate = datetime.datetime.strptime(request.POST['startDate'], '%m/%d/%Y')

                if not request.POST.get('case11', None) == None:
                    lecObj.knowledge = '1'
                if not request.POST.get('case12', None) == None:
                    lecObj.knowledge = '2'
                if not request.POST.get('case13', None) == None:
                    lecObj.knowledge = '3'
                if not request.POST.get('case14', None) == None:
                    lecObj.knowledge = '4'
                if not request.POST.get('case15', None) == None:
                    lecObj.knowledge = '5'

                if not request.POST.get('case21', None) == None:
                    lecObj.teachingMethod = '1'
                if not request.POST.get('case22', None) == None:
                    lecObj.teachingMethod = '2'
                if not request.POST.get('case23', None) == None:
                    lecObj.teachingMethod = '3'
                if not request.POST.get('case24', None) == None:
                    lecObj.teachingMethod = '4'
                if not request.POST.get('case25', None) == None:
                    lecObj.teachingMethod = '5'

                if not request.POST.get('case31', None) == None:
                    lecObj.abilityToAnswer = '1'
                if not request.POST.get('case32', None) == None:
                    lecObj.abilityToAnswer = '2'
                if not request.POST.get('case33', None) == None:
                    lecObj.abilityToAnswer = '3'
                if not request.POST.get('case34', None) == None:
                    lecObj.abilityToAnswer = '4'
                if not request.POST.get('case35', None) == None:
                    lecObj.abilityToAnswer = '5'

                if not request.POST.get('case41', None) == None:
                    lecObj.usefulExample = '1'
                if not request.POST.get('case42', None) == None:
                    lecObj.usefulExample = '2'
                if not request.POST.get('case43', None) == None:
                    lecObj.usefulExample = '3'
                if not request.POST.get('case44', None) == None:
                    lecObj.usefulExample = '4'
                if not request.POST.get('case45', None) == None:
                    lecObj.usefulExample = '5'

                if not request.POST.get('case51', None) == None:
                    lecObj.industrialExperience = '1'
                if not request.POST.get('case52', None) == None:
                    lecObj.industrialExperience = '2'
                if not request.POST.get('case53', None) == None:
                    lecObj.industrialExperience = '3'
                if not request.POST.get('case54', None) == None:
                    lecObj.industrialExperience = '4'
                if not request.POST.get('case55', None) == None:
                    lecObj.industrialExperience = '5'

                if not request.POST.get('case61', None) == None:
                    lecObj.appropriateAids = '1'
                if not request.POST.get('case62', None) == None:
                    lecObj.appropriateAids = '2'
                if not request.POST.get('case63', None) == None:
                    lecObj.appropriateAids = '3'
                if not request.POST.get('case64', None) == None:
                    lecObj.appropriateAids = '4'
                if not request.POST.get('case65', None) == None:
                    lecObj.appropriateAids = '5'

                if not request.POST.get('case71', None) == None:
                    lecObj.transposition = '1'
                if not request.POST.get('case72', None) == None:
                    lecObj.transposition = '2'
                if not request.POST.get('case73', None) == None:
                    lecObj.transposition = '3'
                if not request.POST.get('case74', None) == None:
                    lecObj.transposition = '4'
                if not request.POST.get('case75', None) == None:
                    lecObj.transposition = '5'

                if not request.POST.get('case81', None) == None:
                    lecObj.participantsAttraction = '1'
                if not request.POST.get('case82', None) == None:
                    lecObj.participantsAttraction = '2'
                if not request.POST.get('case83', None) == None:
                    lecObj.participantsAttraction = '3'
                if not request.POST.get('case84', None) == None:
                    lecObj.participantsAttraction = '4'
                if not request.POST.get('case85', None) == None:
                    lecObj.participantsAttraction = '5'

                if not request.POST.get('case91', None) == None:
                    lecObj.ControllingTheClass = '1'
                if not request.POST.get('case92', None) == None:
                    lecObj.ControllingTheClass = '2'
                if not request.POST.get('case93', None) == None:
                    lecObj.ControllingTheClass = '3'
                if not request.POST.get('case94', None) == None:
                    lecObj.ControllingTheClass = '4'
                if not request.POST.get('case95', None) == None:
                    lecObj.ControllingTheClass = '5'

                if not request.POST.get('case101', None) == None:
                    lecObj.punctuality = '1'
                if not request.POST.get('case102', None) == None:
                    lecObj.punctuality = '2'
                if not request.POST.get('case103', None) == None:
                    lecObj.punctuality = '3'
                if not request.POST.get('case104', None) == None:
                    lecObj.punctuality = '4'
                if not request.POST.get('case105', None) == None:
                    lecObj.punctuality = '5'

                if not request.POST.get('case111', None) == None:
                    lecObj.generalBehaviour = '1'
                if not request.POST.get('case112', None) == None:
                    lecObj.generalBehaviour = '2'
                if not request.POST.get('case113', None) == None:
                    lecObj.generalBehaviour = '3'
                if not request.POST.get('case114', None) == None:
                    lecObj.generalBehaviour = '4'
                if not request.POST.get('case115', None) == None:
                    lecObj.generalBehaviour = '5'

                lecObj.knowledgeComment = request.POST['comment1']
                lecObj.teachingMethodComment = request.POST['comment2']
                lecObj.abilityToAnswerComment = request.POST['comment3']
                lecObj.usefulExampleComment = request.POST['comment4']
                lecObj.industrialExperienceComment = request.POST['comment5']
                lecObj.appropriateAidsComment = request.POST['comment6']
                lecObj.transpositionComment = request.POST['comment7']
                lecObj.participantsAttractionComment = request.POST['comment8']
                lecObj.ControllingTheClassComment = request.POST['comment9']
                lecObj.punctualityComment = request.POST['comment10']
                lecObj.generalBehaviourComment = request.POST['comment11']

                lecObj.anyComments = request.POST['comment']

                lecObj.save()

                formListObj = FormList()
                formListObj.name = lecObj.__class__.__name__
                formListObj.event = event
                formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = lecObj.id
                formListObj.save()

                return redirect('forms:allisiontest_')


            else:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                print(canID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                self.candidateID = candidate.id
                print(self.candidateID)
                context = super(NewLecFeedbackForm, self).get_context_data()
                context['candidate'] = candidate
                context['category'] = category
                context['event'] = event
                context['guideline'] = guideline

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, "forms/general/lecturer_feedback.html", context)


class AllLecFeedbackForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_tes_lec_feedback.html"

    def get_context_data(self):
        context = super(AllLecFeedbackForm, self).get_context_data()
        forms = TesLecFeedbackFrom.objects.all()
        context['forms'] = forms
        return context


class DeleteLecFeedbackForm(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = TesLecFeedbackFrom
    success_url = reverse_lazy('forms:alllecfedform_')


class UpdateLecFeedbackForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/update_lect_feedback_form.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(UpdateLecFeedbackForm, self).get_context_data()
        id = self.kwargs['id']
        form = TesFrmExaminationAttendance.objects.filter(id=id).first()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("Git Test")
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =True
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =False
                visionObj = VisionTest.objects.filter(id=id).first()
                visionObj.address = request.POST['address']
                visionObj.phone = request.POST['phone']
                visionObj.email = request.POST['email']
                visionObj.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%m/%d/%Y')
                visionObj.employer = request.POST['employer']
                visionObj.tumbling = request.POST['tumbling']

                if not request.POST.get('uncorrected', None) == None:
                    visionObj.nearVisionAcuity = 'UNCORRECTED'

                if not request.POST.get('corrected', None) == None:
                    visionObj.nearVisionAcuity = 'CORRECTED'

                if not request.POST.get('isNotAble', None) == None:
                    visionObj.nearVisionAcuity = 'IS NOT ABLE'

                if not request.POST.get('colorAccept', None) == None:
                    visionObj.colourPerception = 'ACCEPT'

                if not request.POST.get('colorReject', None) == None:
                    visionObj.colourPerception = 'REJECT'

                if not request.POST.get('shadeAccept', None) == None:
                    visionObj.shadesOfGrey = 'ACCEPT'

                if not request.POST.get('colorReject', None) == None:
                    visionObj.shadesOfGrey = 'shageReject'

                visionObj.recognisedOrganisation = request.POST['recognisedOrganisation']
                visionObj.recognisedName = request.POST['recognisedName']
                visionObj.recognisedPhone = request.POST['recognisedPhone']
                visionObj.recognisedLicenceNumber = request.POST['recognisedLicenceNumber']
                visionObj.recognisedDate = datetime.datetime.strptime(request.POST['recognisedDate'], '%m/%d/%Y')

                visionObj.save()

                return redirect('forms:allisiontest_')

            return render(request, 'forms/vision_test.html', context)


class ViewLecFeedbackForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/update_lect_feedback_form.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(ViewLecFeedbackForm, self).get_context_data()
        id = self.kwargs['id']
        form = VisionTest.objects.filter(id=id).first()
        context['form'] = form
        return context


class NewTrainingAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/general/training_attendance.html"

    def get_context_data(self):
        context = super(NewTrainingAttendance, self).get_context_data()
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()

                attObj = TrainingAttendance()
                attObj.category = category
                attObj.guideline = guideline
                attObj.event = event

                attObj.examTitleCode =  request.POST['examTitleCode']
                attObj.venue =  request.POST['venue']
                attObj.date = datetime.datetime.strptime(request.POST['date'], '%m/%d/%Y')
                attObj.lecturerName =   request.POST['lecturerName']

                #
                # if not request.POST.get('uncorrected', None) == None:
                #     visionObj.nearVisionAcuity = 'UNCORRECTED'

                attObj.save()

                for idx, item in enumerate(range(0, 8)):
                    print(idx)
                    fullName = request.POST["canName" + str(idx + 1)].split(' ')
                    print(fullName)
                    if len(fullName) == 2:
                        candidate = TesCandidate.objects.filter(
                            Q(first_name=fullName[0]) & Q(last_name=fullName[1])).first()
                        print(candidate.first_name)

                    elif len(fullName) == 3:
                        candidate = TesCandidate.objects.filter(
                            Q(first_name=fullName[0]) & Q(middleName=fullName[1]) & Q(last_name=fullName[2])).first()
                        print(candidate.first_name)

                    if len(fullName) > 1:
                        canObj = TesAttCandidate()
                        canObj.candidate = candidate
                        canObj.testSequence = request.POST['testSequence' + str(idx + 1)]
                        if not request.POST.get('dayOneSec1'+ str(idx + 1), None) == None:
                            canObj.dayOneSec1 = True
                        if not request.POST.get('dayOneSec2'+ str(idx + 1), None) == None:
                            canObj.dayOneSec2 = True
                        if not request.POST.get('dayOneSec3'+ str(idx + 1), None) == None:
                            canObj.dayOneSec3 = True
                        if not request.POST.get('dayOneSec4'+ str(idx + 1), None) == None:
                            canObj.dayOneSec4 = True

                        if not request.POST.get('dayTwoSec1'+ str(idx + 1), None) == None:
                            canObj.dayTwoSec1 = True
                        if not request.POST.get('dayTwoSec2'+ str(idx + 1), None) == None:
                            canObj.dayTwoSec2 = True
                        if not request.POST.get('dayTwoSec3'+ str(idx + 1), None) == None:
                            canObj.dayTwoSec3 = True
                        if not request.POST.get('dayTwoSec1'+ str(idx + 1), None) == None:
                            canObj.dayTwoSec1 = True

                        if not request.POST.get('dayThreeSec1'+ str(idx + 1), None) == None:
                            canObj.dayThreeSec1 = True
                        if not request.POST.get('dayThreeSec2'+ str(idx + 1), None) == None:
                            canObj.dayThreeSec2 = True
                        if not request.POST.get('dayThreeSec3'+ str(idx + 1), None) == None:
                            canObj.dayThreeSec3 = True
                        if not request.POST.get('dayThreeSec4'+ str(idx + 1), None) == None:
                            canObj.dayThreeSec4 = True
                        canObj.save()
                        attObj.attCandidate.add(canObj)


                formListObj = FormList()
                formListObj.name = attObj.__class__.__name__
                formListObj.event = event
                # formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = attObj.id
                formListObj.save()

                return redirect('forms:updatetrainingatt_' ,id=attObj.id )

            else:
                print('Here Friday')
                # if request.FILES.get('file', False):

                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']

                event = Event.objects.filter(id=eventID).first()
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()

                context = super(NewTrainingAttendance, self).get_context_data()

                context['category'] = category
                context['event'] = event
                context['guideline'] = guideline

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/general/training_attendance.html', context)


class AllTrainingAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/All-TRAINING-ATTENDANCE-FORM-TES-TES-FRM-007-01.html"

    def get_context_data(self):
        context = super(AllTrainingAttendance, self).get_context_data()
        forms = TrainingAttendance.objects.all()
        context['forms'] = forms
        return context


class DeleteTrainingAttendance(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = TrainingAttendance
    success_url = reverse_lazy('forms:alltrainingatt_')


class UpdateTrainingAttendancem(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/general/update_training_attendance.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(UpdateTrainingAttendancem, self).get_context_data()
        id = self.kwargs['id']
        form = TrainingAttendance.objects.filter(id=id).first()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:

                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =True
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =False
                attObj = TrainingAttendance.objects.filter(id=id).first()
                attObj.examTitleCode = request.POST['examTitleCode']
                attObj.venue = request.POST['venue']
                attObj.date = datetime.datetime.strptime(request.POST['date'], '%m/%d/%Y')
                attObj.lecturerName = request.POST['lecturerName']
                attObj.save()

                for idx, item in enumerate(range(0, 8)):
                    print(idx)
                    if not request.POST.get('canName' + str(idx + 1), None) == None:
                        fullName = request.POST["canName" + str(idx + 1)].split(' ')
                        print(fullName)
                        if len(fullName) == 2:
                            candidate = TesCandidate.objects.filter(
                                Q(first_name=fullName[0]) & Q(last_name=fullName[1])).first()
                            print(candidate.first_name)

                        elif len(fullName) == 3:
                            candidate = TesCandidate.objects.filter(
                                Q(first_name=fullName[0]) & Q(middleName=fullName[1]) & Q(last_name=fullName[2])).first()
                            print(candidate.first_name)

                        if len(fullName) > 1:
                            print(request.POST['indexID'+ str(idx + 1)])
                            canObj = TesAttCandidate.objects.filter(id=request.POST['indexID'+ str(idx + 1)]).first()
                            canObj.candidate = candidate
                            canObj.testSequence = request.POST['testSequence' + str(idx + 1)]
                            if not request.POST.get('dayOneSec1' + str(idx + 1), None) == None:
                                canObj.dayOneSec1 = True
                            else:
                                canObj.dayOneSec1 = False

                            if not request.POST.get('dayOneSec2' + str(idx + 1), None) == None:
                                canObj.dayOneSec2 = True
                            else:
                                canObj.dayOneSec2 = False

                            if not request.POST.get('dayOneSec3' + str(idx + 1), None) == None:
                                canObj.dayOneSec3 = True
                            else:
                                canObj.dayOneSec3 = False

                            if not request.POST.get('dayOneSec4' + str(idx + 1), None) == None:
                                canObj.dayOneSec4 = True
                            else:
                                canObj.dayOneSec4 = False



                            if not request.POST.get('dayTwoSec1' + str(idx + 1), None) == None:
                                canObj.dayTwoSec1 = True
                            else:
                                canObj.dayTwoSec1 = False

                            if not request.POST.get('dayTwoSec2' + str(idx + 1), None) == None:
                                canObj.dayTwoSec2 = True
                            else:
                                canObj.dayTwoSec2 = False

                            if not request.POST.get('dayTwoSec3' + str(idx + 1), None) == None:
                                canObj.dayTwoSec3 = True
                            else:
                                canObj.dayTwoSec3 = False

                            if not request.POST.get('dayTwoSec4' + str(idx + 1), None) == None:
                                canObj.dayTwoSec4 = True
                            else:
                                canObj.dayTwoSec4 = False



                            if not request.POST.get('dayThreeSec1' + str(idx + 1), None) == None:
                                canObj.dayThreeSec1 = True
                            else:
                                canObj.dayThreeSec1 = False

                            if not request.POST.get('daythreeSec2' + str(idx + 1), None) == None:
                                canObj.daythreeSec2 = True
                            else:
                                canObj.daythreeSec2 = False

                            if not request.POST.get('dayThreeSec3' + str(idx + 1), None) == None:
                                canObj.dayThreeSec3 = True
                            else:
                                canObj.dayThreeSec3 = False

                            if not request.POST.get('dayThreeSec4' + str(idx + 1), None) == None:
                                canObj.dayThreeSec4 = True
                            else:
                                canObj.dayThreeSec4 = False

                            canObj.save()

                return redirect('forms:alltrainingatt_')


            if 'uploadFormBack' in request.POST:
                print('uploadFormBack')
                obj = TrainingAttendance.objects.filter(id=id).first()
                obj.file = request.FILES['pdfFile']
                obj.save()
                return redirect('forms:alltrainingatt_')

            return render(request, 'forms/vision_test.html', context)


class ViewTrainingAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/view_TRAINING-ATTENDANCE-FORM-TES-TES-FRM-007-01.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(ViewTrainingAttendance, self).get_context_data()
        id = self.kwargs['id']
        form = VisionTest.objects.filter(id=id).first()
        context['form'] = form
        return context


class NewTWITrainingFeedback(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/general/training_feedback.html"

    def get_context_data(self):
        context = super(NewTWITrainingFeedback, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("Test Hello")
            if 'mainForm' in request.POST:
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()

                trainingObj = TwiTrainingFeedback()
                trainingObj.candidate = candidate
                # trainingObj.category =category
                # trainingObj.guideline =guideline
                trainingObj.event = event

                trainingObj.startDate = datetime.datetime.strptime(request.POST['startDate'], '%m/%d/%Y')
                trainingObj.lecturerName = request.POST['lecturerName']
                trainingObj.programme = request.POST['programme']
                trainingObj.venue = request.POST['venue']
                trainingObj.region = request.POST['region']
                trainingObj.howWeDid = request.POST['howWeDid']
                trainingObj.email = request.POST['email']

                if not request.POST.get('bookingProcess1', None) == None:
                    trainingObj.bookingProcess = '1'
                if not request.POST.get('bookingProcess2', None) == None:
                    trainingObj.bookingProcess = '2'
                if not request.POST.get('bookingProcess3', None) == None:
                    trainingObj.bookingProcess = '3'
                if not request.POST.get('bookingProcess4', None) == None:
                    trainingObj.bookingProcess = '4'
                if not request.POST.get('bookingProcess5', None) == None:
                    trainingObj.bookingProcess = '5'
                if not request.POST.get('bookingProcess6', None) == None:
                    trainingObj.bookingProcess = '6'
                if not request.POST.get('bookingProcess7', None) == None:
                    trainingObj.bookingProcess = '7'
                if not request.POST.get('bookingProcess8', None) == None:
                    trainingObj.bookingProcess = '8'
                if not request.POST.get('bookingProcess9', None) == None:
                    trainingObj.bookingProcess = '9'
                if not request.POST.get('bookingProcess10', None) == None:
                    trainingObj.bookingProcess = '10'

                if not request.POST.get('joiningInstructions1', None) == None:
                    trainingObj.joiningInstructions = '1'
                if not request.POST.get('joiningInstructions2', None) == None:
                    trainingObj.joiningInstructions = '2'
                if not request.POST.get('joiningInstructions1', None) == None:
                    trainingObj.joiningInstructions = '3'
                if not request.POST.get('joiningInstructions4', None) == None:
                    trainingObj.joiningInstructions = '4'
                if not request.POST.get('joiningInstructions5', None) == None:
                    trainingObj.joiningInstructions = '5'
                if not request.POST.get('joiningInstructions6', None) == None:
                    trainingObj.joiningInstructions = '6'
                if not request.POST.get('joiningInstructions7', None) == None:
                    trainingObj.joiningInstructions = '7'
                if not request.POST.get('joiningInstructions8', None) == None:
                    trainingObj.joiningInstructions = '8'
                if not request.POST.get('joiningInstructions9', None) == None:
                    trainingObj.joiningInstructions = '9'
                if not request.POST.get('joiningInstructions10', None) == None:
                    trainingObj.joiningInstructions = '10'

                if not request.POST.get('trainingEnvironment1', None) == None:
                    trainingObj.trainingEnvironment = '1'
                if not request.POST.get('trainingEnvironment2', None) == None:
                    trainingObj.trainingEnvironment = '2'
                if not request.POST.get('trainingEnvironment3', None) == None:
                    trainingObj.trainingEnvironment = '3'
                if not request.POST.get('trainingEnvironment4', None) == None:
                    trainingObj.trainingEnvironment = '4'
                if not request.POST.get('trainingEnvironment5', None) == None:
                    trainingObj.trainingEnvironment = '5'
                if not request.POST.get('trainingEnvironment6', None) == None:
                    trainingObj.trainingEnvironment = '6'
                if not request.POST.get('trainingEnvironment7', None) == None:
                    trainingObj.trainingEnvironment = '7'
                if not request.POST.get('trainingEnvironment8', None) == None:
                    trainingObj.trainingEnvironment = '8'
                if not request.POST.get('trainingEnvironment9', None) == None:
                    trainingObj.trainingEnvironment = '9'
                if not request.POST.get('trainingEnvironment10', None) == None:
                    trainingObj.trainingEnvironment = '10'

                if not request.POST.get('objectivesCourse1', None) == None:
                    trainingObj.objectivesCourse = '1'
                if not request.POST.get('objectivesCourse2', None) == None:
                    trainingObj.objectivesCourse = '2'
                if not request.POST.get('objectivesCourse3', None) == None:
                    trainingObj.objectivesCourse = '3'
                if not request.POST.get('objectivesCourse4', None) == None:
                    trainingObj.objectivesCourse = '4'
                if not request.POST.get('objectivesCourse5', None) == None:
                    trainingObj.objectivesCourse = '5'
                if not request.POST.get('objectivesCourse6', None) == None:
                    trainingObj.objectivesCourse = '6'
                if not request.POST.get('objectivesCourse7', None) == None:
                    trainingObj.objectivesCourse = '7'
                if not request.POST.get('objectivesCourse8', None) == None:
                    trainingObj.objectivesCourse = '8'
                if not request.POST.get('objectivesCourse9', None) == None:
                    trainingObj.objectivesCourse = '9'
                if not request.POST.get('objectivesCourse10', None) == None:
                    trainingObj.objectivesCourse = '10'

                if not request.POST.get('tutorLecturer1', None) == None:
                    trainingObj.tutorLecturer = '1'
                if not request.POST.get('tutorLecturer2', None) == None:
                    trainingObj.tutorLecturer = '2'
                if not request.POST.get('tutorLecturer3', None) == None:
                    trainingObj.tutorLecturer = '3'
                if not request.POST.get('tutorLecturer4', None) == None:
                    trainingObj.tutorLecturer = '4'
                if not request.POST.get('tutorLecturer5', None) == None:
                    trainingObj.tutorLecturer = '5'
                if not request.POST.get('tutorLecturer6', None) == None:
                    trainingObj.tutorLecturer = '6'
                if not request.POST.get('tutorLecturer7', None) == None:
                    trainingObj.tutorLecturer = '7'
                if not request.POST.get('tutorLecturer8', None) == None:
                    trainingObj.tutorLecturer = '8'
                if not request.POST.get('tutorLecturer9', None) == None:
                    trainingObj.tutorLecturer = '9'
                if not request.POST.get('tutorLecturer10', None) == None:
                    trainingObj.tutorLecturer = '10'

                if not request.POST.get('principlesExplained1', None) == None:
                    trainingObj.principlesExplained = '1'
                if not request.POST.get('principlesExplained2', None) == None:
                    trainingObj.principlesExplained = '2'
                if not request.POST.get('principlesExplained3', None) == None:
                    trainingObj.principlesExplained = '3'
                if not request.POST.get('principlesExplained4', None) == None:
                    trainingObj.principlesExplained = '4'
                if not request.POST.get('principlesExplained5', None) == None:
                    trainingObj.principlesExplained = '5'
                if not request.POST.get('principlesExplained6', None) == None:
                    trainingObj.principlesExplained = '6'
                if not request.POST.get('principlesExplained7', None) == None:
                    trainingObj.principlesExplained = '7'
                if not request.POST.get('principlesExplained8', None) == None:
                    trainingObj.principlesExplained = '8'
                if not request.POST.get('principlesExplained9', None) == None:
                    trainingObj.principlesExplained = '9'
                if not request.POST.get('principlesExplained10', None) == None:
                    trainingObj.principlesExplained = '10'

                if not request.POST.get('questionsAnswered1', None) == None:
                    trainingObj.questionsAnswered = '1'
                if not request.POST.get('questionsAnswered2', None) == None:
                    trainingObj.questionsAnswered = '2'
                if not request.POST.get('questionsAnswered3', None) == None:
                    trainingObj.questionsAnswered = '3'
                if not request.POST.get('questionsAnswered4', None) == None:
                    trainingObj.questionsAnswered = '4'
                if not request.POST.get('questionsAnswered5', None) == None:
                    trainingObj.questionsAnswered = '5'
                if not request.POST.get('questionsAnswered6', None) == None:
                    trainingObj.questionsAnswered = '6'
                if not request.POST.get('questionsAnswered7', None) == None:
                    trainingObj.questionsAnswered = '7'
                if not request.POST.get('questionsAnswered8', None) == None:
                    trainingObj.questionsAnswered = '8'
                if not request.POST.get('questionsAnswered9', None) == None:
                    trainingObj.questionsAnswered = '9'
                if not request.POST.get('questionsAnswered10', None) == None:
                    trainingObj.questionsAnswered = '10'

                if not request.POST.get('audience1', None) == None:
                    trainingObj.audience = '1'
                if not request.POST.get('audience2', None) == None:
                    trainingObj.audience = '2'
                if not request.POST.get('audience3', None) == None:
                    trainingObj.audience = '3'
                if not request.POST.get('audience4', None) == None:
                    trainingObj.audience = '4'
                if not request.POST.get('audience5', None) == None:
                    trainingObj.audience = '5'
                if not request.POST.get('audience6', None) == None:
                    trainingObj.audience = '6'
                if not request.POST.get('audience7', None) == None:
                    trainingObj.audience = '7'
                if not request.POST.get('audience8', None) == None:
                    trainingObj.audience = '8'
                if not request.POST.get('audience9', None) == None:
                    trainingObj.audience = '9'
                if not request.POST.get('audience10', None) == None:
                    trainingObj.audience = '10'

                if not request.POST.get('atmosphere1', None) == None:
                    trainingObj.atmosphere = '1'
                if not request.POST.get('atmosphere2', None) == None:
                    trainingObj.atmosphere = '2'
                if not request.POST.get('atmosphere3', None) == None:
                    trainingObj.atmosphere = '3'
                if not request.POST.get('atmosphere4', None) == None:
                    trainingObj.atmosphere = '4'
                if not request.POST.get('atmosphere5', None) == None:
                    trainingObj.atmosphere = '5'
                if not request.POST.get('atmosphere6', None) == None:
                    trainingObj.atmosphere = '6'
                if not request.POST.get('atmosphere7', None) == None:
                    trainingObj.atmosphere = '7'
                if not request.POST.get('atmosphere8', None) == None:
                    trainingObj.atmosphere = '8'
                if not request.POST.get('atmosphere9', None) == None:
                    trainingObj.atmosphere = '9'
                if not request.POST.get('atmosphere10', None) == None:
                    trainingObj.atmosphere = '10'

                if not request.POST.get('practicalSessions1', None) == None:
                    trainingObj.practicalSessions = '1'
                if not request.POST.get('practicalSessions2', None) == None:
                    trainingObj.practicalSessions = '2'
                if not request.POST.get('practicalSessions3', None) == None:
                    trainingObj.practicalSessions = '3'
                if not request.POST.get('practicalSessions4', None) == None:
                    trainingObj.practicalSessions = '4'
                if not request.POST.get('practicalSessions5', None) == None:
                    trainingObj.practicalSessions = '5'
                if not request.POST.get('practicalSessions6', None) == None:
                    trainingObj.practicalSessions = '6'
                if not request.POST.get('practicalSessions7', None) == None:
                    trainingObj.practicalSessions = '7'
                if not request.POST.get('practicalSessions8', None) == None:
                    trainingObj.practicalSessions = '8'
                if not request.POST.get('practicalSessions9', None) == None:
                    trainingObj.practicalSessions = '9'
                if not request.POST.get('practicalSessions10', None) == None:
                    trainingObj.practicalSessions = '10'

                if not request.POST.get('notes1', None) == None:
                    trainingObj.notes = '1'
                if not request.POST.get('notes2', None) == None:
                    trainingObj.notes = '2'
                if not request.POST.get('notes3', None) == None:
                    trainingObj.notes = '3'
                if not request.POST.get('notes4', None) == None:
                    trainingObj.notes = '4'
                if not request.POST.get('notes5', None) == None:
                    trainingObj.notes = '5'
                if not request.POST.get('notes6', None) == None:
                    trainingObj.notes = '6'
                if not request.POST.get('notes7', None) == None:
                    trainingObj.notes = '7'
                if not request.POST.get('notes8', None) == None:
                    trainingObj.notes = '8'
                if not request.POST.get('notes9', None) == None:
                    trainingObj.notes = '9'
                if not request.POST.get('notes10', None) == None:
                    trainingObj.notes = '10'

                if not request.POST.get('equipment1', None) == None:
                    trainingObj.equipment = '1'
                if not request.POST.get('equipment2', None) == None:
                    trainingObj.equipment = '2'
                if not request.POST.get('equipment3', None) == None:
                    trainingObj.equipment = '3'
                if not request.POST.get('equipment4', None) == None:
                    trainingObj.equipment = '4'
                if not request.POST.get('equipment5', None) == None:
                    trainingObj.equipment = '5'
                if not request.POST.get('equipment6', None) == None:
                    trainingObj.equipment = '6'
                if not request.POST.get('equipment7', None) == None:
                    trainingObj.equipment = '7'
                if not request.POST.get('equipment8', None) == None:
                    trainingObj.equipment = '8'
                if not request.POST.get('equipment9', None) == None:
                    trainingObj.equipment = '9'
                if not request.POST.get('equipment10', None) == None:
                    trainingObj.equipment = '10'

                if not request.POST.get('overallQuality1', None) == None:
                    trainingObj.overallQuality = '1'
                if not request.POST.get('overallQuality2', None) == None:
                    trainingObj.overallQuality = '2'
                if not request.POST.get('overallQuality3', None) == None:
                    trainingObj.overallQuality = '3'
                if not request.POST.get('overallQuality4', None) == None:
                    trainingObj.overallQuality = '4'
                if not request.POST.get('overallQuality5', None) == None:
                    trainingObj.overallQuality = '5'
                if not request.POST.get('overallQuality6', None) == None:
                    trainingObj.overallQuality = '6'
                if not request.POST.get('overallQuality7', None) == None:
                    trainingObj.overallQuality = '7'
                if not request.POST.get('overallQuality8', None) == None:
                    trainingObj.overallQuality = '8'
                if not request.POST.get('overallQuality9', None) == None:
                    trainingObj.overallQuality = '9'
                if not request.POST.get('overallQuality10', None) == None:
                    trainingObj.overallQuality = '10'

                if not request.POST.get('expectations1', None) == None:
                    trainingObj.expectations = '1'
                if not request.POST.get('expectations2', None) == None:
                    trainingObj.expectations = '2'
                if not request.POST.get('expectations3', None) == None:
                    trainingObj.expectations = '3'
                if not request.POST.get('expectations4', None) == None:
                    trainingObj.expectations = '4'
                if not request.POST.get('expectations5', None) == None:
                    trainingObj.expectations = '5'
                if not request.POST.get('expectations6', None) == None:
                    trainingObj.expectations = '6'
                if not request.POST.get('expectations7', None) == None:
                    trainingObj.expectations = '7'
                if not request.POST.get('expectations8', None) == None:
                    trainingObj.expectations = '8'
                if not request.POST.get('expectations9', None) == None:
                    trainingObj.expectations = '9'
                if not request.POST.get('expectations10', None) == None:
                    trainingObj.expectations = '10'

                if not request.POST.get('penetrantTesting', None) == None:
                    trainingObj.penetrantTesting = True
                else:
                    trainingObj.penetrantTesting = False

                if not request.POST.get('magneticTesting', None) == None:
                    trainingObj.magneticTesting = True
                else:
                    trainingObj.magneticTesting = False

                if not request.POST.get('radioTesting', None) == None:
                    trainingObj.radioTesting = True
                else:
                    trainingObj.radioTesting = False

                if not request.POST.get('radioIntro', None) == None:
                    trainingObj.radioIntro = True
                else:
                    trainingObj.radioIntro = False

                if not request.POST.get('ultrasonicTesting', None) == None:
                    trainingObj.ultrasonicTesting = True
                else:
                    trainingObj.ultrasonicTesting = False

                if not request.POST.get('eddyCurrentTesting', None) == None:
                    trainingObj.eddyCurrentTesting = True
                else:
                    trainingObj.eddyCurrentTesting = False

                if not request.POST.get('timeFlightDiffraction', None) == None:
                    trainingObj.timeFlightDiffraction = True
                else:
                    trainingObj.timeFlightDiffraction = False

                if not request.POST.get('phasedArrayUltrasonic', None) == None:
                    trainingObj.phasedArrayUltrasonic = True
                else:
                    trainingObj.phasedArrayUltrasonic = False

                if not request.POST.get('ACFM', None) == None:
                    trainingObj.ACFM = True
                else:
                    trainingObj.ACFM = False

                if not request.POST.get('digitalComputedRadiography', None) == None:
                    trainingObj.digitalComputedRadiography = True
                else:
                    trainingObj.digitalComputedRadiography = False

                if not request.POST.get('automatedUltrasonicTesting', None) == None:
                    trainingObj.automatedUltrasonicTesting = True
                else:
                    trainingObj.automatedUltrasonicTesting = False

                if not request.POST.get('pulsedEddyCurrent', None) == None:
                    trainingObj.pulsedEddyCurrent = True
                else:
                    trainingObj.pulsedEddyCurrent = False

                if not request.POST.get('appreciationBasicNDTMethod', None) == None:
                    trainingObj.appreciationBasicNDTMethod = True
                else:
                    trainingObj.appreciationBasicNDTMethod = False

                if not request.POST.get('appreciationAdvancedNDTmethods', None) == None:
                    trainingObj.appreciationAdvancedNDTmethods = True
                else:
                    trainingObj.appreciationAdvancedNDTmethods = False

                if not request.POST.get('cathodicProtection', None) == None:
                    trainingObj.cathodicProtection = True
                else:
                    trainingObj.cathodicProtection = False

                if not request.POST.get('introNDT', None) == None:
                    trainingObj.introNDT = True
                else:
                    trainingObj.introNDT = False

                if not request.POST.get('visualWeldingInspection', None) == None:
                    trainingObj.visualWeldingInspection = True
                else:
                    trainingObj.visualWeldingInspection = False

                if not request.POST.get('weldingInspection', None) == None:
                    trainingObj.weldingInspection = True
                else:
                    trainingObj.weldingInspection = False

                if not request.POST.get('seniorWeldingInspection', None) == None:
                    trainingObj.seniorWeldingInspection = True
                else:
                    trainingObj.seniorWeldingInspection = False

                if not request.POST.get('weldingQuality', None) == None:
                    trainingObj.weldingQuality = True
                else:
                    trainingObj.weldingQuality = False

                if not request.POST.get('partialWelder', None) == None:
                    trainingObj.partialWelder = True
                else:
                    trainingObj.partialWelder = False

                if not request.POST.get('introASME', None) == None:
                    trainingObj.introASME = True
                else:
                    trainingObj.introASME = False

                if not request.POST.get('introErupeanStandard', None) == None:
                    trainingObj.introErupeanStandard = True
                else:
                    trainingObj.introErupeanStandard = False

                if not request.POST.get('reviewAsmeXI', None) == None:
                    trainingObj.reviewAsmeXI = True
                else:
                    trainingObj.reviewAsmeXI = False

                if not request.POST.get('siteCoating', None) == None:
                    trainingObj.siteCoating = True
                else:
                    trainingObj.siteCoating = False

                if not request.POST.get('paitingInspector', None) == None:
                    trainingObj.paitingInspector = True
                else:
                    trainingObj.paitingInspector = False

                if not request.POST.get('weldingInspector', None) == None:
                    trainingObj.weldingInspector = True
                else:
                    trainingObj.weldingInspector = False

                if not request.POST.get('IIWDiploma', None) == None:
                    trainingObj.IIWDiploma = True
                else:
                    trainingObj.IIWDiploma = False

                if not request.POST.get('plantInspector', None) == None:
                    trainingObj.plantInspector = True
                else:
                    trainingObj.plantInspector = False

                if not request.POST.get('underWater', None) == None:
                    trainingObj.underWater = True
                else:
                    trainingObj.underWater = False

                trainingObj.save()

                formListObj = FormList()
                formListObj.name = trainingObj.__class__.__name__
                formListObj.event = event
                formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = trainingObj.id
                formListObj.save()

                return redirect('forms:alltwitrainingfeed_')
            else:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                print(canID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                self.candidateID = candidate.id
                print(self.candidateID)
                context = super(NewTWITrainingFeedback, self).get_context_data()
                context['candidate'] = candidate
                context['category'] = category
                context['event'] = event
                context['guideline'] = guideline

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/general/training_feedback.html', context)


class AllTWITrainingFeedback(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_twi_training_feedback.html"

    def get_context_data(self):
        context = super(AllTWITrainingFeedback, self).get_context_data()
        forms = TwiTrainingFeedback.objects.all().order_by('-id')
        context['forms'] = forms
        return context


class DeleteTWITrainingFeedback(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = TwiTrainingFeedback
    success_url = reverse_lazy('forms:alltwitrainingfeed_')


class UpdateTWITrainingFeedback(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/update_twi_Training_Feedback.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(UpdateTWITrainingFeedback, self).get_context_data()
        id = self.kwargs['id']
        form = TesFrmExaminationAttendance.objects.filter(id=id).first()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("Git Test")
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =True
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =False
                visionObj = VisionTest.objects.filter(id=id).first()
                visionObj.address = request.POST['address']
                visionObj.phone = request.POST['phone']
                visionObj.email = request.POST['email']
                visionObj.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%m/%d/%Y')
                visionObj.employer = request.POST['employer']
                visionObj.tumbling = request.POST['tumbling']

                if not request.POST.get('uncorrected', None) == None:
                    visionObj.nearVisionAcuity = 'UNCORRECTED'

                if not request.POST.get('corrected', None) == None:
                    visionObj.nearVisionAcuity = 'CORRECTED'

                if not request.POST.get('isNotAble', None) == None:
                    visionObj.nearVisionAcuity = 'IS NOT ABLE'

                if not request.POST.get('colorAccept', None) == None:
                    visionObj.colourPerception = 'ACCEPT'

                if not request.POST.get('colorReject', None) == None:
                    visionObj.colourPerception = 'REJECT'

                if not request.POST.get('shadeAccept', None) == None:
                    visionObj.shadesOfGrey = 'ACCEPT'

                if not request.POST.get('colorReject', None) == None:
                    visionObj.shadesOfGrey = 'shageReject'

                visionObj.recognisedOrganisation = request.POST['recognisedOrganisation']
                visionObj.recognisedName = request.POST['recognisedName']
                visionObj.recognisedPhone = request.POST['recognisedPhone']
                visionObj.recognisedLicenceNumber = request.POST['recognisedLicenceNumber']
                visionObj.recognisedDate = datetime.datetime.strptime(request.POST['recognisedDate'], '%m/%d/%Y')

                visionObj.save()

                return redirect('forms:allisiontest_')

            return render(request, 'forms/vision_test.html', context)


class ViewTWITrainingFeedback(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/new_twi_Training_Feedback.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(ViewTWITrainingFeedback, self).get_context_data()
        id = self.kwargs['id']
        form = VisionTest.objects.filter(id=id).first()
        context['form'] = form
        return context


class NewTWIExamFeedback(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/twi_exam_Feedback_S.html"

    def get_context_data(self):
        context = super(NewTWIExamFeedback, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        categories = Category.objects.all()
        guidelines = Guideline.objects.all()

        context['categories'] = categories
        context['guidelines'] = guidelines
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                eventID = request.POST['eventID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                event = Event.objects.filter(id=eventID).first()
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()

                examObj = TwiExamFeedback()
                examObj.candidate =candidate
                examObj.event = event
                examObj.startDate = datetime.datetime.strptime(request.POST['startDate'], '%m/%d/%Y')
                examObj.invigilator = request.POST['lecturerName']
                examObj.programme = request.POST['programme']
                examObj.venue = request.POST['venue']
                examObj.region = request.POST['region']
                examObj.howWeDid = request.POST['howWeDid']
                examObj.candidateOpinion = request.POST['candidateOpinion']


                for idx,item in enumerate(range(0,10)):
                    print(idx+1)
                    if not request.POST.get('administrativeStaff'+str(idx+1), None) == None:
                        examObj.administrativeStaff = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('examinationRoom'+str(idx+1), None) == None:
                        examObj.examinationRoom = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('feltComfortable'+str(idx+1), None) == None:
                        examObj.feltComfortable = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('explanationInvigilator'+str(idx+1), None) == None:
                        examObj.explanationInvigilator = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('writtenExamination'+str(idx+1), None) == None:
                        examObj.writtenExamination = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('courseContent'+str(idx+1), None) == None:
                        examObj.courseContent = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('equipment'+str(idx+1), None) == None:
                        examObj.equipment = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('samples'+str(idx+1), None) == None:
                        examObj.samples = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('reflection'+str(idx+1), None) == None:
                        examObj.reflection = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('practicalSamples'+str(idx+1), None) == None:
                        examObj.practicalSamples = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('recommend'+str(idx+1), None) == None:
                        examObj.recommend = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('comparisonTo'+str(idx+1), None) == None:
                        examObj.comparisonTo = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('afterYourExperience'+str(idx+1), None) == None:
                        examObj.afterYourExperience = str(idx+1)

                for idx,item in enumerate(range(0,10)):
                    if not request.POST.get('catering'+str(idx+1), None) == None:
                        examObj.catering = str(idx+1)



                examObj.save()

                formListObj = FormList()
                formListObj.name = examObj.__class__.__name__
                formListObj.event = event
                formListObj.candidate = candidate
                formListObj.category = category
                formListObj.guideline = guideline
                formListObj.FormID = examObj.id
                formListObj.save()

                return redirect('forms:alltwiexamfeed_')
            else:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canCanID']
                eventID = request.POST['eventEvID']
                categoryID = request.POST['categoryID']
                guidelineID = request.POST['guidelineID']
                print(canID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                category = Category.objects.filter(id=categoryID).first()
                guideline = Guideline.objects.filter(id=guidelineID).first()
                self.candidateID = candidate.id
                print(self.candidateID)
                context = super(NewTWIExamFeedback, self).get_context_data()
                context['candidate'] = candidate
                context['category'] = category
                context['event'] = event
                context['guideline'] = guideline

            # return redirect('forms:jaegertofdl2_' ,context)
            return render(request, 'forms/twi_exam_Feedback_S.html', context)

class AllTWIExamFeedback(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/all_twi_exam_feedback.html"

    def get_context_data(self):
        context = super(AllTWIExamFeedback, self).get_context_data()
        forms = TwiExamFeedback.objects.all()
        context['forms'] = forms
        return context


class DeleteTWIExamFeedback(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = TwiExamFeedback
    success_url = reverse_lazy('forms:alltwiexamfeed_')


class UpdateTWIExamFeedback(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/update_twi_exam_Feedback.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(UpdateTWIExamFeedback, self).get_context_data()
        id = self.kwargs['id']
        form = TesFrmExaminationAttendance.objects.filter(id=id).first()
        context['form'] = form
        return context

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("Git Test")
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =True
                # if not  request.POST.get('contactMe', None) == None:
                #     objPSL57.contactMe =False
                visionObj = VisionTest.objects.filter(id=id).first()
                visionObj.address = request.POST['address']
                visionObj.phone = request.POST['phone']
                visionObj.email = request.POST['email']
                visionObj.birthDay = datetime.datetime.strptime(request.POST['birthDay'], '%m/%d/%Y')
                visionObj.employer = request.POST['employer']
                visionObj.tumbling = request.POST['tumbling']

                if not request.POST.get('uncorrected', None) == None:
                    visionObj.nearVisionAcuity = 'UNCORRECTED'

                if not request.POST.get('corrected', None) == None:
                    visionObj.nearVisionAcuity = 'CORRECTED'

                if not request.POST.get('isNotAble', None) == None:
                    visionObj.nearVisionAcuity = 'IS NOT ABLE'

                if not request.POST.get('colorAccept', None) == None:
                    visionObj.colourPerception = 'ACCEPT'

                if not request.POST.get('colorReject', None) == None:
                    visionObj.colourPerception = 'REJECT'

                if not request.POST.get('shadeAccept', None) == None:
                    visionObj.shadesOfGrey = 'ACCEPT'

                if not request.POST.get('colorReject', None) == None:
                    visionObj.shadesOfGrey = 'shageReject'

                visionObj.recognisedOrganisation = request.POST['recognisedOrganisation']
                visionObj.recognisedName = request.POST['recognisedName']
                visionObj.recognisedPhone = request.POST['recognisedPhone']
                visionObj.recognisedLicenceNumber = request.POST['recognisedLicenceNumber']
                visionObj.recognisedDate = datetime.datetime.strptime(request.POST['recognisedDate'], '%m/%d/%Y')

                visionObj.save()

                return redirect('forms:allisiontest_')

            return render(request, 'forms/vision_test.html', context)


class ViewTWIExamFeedback(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "forms/view_twi_exam_Feedback.html"

    def get_context_data(self, id, *args, **kwargs):
        context = super(ViewTWIExamFeedback, self).get_context_data()
        id = self.kwargs['id']
        form = VisionTest.objects.filter(id=id).first()
        context['form'] = form
        return context