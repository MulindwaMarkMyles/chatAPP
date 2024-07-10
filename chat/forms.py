from django import forms
from .models import Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password'
        })

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password'
        })

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']
    
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].widget.attrs.update({'id': 'recipient-select'})
        self.fields['content'].widget.attrs.update({'id': 'message-content'})
        
    
