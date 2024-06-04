from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import College, Major, Subject

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class RegistrationForm(forms.Form):
    college = forms.ModelChoiceField(queryset=College.objects.all())
    major = forms.ModelChoiceField(queryset=Major.objects.all(), required=False)
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        college_id = kwargs.pop('college_id', None)
        major_id = kwargs.pop('major_id', None)
        super().__init__(*args, **kwargs)
        if college_id:
            self.fields['major'].queryset = Major.objects.filter(college_id=college_id)
        if major_id:
            self.fields['subject'].queryset = Subject.objects.filter(major_id=major_id)
