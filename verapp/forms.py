from .models import StudebtRegistration
from django import forms
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=StudebtRegistration
        fields=['studentName',
        'studentId',
        'studentClass',
        'StudentGuardiandName',
        'StudentCollegeName',
        'studentPasssword']
        widgets={
        'studentName':forms.TextInput(attrs={'class':'form-control'}),
        'studentId':forms.TextInput(attrs={'class':'form-control'}),
        'studentClass':forms.TextInput(attrs={'class':'form-control'}),
        'StudentGuardiandName':forms.TextInput(attrs={'class':'form-control'}),
        'StudentCollegeName':forms.TextInput(attrs={'class':'form-control'}),
        'studentPasssword':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }
