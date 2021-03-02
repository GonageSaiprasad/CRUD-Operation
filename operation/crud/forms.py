from django import forms

from.models import User


class Registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','username','password','confirmpassword','mob','gender','skill']
        widgets={
        'name':forms.TextInput(attrs={'id':'name','class':'form-control'}),
        'username':forms.TextInput(attrs={'id':'username','class':'form-control'}),
        'password':forms.PasswordInput(attrs={'id':'password','class':'form-control'}),
        'confirmpassword':forms.PasswordInput(attrs={'id':'confirmpassword','class':'form-control'}),
        'mob':forms.TextInput(attrs={'id':'mob','class':'form-control'}),
        'gender':forms.TextInput(attrs={'id':'gender','class':'form-control'}),
        'skill':forms.TextInput(attrs={'id':'skill','class':'form-control'}),
        }
