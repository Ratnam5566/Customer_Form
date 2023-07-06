from django import forms
l=[('MALE','MALE'),('FEMALE','FEMALE')]
class customerForm(forms.Form):
    First_Name=forms.CharField(max_length=100)
    Last_Name=forms.CharField(max_length=100)
    Email=forms.EmailField()
    Street_address=forms.CharField(max_length=100)
    Zip_Code=forms.IntegerField()
    Gender=forms.ChoiceField(choices=l)