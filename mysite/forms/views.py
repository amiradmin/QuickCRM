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
                obj = TwiEnrolmentForm()
                obj.twiCandidateID = request.POST['form1_1']
                obj.eventName = request.POST['form2_1']
                # obj.eventDate = datetime.datetime.strptime(request.POST['form3_1'], '%m/%d/%Y')
                obj.firstName = request.POST['form4_1']
                obj.middleName = request.POST['form5_1']
                obj.lastName = request.POST['form6_1']
                obj.save()
                formObj = FormsList.objects.filter(id=1).first()
                
                mainCanID = request.POST['mainCanID']
                print(mainCanID)
                candidateObj = TesCandidate.objects.filter(id = 1050896).first()
                print(candidateObj.first_name)
                candidateObj.forms.add(formObj)
                
                
                
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
    
    
class EachFormMemebr(TemplateView):
    template_name = "forms/categoried_form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EachFormMemebr, self).get_context_data()
        formID = self.kwargs['id']
        print(formID)
        form = FormsList.objects.filter(id= formID).first()
        canList = TesCandidate.objects.filter(forms=form)
        context['canList'] = canList
        context['form'] = form
        return context 
