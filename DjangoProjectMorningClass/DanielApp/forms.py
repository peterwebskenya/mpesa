from django import forms
from Myapp.models import Student
def employee():
    return None

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'age', 'phoneNumber']


