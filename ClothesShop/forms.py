from django import forms

class Shoe_Form(forms.Form):
  model = forms.CharField()
  size = forms.IntegerField()

class Shirt_Form(forms.Form):
  model = forms.CharField()
  size = forms.IntegerField()

class Register_Form(forms.Form):
  name = forms.CharField()
  last_name = forms.CharField()
  last_name = forms.IntegerField()
  email = forms.EmailField()