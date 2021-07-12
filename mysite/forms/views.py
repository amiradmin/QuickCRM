from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from forms.models import Forms,Field
import json
from classes.db import FormDb
from training.models import TesCandidate,Event
# Create your views here.

class FormJaegerTOFDL2(TemplateView):
    template_name = "forms/reg_forms/Jaeger_TOFDL2.html"

    def get_context_data(self):
        context = super(FormJaegerTOFDL2, self).get_context_data()
        candidates = TesCandidate.objects.all()
        events = Event.objects.all()
        context['candidates'] = candidates
        context['events'] = events
        return context
    

    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            print('Here')
            # if request.FILES.get('file', False):
            canID = request.POST['canID']
            eventID = request.POST['eventID']
            print(canID)
            candidate= TesCandidate.objects.filter(id = canID).first()
            event= Event.objects.filter(id = eventID).first()
            print(candidate.last_name)
            context = super(FormJaegerTOFDL2, self).get_context_data()
            context['candidate'] = candidate
            context['event'] = event
        # return redirect('forms:jaegertofdl2_' ,context)  
            return render(request, 'forms/reg_forms/Jaeger_TOFDL2.html', context)
        
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
    