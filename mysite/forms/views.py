from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from forms.models import Forms,TwiEnrolmentForm
from django.db.models import Count
from classes.db import FormDb
from training.models import FormsList, TesCandidate,Event,Category
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
                candidate = TesCandidate.objects.filter(id=request.POST['mainCanID']).first()
                obj = TwiEnrolmentForm()
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
                    
                    
                obj.save()
                formObj = FormsList.objects.filter(id=1).first()
                
                # mainCanID = request.POST['mainCanID']
                # print(mainCanID)
                # candidateObj = TesCandidate.objects.filter(id = 1050896).first()
                # print(candidateObj.first_name)
                candidate.forms.add(formObj)
                
                
                
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
        formID = self.kwargs['id']
        print(formID)
        form = TwiEnrolmentForm.objects.all()
        # canList = TesCandidate.objects.filter(forms=form)
        # context['canList'] = canList
        context['form'] = form
        return context 
    
class EventSummary(TemplateView):
    template_name = "forms/event_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EventSummary, self).get_context_data()
        # formID = self.kwargs['id']
        # print(formID)
        # form = TwiEnrolmentForm.objects.all()
 
        # context['form'] = form
        return context 
