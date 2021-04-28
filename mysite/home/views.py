from django.shortcuts import render,redirect
from django.views.generic import TemplateView
# Create your views here.



class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context



    # def post(self, request, *args, **kwargs):
    #
    #     form = MedicineForm(self.request.POST)
    #     if form.is_valid():
    #         obj = Tamin()
    #         response=obj.drug_list()


        # return render(request, 'medicine/medicine_panel.html', {'data': response.json()})
        # return redirect('home:main_')
