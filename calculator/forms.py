from django import forms
from calculator.models import Calculate, Term

class CalcForm(forms.ModelForm):
    class Meta:
        model = Calculate
        fields = '__all__'



class TermForm(forms.ModelForm):
     class Meta:
         model = Term
         fields = '__all__'

