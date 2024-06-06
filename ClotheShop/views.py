from django.shortcuts import render
from .forms import Shoe_Form, Shirt_Form, Register_Form
from .models import Shoe, Shirt, User

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
  
def register(req):
  if req.method == 'POST':
    my_form = Register_Form(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      new_user = User(name = data['name'], last_name = data['last_name'], email = data['email'])
      new_user.save()
      return render(req, 'init.html',{'message': 'user created'}) 
    else:
      return render(req, 'shirt.html',{'message': 'invalid data'}) 
  else:
    my_form = Register_Form()
    return render(req, 'init.html',{'my_form': my_form})

def shoes(req):
  all_shoes = Shoe.objects.all()
  return render(req, 'shoes.html', {'shoes': all_shoes})

def shirts(req):
  all_shirts = Shoe.objects.all()
  return render(req, 'shirts.html', {'shirts': all_shirts})

"""
def search_curse(req):
  if req.GET["category"]:
    category = req.GET["category"]
    curses_finded = Curse.objects.filter(category__icontains = category)
    return render(req, 'search_curse.html', {'curses': curses_finded, 'category': category})
  else:
    return render(req, 'init.html', {'message': 'category not sended'})
 """