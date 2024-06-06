from django import forms

class Shirt_Form(forms.Form):
  model = forms.CharField()
  size = forms.IntegerField()

class Shoe_Form(forms.Form):
  model = forms.CharField()
  size = forms.IntegerField()

class Register_Form(forms.Form):
  name = forms.CharField()
  last_name = forms.CharField()
  email = forms.EmailField()
  size = forms.IntegerField()