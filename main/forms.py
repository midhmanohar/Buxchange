from django import forms

branch_choices = [
    ('Civil engineering','Civil engineering'),
    ('Computer science & engineering','Computer science & engineering'),
    ('Electrical & electronics engineering','Electrical & electronics engineering'),
    ('Electronics & communication engineering','Electronics & communication engineering'),
    ('Mechanical engineering','Mechanical engineering'),
]

semester_choices = [
    ('S1&S2','S1&S2'),
    ('S3','S3'),
    ('S4','S4'),
    ('S5','S5'),
]

class DashboardForm(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    phone = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))

class UploadForm(forms.Form):
    branch_name = forms.CharField(widget=forms.Select(choices=branch_choices,attrs = {'class' : 'form-control'}))
    semester = forms.CharField(widget=forms.Select(choices=semester_choices,attrs = {'class' : 'form-control'}))
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name of book'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

class FindForm(forms.Form):
    branch_name = forms.CharField(widget=forms.Select(choices=branch_choices,attrs={'class':'form-control'}))
    semester = forms.CharField(widget=forms.Select(choices=semester_choices,attrs = {'class' : 'form-control'}))
