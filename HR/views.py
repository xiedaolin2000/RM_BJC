import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import personForm
from .models import Person


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    html = "<html><body>HR应用主页<p>现在时间是%s.</body></html>" % now
    return HttpResponse(html)

def infoHR(request):
    return render(request,"HR/HR_list.html")

class PersonListView(generic.ListView):
    model = Person
    context_object_name = 'person_list'
    template_name='HR/HR_list.html'
    #设置了分页的记录数就自动开启了分页功能
    paginate_by=10 
    
    # def get_queryset(self):

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        context["Author"]="xiedaolin.DELEX"
        return context


# class personUpdateView(generic.UpdateView):
#     model = Person
#     # fields = ["userName","workNo"]
#     fields = "__all__"
#     template_name="HR/HR_detail.html" 
#     success_url = 'OK'

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         return super().form_valid(form)

class PersonAddView(generic.edit.CreateView):
    model=Person
    template_name="HR/HR_detail.html" 
    fields="__all__"
    success_url = "OK"
    # success_url = reverse_lazy('success')
class PersonUpdateView(generic.edit.UpdateView):
    model = Person
    template_name="HR/HR_detail.html" 
    fields = "__all__"
    success_url = "OK"
class PersonDelView(generic.edit.DeleteView):
    model = Person
    template_name="HR/HR_Person_Del.html"
    success_url = "/HR/"
    