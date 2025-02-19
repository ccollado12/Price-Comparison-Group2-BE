from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



User = get_user_model()

# create registration
class RegisterForm(forms.Form):
    username = forms.CharField(
         widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username",
                "placeholder": "Enter your username"
            }
        )
    )
    email = forms.EmailField(
         widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "user-email",
                "placeholder": "Enter your email"
            }
        )

    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "Enter password"
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password",
                "placeholder": "Confirm password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        # if username in non_allowed_usernames:
        #     raise forms.ValidationError("This is an invalid username, please pick another.")
        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another.")

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email


# create login Form
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control",
        "placeholder": "Enter your username"
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "Enter password"
            }
        )
    )
#Validating user
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user.")
        if qs.count() != 1:
            raise forms.ValidationError("This is an invalid user.")
        return username