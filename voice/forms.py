from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Thread, Message


#default fields of UserCreationForm are username, password1, password2
class NewUserForm (UserCreationForm):
    #email is the instance of EmailField class
    email = forms.EmailField(required=True)


    # common attributes for Meta class are model, fields, exclude, widgets, labels etc..
    class Meta:
        # indicating that the form NewUserForm is associated with User model in the database
        model = User
        fields  = ('username', 'first_name', 'last_name','email', 'password1', 'password2')

    #commit = False means data will not be immediately saved 
    def save(self, commit = True):
        #super allows you to call the save() of the parent class
        #to user ht esuper method, you need to pass the parent class and 
        #self allows you to pass the current instance of the  chlid class to the parent class method
        #returns the isntance of User model that is obtained by save() 
        #User would have data entered in the form
        user = super (NewUserForm, self).save(commit = False)
        if commit: 
            user.save()
        return user
    
class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'