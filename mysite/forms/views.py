from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from forms.models import Forms
import json
from classes.db import FormDb
# Create your views here.



class NewForm(TemplateView):
    template_name = "forms/new_form.html"

    def get_context_data(self):
        context = super(NewForm, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context
    
    
    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':

            formName =request.POST['formName']
            jsonCode =request.POST['jsonCode']
            
            data = json.loads(jsonCode)
            
            for item in data:
                if item['type'] == 'text' or item['type'] == 'number':
                    
                    name = item['name']
                    label = item['label']
                    required = item['required']
                    required = item['required']
                    
                    formObj = FormDb()
                    formObj.TableGenerator('test')
        return redirect('forms:all_')  
    
    

class AllForms(TemplateView):
    template_name = "forms/all_forms.html"

    def get_context_data(self):
        context = super(AllForms, self).get_context_data()
        forms = Forms.objects.all()
        context['forms'] = forms
        return context
    
    



class AllFormsFromPostgres(TemplateView):
    template_name = "forms/all_forms_postres.html"

    def get_context_data(self):
        context = super(AllFormsFromPostgres, self).get_context_data()
        formObj = FormDb()
        tList = formObj.TableLists()
        context['tList'] = tList
        return context
    