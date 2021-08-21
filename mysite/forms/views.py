from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from forms.models import Forms,TwiEnrolmentForm,General,BGAsExperienceForm,PSL30LogExp,NdtTechnique,FormList,PSL30InitialForm
from django.db.models import Count
from classes.db import FormDb
from training.models import FormsList, TesCandidate,Event,Category
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from django.db.models import Q
import datetime
from  authorization.sidebarmixin import SidebarMixin
# Create your views here.

class TwiEnrolment(TemplateView):
    template_name = "forms/reg_forms/twi_enrolment.html"
    candidateID = None

    def get_context_data(self):
        context = super(TwiEnrolment, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name', 'last_name')
        events = Event.objects.all()
        adminStatus = False
        for g in self.request.user.groups.all():
            if  g.name == 'super_admin' or g.name=='training_admin':
                adminStatus=True
        context['adminStatus'] = adminStatus
        context['candidates'] = candidates
        context['events'] = events
        self.candidateID = 50
        return context
    

    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            if 'enrolment' in request.POST:
                eventID = request.POST['eventID']
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()
                obj = TwiEnrolmentForm()
                obj.eventID = eventID
                obj.candidate = candidate
                obj.twiCandidateID = request.POST['form1_1']
                obj.eventName = request.POST['form2_1']
                # obj.eventDate = datetime.datetime.strptime(request.POST['form3_1'], '%m/%d/%Y')
                obj.firstName = request.POST['form4_1']
                obj.middleName = request.POST['form5_1']
                obj.lastName = request.POST['form6_1']
                day = request.POST['form7_1'] 
                month = request.POST['form8_1'] 
                year = request.POST['form9_1'] 
                birdDay = month + '/' + day + '/' + year
                obj.birthOfDate = datetime.datetime.strptime(birdDay, '%m/%d/%Y')
                obj.permanentPrivateAddress = request.POST['form15_1']
                obj.Postcode = request.POST['form18_1']
                obj.CarRegNo = request.POST['form19_1']
                obj.privateTel = request.POST['form20_1']
                obj.emergencyTel = request.POST['form21_1']
                obj.email = request.POST['form22_1']
                obj.correspondenceAddress = request.POST['form28_1']
                obj.invoiceAddress = request.POST['form38_1']
                obj.sponsoringCompanyAndaddress = request.POST['form40_1']
                obj.sponsorPostcode = request.POST['form43_1']
                obj.sponsorContactName = request.POST['form44_1']
                obj.sponsorTel = request.POST['form45_1']
                obj.sponsorFax = request.POST['form46_1']
                obj.sponsorEmail = request.POST['form47_1']
                obj.PCN_BGASApprovalNumber = request.POST['form11_2']
                obj.currentCSWIPQualifications = request.POST['form12_2']
                obj.plantInspectionRequirements = request.POST['form47_3']
                obj.VerifierName = request.POST['form1_4']
                obj.VerifierCompanyPosition = request.POST['form2_4']
                obj.VerifierProfessionalRelation = request.POST['form3_4']
                obj.VerifierTelephone = request.POST['form4_4']
                obj.VerifierEmail = request.POST['form5_4']
                obj.experienceRequirements = request.POST['form34_2']
                obj.otherExaminationsTitle = request.POST['form51_3']
                # obj.VerifierDate = request.POST['form6_4']
                obj.VerifierDate = datetime.datetime.strptime(request.POST['form6_4'], '%m/%d/%Y')

                # obj.GDPRstatement = request.POST['form37_1']
                
      
                
               
                if not request.POST.get('form54_1', None) == None:                             
                    obj.venue ='Calgary'
                    
                if not request.POST.get('form56_1', None) == None:                             
                    obj.venue ='Edmonton'
                                        
                if not request.POST.get('form12_1', None) == None:                             
                    obj.venue ='Brazil'
                                                            
                if not request.POST.get('form55_1', None) == None:                             
                    obj.venue ='Toronto'
                                                                                
                if not request.POST.get('form57_1', None) == None:                             
                   obj.venue ='Fort Erie'        
                                                                                            
                if not request.POST.get('form13_1', None) == None:                             
                    obj.venue ='USA'
                                                                                                                
                if not request.POST.get('form10_1', None) == None:                             
                    obj.venue ='Quebec' 
                                                                                                                                   
                if not request.POST.get('form11_1', None) == None:                             
                    obj.venue ='Vancouver'     
                                                                                                                                                  
                if not request.POST.get('form14_1', None) == None:                             
                    obj.venue ='New Brunswick'
                    
                if not request.POST.get('diabilityYes', None) == None:
                    obj.disability =True
                if request.POST.get('diabilityNo', None) == None:
                    obj.disability =False
                                    
                if not  request.POST.get('form58_1', None) == None:
                    obj.weldingSociety =True
                if not request.POST.get('form59_1', None) == None:
                    obj.twiEmployee =True

                if not request.POST.get('compSponser', None) == None:
                    obj.sponsorStatus =True
                if not request.POST.get('selfSponser', None) == None:
                    obj.sponsorStatus =True          
                          
                if not request.POST.get('form37_1', None) == None:
                    obj.GDPRstatement =True
                    
                tempTearAbout=''
                if not request.POST.get('form29_1', None) == None:
                    tempTearAbout = 'TWI Corporate Website '
                if not request.POST.get('form30_1', None) == None:
                    tempTearAbout =tempTearAbout +' - '+ 'CSWIP Website'
                if not request.POST.get('form31_1', None) == None:
                    tempTearAbout =tempTearAbout +' - '+  'Email marketing '
                if not request.POST.get('form32_1', None) == None:
                    tempTearAbout =tempTearAbout +' - '+  'Bulletin / Connect '
                if not request.POST.get('form33_1', None) == None:
                    tempTearAbout =tempTearAbout +' - '+  'Google search'
                if not request.POST.get('form34_1', None) == None:
                    tempTearAbout =tempTearAbout +' - '+  'Other (please specify)'
                if not request.POST.get('form23_1', None) == None:
                    tempTearAbout =tempTearAbout +' - '+ 'LinkedIn'
                if not request.POST.get('form24_1', None) == None:
                    tempTearAbout =tempTearAbout +' - '+  'Facebook'
                if not request.POST.get('form25_1', None) == None:
                    tempTearAbout =tempTearAbout +' - '+  'NDT News / Insight'          
                if not request.POST.get('form26_1', None) == None: 
                    tempTearAbout =tempTearAbout +' - '+  'Exhibitions / Events'       
                if not request.POST.get('form27_1', None) == None: 
                    tempTearAbout =tempTearAbout +' - '+  'Word of Mouth'                     
                obj.hearAbout =tempTearAbout
                
                if not request.POST.get('form1_2', None) == None:                             
                    obj.examinationType ='Initial'                
                if not request.POST.get('form2_2', None) == None:                             
                    obj.examinationType ='supplementary'
                if not request.POST.get('form3_2', None) == None:                             
                    obj.examinationType ='renewal'
                if not request.POST.get('form4_2', None) == None:                             
                    obj.examinationType ='bridging'
                if not request.POST.get('form5_2', None) == None:                             
                    obj.examinationType ='retest of a previously failed examination'

                if not request.POST.get('form6_2', None) == None:                             
                    obj.examinationBody ='CSWIP'                
                if not request.POST.get('form7_2', None) == None:                             
                    obj.examinationBody ='PCN'
                if not request.POST.get('form8_2', None) == None:                             
                    obj.examinationBody ='AWS'
                if not request.POST.get('form9_2', None) == None:                             
                    obj.examinationBody ='BGAS'
                if not request.POST.get('form10_2', None) == None:                             
                    obj.examinationBody ='ASNT'


                if not request.POST.get('form13_2', None) == None:
                    obj.CSWIPWeldingexamination ='VWI (3.0)'
                if not request.POST.get('form14_2', None) == None:
                    obj.CSWIPWeldingexamination ='WI (3.1)'
                if not request.POST.get('form15_2', None) == None:
                    obj.CSWIPWeldingexamination ='SWI (3.2.1)'
                if not request.POST.get('form16_2', None) == None:
                    obj.CSWIPWeldingexamination ='SWI (3.2.2) '
                if not request.POST.get('form17_2', None) == None:
                    obj.CSWIPWeldingexamination ='AWSCSWIP'

                if not request.POST.get('form18_2', None) == None:
                    obj.CSWIPWeldingexamination ='Endorsement'
                if not request.POST.get('form19_2', None) == None:
                    obj.CSWIPWeldingexamination ='Instructor'
                if not request.POST.get('form20_2', None) == None:
                    obj.CSWIPWeldingexamination ='Supervisor'
                if not request.POST.get('form21_2', None) == None:
                    obj.CSWIPWeldingexamination ='QC Coordinator '
                if not request.POST.get('form22_2', None) == None:
                    obj.CSWIPWeldingexamination ='ASME IX'

                if not request.POST.get('form23_2', None) == None:
                    obj.experience ='WI(3.1) - Welding Inspector for a minimum of 3 years with experience related to the duties and responsibilities listed in Clause 1.2.2 under qualified supervision, independently verified.'
                if not request.POST.get('form24_2', None) == None:
                    obj.experience ='WI (3.1) - Certified Visual Welding Inspector for a minimum of 2 years with job responsibilities in the areas listed in 1.2.1 and 1.2.2.'
                if not request.POST.get('form25_2', None) == None:
                    obj.experience ='WI (3.1) - Welding Instructor or Welding Foreman/Supervisor for a minimum of 1 year.'
                if not request.POST.get('form26_2', None) == None:
                    obj.experience ='SWI (3.2.1 & 3.2.2) - Certified Welding Inspector for a minimum of 2 years with job responsibilities in the areas listed in 1.2.1, 1.2.2 and 1.2.3. '
                if not request.POST.get('form27_2', None) == None:
                    obj.experience ='SWI (3.2.1 & 3.2.2) - 5 years\' authenticated experience related to the duties and responsibilities listed in Clause 1.2.3, independently verified.'

                if not request.POST.get('form28_2', None) == None:
                    obj.experience ='Welding QC coordinator - A current valid CSWIP 3.2 Senior Welding Inspector certification plus three years documented experience related to the duties and responsibilities or an international equivalent.'
                if not request.POST.get('form29_2', None) == None:
                    obj.experience ='Welding QC coordinator - A current valid CSWIP 3.1 Welding Inspector with 10 year’s documented experience related to the duties and responsibilities or an international equivalent. '
                if not request.POST.get('form30_2', None) == None:
                    obj.experience ='ASME IX - Hold current valid Senior Welding Inspector or international equivalent.'
                if not request.POST.get('form31_2', None) == None:
                    obj.experience ='ASME IX - Certified Welding Inspector with five years relevant verified work experience or international equivalent '
                if not request.POST.get('form32_2', None) == None:
                    obj.experience ='ASME IX - A HNC in Welding Fabrication'
                if not request.POST.get('form33_2', None) == None:
                    obj.experience ='ASME IX - Working in quality control function related to welding activities with five years of verified working experience (this could relate to a CSWIP WI (3.1) holder'


                if not request.POST.get('form35_2', None) == None:
                    obj.underwaterInspectionExam ='3.1U'
                if not request.POST.get('form36_2', None) == None:
                    obj.underwaterInspectionExam ='3.2U'
                if not request.POST.get('form37_2', None) == None:
                    obj.underwaterInspectionExam ='3.3U'
                if not request.POST.get('form38_2', None) == None:
                    obj.underwaterInspectionExam ='3.4U'
                if not request.POST.get('form39_2', None) == None:
                    obj.underwaterInspectionExam ='A-SCAN '
                if not request.POST.get('form40_2', None) == None:
                    obj.underwaterInspectionExam ='Concrete'


                if not request.POST.get('form1_3', None) == None:
                    obj.NDTexamination ='PT'
                if not request.POST.get('form2_3', None) == None:
                    obj.NDTexamination ='MT'
                if not request.POST.get('form3_3', None) == None:
                    obj.NDTexamination ='VT'
                if not request.POST.get('form4_3', None) == None:
                    obj.NDTexamination ='ET'
                if not request.POST.get('form5_3', None) == None:
                    obj.NDTexamination ='ACFM'

                if not request.POST.get('form6_3', None) == None:
                    obj.NDTexamination ='RT'
                if not request.POST.get('form7_3', None) == None:
                    obj.NDTexamination ='Rad Interpret'
                if not request.POST.get('form8_3', None) == None:
                    obj.NDTexamination ='CR/DR'
                if not request.POST.get('form9_3', None) == None:
                    obj.NDTexamination ='CRI/DRI'
                if not request.POST.get('form10_3', None) == None:
                    obj.NDTexamination ='BRS'
                if not request.POST.get('form11_3', None) == None:
                    obj.NDTexamination ='RPS'

                if not request.POST.get('form12_3', None) == None:
                    obj.NDTexamination ='UT'
                if not request.POST.get('form13_3', None) == None:
                    obj.NDTexamination ='PAUT'
                if not request.POST.get('form14_3', None) == None:
                    obj.NDTexamination ='TOFD'
                if not request.POST.get('form15_3', None) == None:
                    obj.NDTexamination ='AUT'
                if not request.POST.get('form16_3', None) == None:
                    obj.NDTexamination ='UTCM'
                if not request.POST.get('form17_3', None) == None:
                    obj.NDTexamination ='PACM'

                if not request.POST.get('form18_3', None) == None:
                    obj.NDTexamination ='Appreciation'
                if not request.POST.get('form19_3', None) == None:
                    obj.NDTexamination ='Basic'
                if not request.POST.get('form20_3', None) == None:
                    obj.NDTexamination ='Phasor DM'

                if not request.POST.get('form21_3', None) == None:
                    obj.NDTexaminationLevel ='Level 1'
                if not request.POST.get('form22_3', None) == None:
                    obj.NDTexaminationLevel ='Level 2'
                if not request.POST.get('form23_3', None) == None:
                    obj.NDTexaminationLevel ='Level 3'

                if not request.POST.get('form24_3', None) == None:
                    obj.NDTIndustrySector ='General'
                if not request.POST.get('form25_3', None) == None:
                    obj.NDTIndustrySector ='Welds'
                if not request.POST.get('form26_3', None) == None:
                    obj.NDTIndustrySector ='Castings'
                if not request.POST.get('form27_3', None) == None:
                    obj.NDTIndustrySector ='Wrought'
                if not request.POST.get('form28_3', None) == None:
                    obj.NDTIndustrySector ='Forgings'
                if not request.POST.get('form29_3', None) == None:
                    obj.NDTIndustrySector ='Tubes & Pipes'
                if not request.POST.get('form30_3', None) == None:
                    obj.NDTIndustrySector ='Aero'


                if not request.POST.get('form31_3', None) == None:
                    obj.NDTexaminationCategories ='3.1'
                if not request.POST.get('form32_3', None) == None:
                    obj.NDTexaminationCategories ='3.2'
                if not request.POST.get('form33_3', None) == None:
                    obj.NDTexaminationCategories ='3.7'
                if not request.POST.get('form34_3', None) == None:
                    obj.NDTexaminationCategories ='3.8'
                if not request.POST.get('form35_3', None) == None:
                    obj.NDTexaminationCategories ='3.9'
                if not request.POST.get('form36_3', None) == None:
                    obj.NDTexaminationCategories ='Critical sizing'


                if not request.POST.get('form37_3', None) == None:
                    obj.plantInspectionLevel ='Level 1'
                if not request.POST.get('form38_3', None) == None:
                    obj.plantInspectionLevel ='Level 2'
                if not request.POST.get('form39_3', None) == None:
                    obj.plantInspectionLevel ='Level 3'
                if not request.POST.get('form40_3', None) == None:
                    obj.plantInspectionLevel ='Endorsement'

                if not request.POST.get('form41_3', None) == None:
                    obj.plantInspectionLevel1 ='I hold current approved NDT Level 2 (ACCP, CSWIP, PCN or ASNT) in two methods, one of which must be Ultrasonic'
                if not request.POST.get('form42_3', None) == None:
                    obj.plantInspectionLevel1 ='I hold CSWIP Welding Inspector or higher'
                if not request.POST.get('form43_3', None) == None:
                    obj.plantInspectionLevel1 ='I hold HNC in Mechanical Engineering or equivalent'
                if not request.POST.get('form44_3', None) == None:
                    obj.plantInspectionLevel1 ='I have a minimum of Five years, assessed and authenticated industry experience in this field (Mature Entry Route), a verified CV can be supplied – Must be Authenticated by Line Manager'

                if not request.POST.get('form45_3', None) == None:
                    obj.plantInspectionLevel2 ='I hold a valid Level 1 Plant Inspector approval'
                if not request.POST.get('form46_3', None) == None:
                    obj.plantInspectionLevel2 ='I have successfully completed the Level 1 exams as a pre entry requirement'


                if not request.POST.get('form48_3', None) == None:
                   obj.otherExaminationsTitleRequired ='Plastic welding'
                if not request.POST.get('form49_3', None) == None:
                    obj.otherExaminationsTitleRequired ='Offshore visual Inspector'
                if not request.POST.get('form50_3', None) == None:
                    obj.otherExaminationsTitleRequired ='BGAS'



                obj.save()
                formObj = FormsList.objects.filter(id=1).first()
                
                # mainCanID = request.POST['mainCanID']
                # print(mainCanID)
                # candidateObj = TesCandidate.objects.filter(id = 1050896).first()
                # print(candidateObj.first_name)
                candidate.forms.add(formObj)
                
                generalObj = General.objects.filter(event_id=eventID).first()
                generalObj.twiEnrolmentForm.add( obj)
                generalObj.save()
                
                return redirect('forms:allenrolmentform_')  

                 
            else :
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                print(canID)
                
                candidate= TesCandidate.objects.filter(id = canID).first()
                event= Event.objects.filter(id = eventID).first()
                self.candidateID = candidate.id
                print(self.candidateID)
                context = super(TwiEnrolment, self).get_context_data()
                context['candidate'] = candidate
                context['event'] = event
                
        # return redirect('forms:jaegertofdl2_' ,context)  
            return render(request, 'forms/reg_forms/twi_enrolment.html', context)


class TwiEnrolmentReg(TemplateView):
    template_name = "forms/reg_forms/twi_enrolment_reg.html"
    candidateID = None

    def get_context_data(self,id, *args, **kwargs):
        context = super(TwiEnrolmentReg, self).get_context_data()
        self.candidateID = self.kwargs['id']
        print("Get : "+ str(id))
        return context

    def post(self, request,id, *args, **kwargs):

        if request.method == 'POST':
            if 'enrolment' in request.POST:
                print("Post: "+ str(id))
                print("Amir")
                # eventID = request.POST['eventID']
                candidate = TesCandidate.objects.filter(id=	id).first()
                obj = TwiEnrolmentForm()
                # obj.eventID = eventID
                obj.candidate = candidate
                # obj.twiCandidateID = request.POST['form1_1']
                obj.eventName = request.POST['form2_1']
                # obj.eventDate = datetime.datetime.strptime(request.POST['form3_1'], '%m/%d/%Y')
                obj.firstName = request.POST['form4_1']
                obj.middleName = request.POST['form5_1']
                obj.lastName = request.POST['form6_1']
                day = request.POST['form7_1']
                month = request.POST['form8_1']
                year = request.POST['form9_1']
                birdDay = day + '/' + month + '/' + year
                obj.birthOfDate = datetime.datetime.strptime(birdDay, '%m/%d/%Y')
                obj.permanentPrivateAddress = request.POST['form15_1']
                obj.Postcode = request.POST['form18_1']
                obj.CarRegNo = request.POST['form19_1']
                obj.privateTel = request.POST['form20_1']
                obj.emergencyTel = request.POST['form21_1']
                obj.email = request.POST['form22_1']
                obj.correspondenceAddress = request.POST['form28_1']
                obj.invoiceAddress = request.POST['form38_1']
                obj.sponsoringCompanyAndaddress = request.POST['form40_1']
                obj.sponsorPostcode = request.POST['form43_1']
                obj.sponsorContactName = request.POST['form44_1']
                obj.sponsorTel = request.POST['form45_1']
                obj.sponsorFax = request.POST['form46_1']
                obj.sponsorEmail = request.POST['form47_1']
                obj.PCN_BGASApprovalNumber = request.POST['form11_2']
                obj.currentCSWIPQualifications = request.POST['form12_2']
                # obj.GDPRstatement = request.POST['form37_1']

                if not request.POST.get('form54_1', None) == None:
                    obj.venue = 'Calgary'

                if not request.POST.get('form56_1', None) == None:
                    obj.venue = 'Edmonton'

                if not request.POST.get('form12_1', None) == None:
                    obj.venue = 'Brazil'

                if not request.POST.get('form55_1', None) == None:
                    obj.venue = 'Toronto'

                if not request.POST.get('form57_1', None) == None:
                    obj.venue = 'Fort Erie'

                if not request.POST.get('form13_1', None) == None:
                    obj.venue = 'USA'

                if not request.POST.get('form10_1', None) == None:
                    obj.venue = 'Quebec'

                if not request.POST.get('form11_1', None) == None:
                    obj.venue = 'Vancouver'

                if not request.POST.get('form14_1', None) == None:
                    obj.venue = 'New Brunswick'

                if not request.POST.get('diabilityYes', None) == None:
                    obj.disability = True
                if request.POST.get('diabilityNo', None) == None:
                    obj.disability = False

                if not request.POST.get('form58_1', None) == None:
                    obj.weldingSociety = True
                if not request.POST.get('form59_1', None) == None:
                    obj.twiEmployee = True

                if not request.POST.get('compSponser', None) == None:
                    obj.sponsorStatus = True
                if not request.POST.get('selfSponser', None) == None:
                    obj.sponsorStatus = True

                if not request.POST.get('form37_1', None) == None:
                    obj.GDPRstatement = True

                tempTearAbout = ''
                if not request.POST.get('form29_1', None) == None:
                    tempTearAbout = 'TWI Corporate Website '
                if not request.POST.get('form30_1', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'CSWIP Website'
                if not request.POST.get('form31_1', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Email marketing '
                if not request.POST.get('form32_1', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Bulletin / Connect '
                if not request.POST.get('form33_1', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Google search'
                if not request.POST.get('form34_1', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Other (please specify)'
                if not request.POST.get('form23_1', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'LinkedIn'
                if not request.POST.get('form24_1', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Facebook'
                if not request.POST.get('form25_1', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'NDT News / Insight'
                if not request.POST.get('form26_1', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Exhibitions / Events'
                if not request.POST.get('form27_1', None) == None:
                    tempTearAbout = tempTearAbout + ' - ' + 'Word of Mouth'
                obj.hearAbout = tempTearAbout

                if not request.POST.get('form1_2', None) == None:
                    obj.examinationType = 'Initial'
                if not request.POST.get('form2_2', None) == None:
                    obj.examinationType = 'supplementary'
                if not request.POST.get('form3_2', None) == None:
                    obj.examinationType = 'renewal'
                if not request.POST.get('form4_2', None) == None:
                    obj.examinationType = 'bridging'
                if not request.POST.get('form5_2', None) == None:
                    obj.examinationType = 'retest of a previously failed examination'

                if not request.POST.get('form6_2', None) == None:
                    obj.examinationBody = 'CSWIP'
                if not request.POST.get('form7_2', None) == None:
                    obj.examinationBody = 'PCN'
                if not request.POST.get('form8_2', None) == None:
                    obj.examinationBody = 'AWS'
                if not request.POST.get('form9_2', None) == None:
                    obj.examinationBody = 'BGAS'
                if not request.POST.get('form10_2', None) == None:
                    obj.examinationBody = 'ASNT'

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
        <td style="padding:30px 30px 0px 30px; line-height:36px; text-align:inherit; background-color:#4d5171;" height="100%" valign="top" bgcolor="#4d5171" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="color: #ffffff; font-size: 18px; font-family: inherit">Dear """ + candidate.first_name+ """ """ + candidate.last_name + """</span></div><div></div></div></td>
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

class AllEnrolmentForm(TemplateView):
    template_name = "forms/all_forms_enrolment.html"

    def get_context_data(self):
        context = super(AllEnrolmentForm, self).get_context_data()
        forms = TwiEnrolmentForm.objects.all()
        adminStatus = False
        for g in self.request.user.groups.all():
            if  g.name == 'super_admin' or g.name=='training_admin':
                adminStatus=True
        context['adminStatus'] = adminStatus
        context['forms'] = forms
        return context   
    
class AllBGASForm(TemplateView):
    template_name = "forms/all_bgas_form.html"

    def get_context_data(self):
        context = super(AllBGASForm, self).get_context_data()
        forms = BGAsExperienceForm.objects.all()
        adminStatus = False
        for g in self.request.user.groups.all():
            if  g.name == 'super_admin' or g.name=='training_admin':
                adminStatus=True
        context['adminStatus'] = adminStatus
        context['forms'] = forms
        return context

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

class BGASExperienceForm(TemplateView):
    template_name = "forms/reg_forms/BGAS_experience_form.html"

    def get_context_data(self):
        context = super(BGASExperienceForm, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name')
        events = Event.objects.all()
        adminStatus =False
        for g in self.request.user.groups.all():
            if  g.name == 'super_admin' or g.name=='training_admin':
                adminStatus=True
        context['adminStatus'] = adminStatus
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                canID = request.POST['canID']
                # eventID = request.POST['eventID']
                print("Form")
                print(canID)
                candidate = TesCandidate.objects.filter(id=canID).first()
                # event = Event.objects.filter(id=eventID).first()
                bgasObj = BGAsExperienceForm()
                bgasObj.candidate =candidate
                # bgasObj.evenID =event.id
                bgasObj.firstName =candidate.first_name
                bgasObj.lastName =candidate.last_name
                bgasObj.middleName =candidate.middleName
                # bgasObj.twiCandidateID = request.POST['canID']
                bgasObj.VerifierName = request.POST['verifierName']
                bgasObj.VerifierCompany = request.POST['verifierCompany']
                bgasObj.VerifierPosition = request.POST['verifierPosition']
                bgasObj.VerifierTelephone = request.POST['verifierTel']
                bgasObj.VerifierEmail = request.POST['verifiermail']
                bgasObj.VerifierDate = datetime.datetime.strptime(request.POST['verifierDate'], '%m/%d/%Y')
                bgasObj.PreCertificationExperience = request.POST['PreCertificationExperience']

                bgasObj.save()

                formObj = FormList()
                formObj.name = "BGAS_Experience_Form"
                formObj.candidate = candidate

                formObj.save()

                return redirect('forms:allbgasform_')


            elif 'selector' in request.POST:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                print(canID)
                print(eventID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                print(candidate.first_name)
                event = Event.objects.filter(id=eventID).first()
                self.candidateID = candidate.id
                twiEnrolmentForm = TwiEnrolmentForm.objects.filter(candidate=candidate).first()
                context = super(BGASExperienceForm, self).get_context_data()
                context['candidate'] = candidate
                context['event'] = event
                context['twiEnrolmentForm'] = twiEnrolmentForm

            # return redirect('forms:jaegertofdl2_' ,context)
                return render(request, 'forms/reg_forms/BGAS_experience_form.html', context)



class BGASinitialForm(SidebarMixin,TemplateView):
    template_name = "forms/reg_forms/PSL-57A_Initial_exam_application.html"

    def get_context_data(self):
        context = super(BGASinitialForm, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name')
        events = Event.objects.all()


        context['candidates'] = candidates
        context['events'] = events
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

                mainObj =PSL30InitialForm()
                mainObj.candidate =candidate
                mainObj.event =event
                mainObj.cerAddres =request.POST['cerAddres']

                mainObj.save()


                formObj = FormList()
                formObj.name = "PSL-57A Initial exam application"
                formObj.candidate = candidate
                formObj.event = event
                if not request.POST.get('comfirmation', None) == None:
                    formObj.status = True

                formObj.save()

                return redirect('forms:allpslinitialform_')


            elif 'selector' in request.POST:
                print('Here')
                # if request.FILES.get('file', False):
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                print(canID)
                print(eventID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                print(candidate.first_name)
                event = Event.objects.filter(id=eventID).first()
                self.candidateID = candidate.id
                twiEnrolmentForm = TwiEnrolmentForm.objects.filter(candidate=candidate).first()
                context = super(BGASinitialForm, self).get_context_data()
                context['candidate'] = candidate
                context['event'] = event
                context['twiEnrolmentForm'] = twiEnrolmentForm

            # return redirect('forms:jaegertofdl2_' ,context)
                return render(request, 'forms/reg_forms/PSL-57A_Initial_exam_application.html', context)


class AllBGASinitialForms(SidebarMixin,TemplateView):
    template_name = "forms/all_psl30_inintal_forms.html"

    def get_context_data(self):
        context = super(AllBGASinitialForms, self).get_context_data()
        forms = PSL30InitialForm.objects.all()

        context['forms'] = forms
        return context

class PSL30LogExperienceForm(TemplateView):
    template_name = "forms/reg_forms/PSL_30_log_exper.html"

    def get_context_data(self):
        context = super(PSL30LogExperienceForm, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name')
        events = Event.objects.all()
        adminStatus = False
        for g in self.request.user.groups.all():
            if  g.name == 'super_admin' or g.name=='training_admin':
                adminStatus=True
        context['adminStatus'] = adminStatus
        context['candidates'] = candidates
        context['events'] = events

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                canID = request.POST['canID']
                eventID = request.POST['eventID']
                # eventID = request.POST['eventID']
                print("Form")
                candidate = TesCandidate.objects.filter(id=canID).first()
                event = Event.objects.filter(id=eventID).first()
                pslObj = PSL30LogExp()
                pslObj.candidate =candidate
                pslObj.event =event
                pslObj.fullName =request.POST['canName']
                pslObj.dateFrom = datetime.datetime.strptime(request.POST['dateFrom'], '%m/%d/%Y')
                pslObj.dateTo = datetime.datetime.strptime(request.POST['dateTo'], '%m/%d/%Y')
                pslObj.ndtMethod =request.POST['NDTmethod']
                pslObj.totalHours =request.POST['totalHours']
                pslObj.employingOrganisation =request.POST['employingOrganisation']
                pslObj.reviewerName =request.POST['reviewerName']
                pslObj.reviewerDate =datetime.datetime.strptime(request.POST['reviewerDate'], '%m/%d/%Y')
                pslObj.finalEmployerDeclarationName =request.POST['finalEmployerDeclarationName']
                pslObj.dateCandidateDeclaration =datetime.datetime.strptime(request.POST['dateCandidateDeclaration'], '%m/%d/%Y')
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

            else :
                print('Here')
                context = super(PSL30LogExperienceForm, self).get_context_data()
                canID = request.POST['canID']
                eventID = request.POST['eventID']

                print(canID)
                print(eventID)

                candidate = TesCandidate.objects.filter(id=canID).first()
                print(candidate.first_name)
                event = Event.objects.filter(id=eventID).first()
                self.candidateID = candidate.id
                twiEnrolmentForm = TwiEnrolmentForm.objects.filter(candidate=candidate).first()

                context['candidate'] = candidate
                context['event'] = event
                context['twiEnrolmentForm'] = twiEnrolmentForm

                # return redirect('forms:jaegertofdl2_' ,context)
                return render(request, 'forms/reg_forms/PSL_30_log_exper.html', context)


class AllPSL30LogForm(TemplateView):
    template_name = "forms/all_psl30log_forms.html"

    def get_context_data(self):
        context = super(AllPSL30LogForm, self).get_context_data()
        pslForms = PSL30LogExp.objects.all()
        adminStatus =False
        for g in self.request.user.groups.all():
            if  g.name == 'super_admin' or g.name=='training_admin':
                adminStatus=True
        context['adminStatus'] = adminStatus
        context['pslForms'] = pslForms

        return context

class AllFormsList(TemplateView):
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
        context = super(ViewFormByID, self).get_context_data()
        canID = self.kwargs['id']
        candidate = TesCandidate.objects.filter(id =canID).first()
        print(canID)
        print(candidate.id)
        form = TwiEnrolmentForm.objects.filter(candidate=candidate).first()
        context['form'] = form
        return context    

class ViewFormByFormID(TemplateView):
    template_name = "forms/reg_forms/twi_enrolment_by_id.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ViewFormByFormID, self).get_context_data()
        canID = self.kwargs['id']
        print(canID)

        form = TwiEnrolmentForm.objects.filter(id=canID).first()
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
    

class sigDrawer(TemplateView):
    template_name = "forms/draw_sig.html"
    candidateID = None

    def get_context_data(self, *args, **kwargs):
        context = super(sigDrawer, self).get_context_data()
 

        return context


class uploadSignature(TemplateView):
    template_name = "forms/uploud_sig.html"
    candidateID = None

    def get_context_data(self, *args, **kwargs):
        context = super(uploadSignature, self).get_context_data()
 

        return context
    
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
    
    
class UploadForm(TemplateView):
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
               formObj = TwiEnrolmentForm.objects.filter(id = formID).first()
               formObj.uploadedForm = request.FILES['myFile']
               formObj.save()
            
        return redirect('forms:allenrolmentform_')  
    
    
class EachFormMemebr(TemplateView):
    template_name = "forms/categoried_form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EachFormMemebr, self).get_context_data()
        eventID = self.kwargs['id']
        event = Event.objects.filter(id=eventID).first()
        general= General.objects.filter(event = event).first()
        form = TwiEnrolmentForm.objects.all()
        # canList = TesCandidate.objects.filter(forms=form)
        # context['canList'] = canList
        context['form'] = form
        context['general'] = general
        return context 
    
class EventSummary(TemplateView):
    template_name = "forms/event_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventSummary, self).get_context_data()
        eventID = self.kwargs['id']
        twiForm = TwiEnrolmentForm.objects.filter(eventID=eventID)
        event = Event.objects.filter(id=eventID).first()
        generalObj = General.objects.filter(event=event).first()
        eventConfirm = TwiEnrolmentForm.objects.filter(Q(eventID=eventID) & Q(confirmation=True))
        tag = Category.objects.filter(id=event.formCategory.id).first()  

        candidateList = event.candidate.all()
        submitedList = generalObj.twiEnrolmentForm.all()
        list1=[]
        list2=[]
        for item in candidateList:
            print(item.tes_candidate_id)
            list1.append(item.tes_candidate_id)
        
        print("====")
        for item in submitedList:
            print(item.candidate.tes_candidate_id)
            list2.append(item.candidate.tes_candidate_id)

        resultList = list(set(list1).difference(list2))
        unsubmited = TesCandidate.objects.filter(tes_candidate_id__in=resultList)

        print(resultList)
        context['tag'] = tag        
        context['form'] = generalObj.twiEnrolmentForm.all()
        context['event'] = event
        context['eventConfirm'] = eventConfirm
        context['generalObj'] = generalObj
        context['unsubmited'] = unsubmited
        return context 

class EventSummaryByFormId(TemplateView):
    template_name = "forms/event_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventSummaryByFormId, self).get_context_data()
        formID = self.kwargs['formID']
        generalID = self.kwargs['genID']
        submitedList=None
        generalObj = General.objects.filter(id=generalID).first()
        print(generalID)
        if formID==1 :
            form = generalObj.twiEnrolmentForm.all()
            
            eventConfirm = TwiEnrolmentForm.objects.filter(Q(eventID=generalObj.event.id) & Q(confirmation=True))
        elif formID==2:
            form = generalObj.bgasExperienceForm.all()
            eventConfirm = BGAsExperienceForm.objects.filter(Q(eventID=generalObj.event.id) & Q(confirmation=True))
        event = Event.objects.filter(id=generalObj.event.id).first()
        
        
        tag = Category.objects.filter(id=event.formCategory.id).first()  
        candidateList = event.candidate.all()
        
        list1=[]
        list2=[]
        for item in candidateList:
            print(item.tes_candidate_id)
            list1.append(item.tes_candidate_id)
        
        print("====")
        for item in form:
            print(item.candidate.tes_candidate_id)
            list2.append(item.candidate.tes_candidate_id)

        resultList = list(set(list1).difference(list2))
        unsubmited = TesCandidate.objects.filter(tes_candidate_id__in=resultList)

        print(generalObj.id)
        context['tag'] = tag        
        context['event'] = event
        context['eventConfirm'] = eventConfirm
        context['generalObj'] = generalObj
        context['form'] = form
        context['unsubmited'] = unsubmited

        return context 
