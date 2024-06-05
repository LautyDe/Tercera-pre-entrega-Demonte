from django import forms

class Shoe_Form(forms.Form):
  model = forms.CharField()
  size = forms.IntegerField()

class Shirt_Form(forms.Form):
  model = forms.CharField()
  size = forms.IntegerField()

