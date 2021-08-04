from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from forms.models import Forms,TwiEnrolmentForm,General,BGAsExperienceForm
from django.db.models import Count
from classes.db import FormDb
from training.models import FormsList, TesCandidate,Event,Category
from django.core.mail import EmailMessage
from django.db.models import Q
import datetime
# Create your views here.

class TwiEnrolment(TemplateView):
    template_name = "forms/reg_forms/twi_enrolment.html"
    candidateID = None

    def get_context_data(self):
        context = super(TwiEnrolment, self).get_context_data()
        candidates = TesCandidate.objects.all()
        events = Event.objects.all()
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
                obj.plantInspectionRequirements = request.POST['form47_3']
                obj.VerifierName = request.POST['form1_4']
                obj.VerifierCompanyPosition = request.POST['form2_4']
                obj.VerifierProfessionalRelation = request.POST['form3_4']
                obj.VerifierTelephone = request.POST['form4_4']
                obj.VerifierEmail = request.POST['form4_4']
                obj.VerifierDate = request.POST['form5_4']
                obj.VerifierDate = datetime.datetime.strptime(request.POST['form5_4'], '%m/%d/%Y')

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
                if not request.POST.get('form33_2 - Working in quality control function related to welding activities with five years of verified working experience (this could relate to a CSWIP WI (3.1) holder', None) == None:
                    obj.experience ='ASME IX'


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
                # print("Here")
                # eventID = request.POST['eventID']
                candidate = TesCandidate.objects.filter(id=	id).first()
                obj = TwiEnrolmentForm()
                # obj.eventID = eventID
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
                # formObj = FormsList.objects.filter(id=1).first()
                #
                # # mainCanID = request.POST['mainCanID']
                # # print(mainCanID)
                # # candidateObj = TesCandidate.objects.filter(id = 1050896).first()
                # # print(candidateObj.first_name)
                # candidate.forms.add(formObj)
                #
                # generalObj = General.objects.filter(event_id=eventID).first()
                # generalObj.twiEnrolmentForm.add(obj)
                # generalObj.save()
                # email = EmailMessage('Subject', 'Body', to=['your@email.com'],['bcc@example.com'])
                print("Start Mailing")
                email = EmailMessage(
                    'Tescan Registration Dept.',
                    'Dear {}! Registration is done successfully. '.format(obj.firstName),
                    'registration@tescan.ca',
                    [obj.email],
                    ['nima.vakilotojjar@tescan.ca'],

                )
                email.send()
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
        candidates = TesCandidate.objects.all()
        events = Event.objects.all()
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'mainForm' in request.POST:
                print("Form")
                return redirect('forms:allenrolmentform_')


            else:
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
