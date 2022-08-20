
from dataclasses import field
from turtle import textinput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from accounts.models import User,Room,Image,Amenities


class signup_form(UserCreationForm):
    first_name = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'First Name ','class':'form-control'}))
    last_name = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Last Name ','class':'form-control'}))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'placeholder': 'Email ','class':'form-control'}))
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder': 'Password ','class':'form-control'}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation ','class':'form-control'}))
    phone_no = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Phone Number ','class':'form-control'}))
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'phone_no',
        ]
        
        
       
class DateInput(forms.DateInput):
    input_type = 'date'
          
class addRoom_form(forms.ModelForm):
    options=(
     ('category','category'),
     ('Boys','Boys',),
     ("girls",'girls'),
     ('bachelor','bachelor'),
     )
    address= forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'address ','class':'form-control','required':'false'}))
    city= forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'city ','class':'form-control'}))
    category= forms.ChoiceField( choices=options)
    price= forms.CharField( widget=forms.NumberInput(attrs={'placeholder': 'price ','class':'form-control'}))
    availablity= forms.BooleanField()
    available_on= forms.DateField( widget=forms.DateInput(attrs={'placeholder': 'available on', 'type': 'text','onfocus': "(this.type='date')",'class':'form-control'}))
    description= forms.CharField( widget=forms.Textarea(attrs={'placeholder': 'description ','rows':10,'cols':15,'class':'form-control'}))
    amenities= forms.ModelMultipleChoiceField( widget=forms.CheckboxSelectMultiple,queryset=Amenities.objects.all())
    
    def __init__(self, *args, **kwargs):
            # first call parent's constructor
        super(addRoom_form, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['availablity'].required = False
    class Meta:
        model=Room
        fields=[
            'address',
            'city',
            'category',
            'price',
            'availablity',
            'available_on',
            'description',
            'amenities',
        ]
         
        
        widgets = {
            'available_on': DateInput()
        }
        
        
class imageForm(forms.ModelForm):
    image=forms.ImageField(label='Image',widget=forms.ClearableFileInput(attrs={'multiple':True}),)
    
    class Meta:
        model=Image
        fields=('image',)
        
class AmenitiesForm(forms.ModelForm):
    class Meta:
        model=Amenities
        fields=['amenities_name',]