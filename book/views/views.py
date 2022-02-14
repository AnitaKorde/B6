from multiprocessing import context
from os import name
from pyexpat import model
from re import template
import traceback
from django.shortcuts import render,redirect
from book.models import Book, Person
from django.http import HttpResponse
import logging


# Create a custom logger
logger = logging.getLogger("first")


# Create your views here.
def homepage(request):
   
   logger.info("In home page")
   books = Book.objects.all()
   logger.info(books)
    #print("in home page")
    #print(dir(request))
    #print(request.method)
    #print(request.GET)
    #print(request.POST)
   if request.method == "POST":
      logger.info(request.POST)
      if not request.POST.get("bid"):
        
         book_name = request.POST["bname"]
         book_price = request.POST["bprice"]
         book_qty = request.POST["bqty"]
      #print(book_name,book_price,book_qty)
         Book.objects.create(name=book_name,price=book_price,qty=book_qty)
         return redirect("homepage")
    #return HttpResponse("<h1>Hi Hello</h1>")
      else:
         bid=request.POST.get("bid")
         book_obj = Book.objects.get(id=bid)
         book_obj.name = request.POST["bname"]
         book_obj.price = request.POST["bprice"]
         book_obj.qty = request.POST["bqty"]
         book_obj.save()
         return redirect("show_all_book")
      
   elif request.method == "GET":
  
   
         return render(request,template_name="home.html")


""" show all books """
def show_all_book(request):
   logger.info("In show all book page")
   all_book=Book.objects.all()
   logger.info(all_book)
 
   cont = {"books":all_book}
   logger.info(request.POST) #get empty dict
   return render(request,template_name="show_book.html",context=cont)

def edit_data(request,id):
   logger.info("In edit book page")
   book = Book.objects.get(id=id)
   logger.info(book)
   
   return render(request,template_name="home.html",context={"single_book":book})

def delete_data(request,id):
   if request.method == "POST":
      try:
         logger.info("In delete perticular book data page")
         book = Book.objects.get(id=id)
         logger.debug(book)
      except Book.DoesNotExist as err_msg:
         
         #traceback.print_exc()
         #return HttpResponse(f"Book does not exist for id:-{id}")
         logger.error(f"{err_msg}------in exception")
      else:
         book.delete()
      return redirect("show_all_book")
   else:
      #return HttpResponse(f"request method: {request.method} not allowed..! only post method is allowed")
      logger.error(f"request method: {request.method} not allowed..! only post method is allowed")

""" Delete all records """
def delete_all(request):
   logger.info("In delete book page")
   all_data = Book.objects.all().delete()
   logger.info(all_data)
   return render(request,template_name = "show_book.html",context={"all_book":all_data})

def is_inactive(request):
   logger.info("In delete book page")
   all_is_inactive = Book.inactive_obj.all()
   logger.info(all_is_inactive)
   return render(request,template_name = "show_soft_delete.html",context={"all_aval_book":all_is_inactive})


""" update status of soft deleted books to n """
def update_soft_del(request,id):
   try:
      book = Book.objects.get(id=id)
   except Book.DoesNotExist as msg:
      #traceback.print_exc()
      #return HttpResponse(f"Book does not exist for id:-{id}")
      logger.error(f"{msg}-------------In exception")
   else:
      book.is_active = "n"
      book.save()
   return redirect("show_all_book")


""" restore books from soft delete """
def recover_soft_del(request,id):
   try:
      book = Book.objects.get(id=id)
   except Book.DoesNotExist as msg:
      traceback.print_exc()
      #return HttpResponse(f"Book does not exist for id:-{id}")
      logger.error(f"{msg}-------------In exception")
   else:
      book.is_active = "y"
      book.save()
   return redirect("soft_delete")


""" delete al soft deleted books """
 
def all_soft_del(request):
   logger.info("In all soft delete book page")
   all_is_inactive = Book.inactive_obj.all()
   logger.info(all_is_inactive)
   all_is_inactive.delete()
   return render(request,template_name = "show_soft_delete.html",context={"all_del_book":all_is_inactive})









from book.forms import StudentForm,CustomerForm,Employeeform,AddressForm,BookForm,PersonForm
 
# creating a form

# Create your views here.
def form_home(request):
   if request.method == "POST":
      print(request.POST)
      print("In post request")
      form = BookForm(request.POST)
      if form.is_valid():
         form.save()
      else:
         return redirect("form-home")
   elif request.method == "GET":
      print("In get request")
      context = {"form":BookForm()}
      return render(request,"form_home.html",context=context)


    #context ={"form":StudentForm()}
    #return render(request, "form_home.html", context)
#print(StudentForm())

def index(request):

	form = CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'index.html', context)

def  emp_form(request):
   form = Employeeform()
   context = {'form': form}
   return render(request,'emp_form.html',context)

def crispy_form(request):
   form = AddressForm()
   context = {'form': form}
   return render(request,'crispy_form.html',context)


"""Classbased view"""

from django.views import View

class Home(View):
   Name = None
   def get(self, request):
      print(self.Name)
      print("In get request")
      return HttpResponse("In get")

   def post(self,request):
      print(request.POST)
      print("In post request")
      return HttpResponse("In Post")
   
   def put(self,request):
      print("In put request")
      return HttpResponse("In Put")
   
   def delete(self,request):
      print("In delete request")
      return HttpResponse("In delete")
   
   def patch(self,request):
      print("In patch request")
      return HttpResponse("In patch")


"""Template View"""
from django.views.generic.base import TemplateView

class temp_cbv(TemplateView):
   #extra_context = {"value":"Python"}
   extra_context = {"form":BookForm()}
   template_name = "temp_cbv.html"



"""Create view"""

from django.views.generic.edit import CreateView  
from django.urls import reverse,reverse_lazy
  
class PersonCreate(CreateView):  #it render person_form.html itself
    model = Person  
  
    fields = '__all__'  
    success_url = reverse_lazy("personCreate")
    #"http://127.0.0.1:8000/person-gcreate/"


"""Retrive view :-List view, Detailview"""
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
  
class PersonRetrieve(ListView):  
    model = Person  

    #return render(request, person_list.html, {"object_list":data})


class PersonDetails(DetailView):
    model = Person

    #return render(request, person_detail.html, {"object":data})

"""Update view"""
from django.views.generic.edit import UpdateView

class PersonUpdate(UpdateView):  
    model = Person  
    template_name_suffix = '_update_form'  
    fields = '__all__'  
    success_url = reverse_lazy('personRetrieve')  

"""Delete view"""
from django.views.generic.edit import DeleteView

class PersonDelete(DeleteView):  
    model = Person
    success_url = reverse_lazy('personRetrieve') 
