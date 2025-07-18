from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            "first_name",
            "username",
            "email",
            "password"
        ]
        
    def save(self):
        user = super().save(commit = True)
        user.set_password(self.cleaned_data["password"])
        user.save() 
        
        from profiles.models import UserProfile
        UserProfile.objects.create(user=user)
        
        return user
    

class loginForm(forms.Form):
    username = forms.CharField(label ="Email")
    password = forms.CharField(label="Pasword", widget=forms.PasswordInput())   