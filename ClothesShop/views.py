from django.shortcuts import render
from django.http import HttpResponse
from .forms import Shoe_Form, Shirt_Form, Seller_Form
from .models import Shoe, Shirt, Seller

# Create your views here.
def init(req):
    return render(req, 'init.html',{})

def shoe_form(req):
  if req.method == 'POST':
    my_form = Shoe_Form(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      new_shoe = Shoe(model = data['model'], size = data['size'])
      new_shoe.save()
      return render(req, 'init.html',{'message': 'shoe created'}) 
    else:
      return render(req, 'shoe.html',{'message': 'invalid data'}) 
  else:
    my_form = Shoe_Form()
    return render(req, 'shoe.html',{'my_form': my_form})
  
def shirt_form(req):
  if req.method == 'POST':
    my_form = Shirt_Form(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      new_shirt = Shirt(model = data['model'], size = data['size'])
      new_shirt.save()
      return render(req, 'init.html',{'message': 'shirt created'}) 
    else:
      return render(req, 'shirt.html',{'message': 'invalid data'}) 
  else:
    my_form = Shirt_Form()
    return render(req, 'shirt.html',{'my_form': my_form})
  
def seller_form(req):
  if req.method == 'POST':
    my_form = Seller_Form(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      new_seller = Shirt(model = data['model'], size = data['size'])
      new_seller.save()
      return render(req, 'init.html',{'message': 'shirt created'}) 
    else:
      return render(req, 'shirt.html',{'message': 'invalid data'}) 
  else:
    my_form = Shirt_Form()
    return render(req, 'shirt.html',{'my_form': my_form})

def shoes(req):
  return render(req, 'shoes.html')

def shirts(req):
  return render(req, 'shirts.html')

""" def curse(req, name, category):
  new_curse = Curse(name = name, category = category)
  new_curse.save()
  return HttpResponse(f'curso creado')

def get_curses(req):
  curses = Curse.objects.all()
  return render(req, 'get_curses.html',{'curses':curses})




def curses(req):
  return render(req, 'curses.html',{})

def teachers(req):
  return render(req, 'teachers.html',{})

def students(req):
  return render(req, 'students.html',{})

def works(req):
  return render(req, 'works.html',{})

def add_curse(req):
  if req.method == 'POST':
    my_form = Curse_Form(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      new_curse = Curse(name = data['name'], category = data['category'])
      new_curse.save()
      return render(req, 'init.html',{'message': 'curse created'}) 
    else:
      return render(req, 'init.html',{'message': 'invalid data'}) 
  else:
    my_form = Curse_Form()
    return render(req, 'curse_form.html',{'my_form': my_form}) 
  
def search_category(req):
  return render(req, 'search_category.html', {})

def search_curse(req):
  if req.GET["category"]:
    category = req.GET["category"]
    curses_finded = Curse.objects.filter(category__icontains = category)
    return render(req, 'search_curse.html', {'curses': curses_finded, 'category': category})
  else:
    return render(req, 'init.html', {'message': 'category not sended'})
 """