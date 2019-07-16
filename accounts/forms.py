from django import forms
from .models import Profile,Company

class ProfileForm(forms.ModelForm):
    class Meta :
        model = Profile
        fields = ("user","Email","company","Phone","SSN","Address")


class CompanyForm(forms.ModelForm):
    class Meta :
        model = Company
        fields = ("Name")

