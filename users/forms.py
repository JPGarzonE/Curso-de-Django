"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile

class SignUpForm(forms.Form):
    """Sign up form.
    
    validate the sign up inputs
    """

    username = forms.CharField(min_length = 4, max_length = 20)

    password = forms.CharField(max_length = 70, widget = forms.PasswordInput() )
    password_confirmation = forms.CharField(max_length = 70, widget = forms.PasswordInput() )

    first_name = forms.CharField(min_length = 2, max_length = 50)
    last_name = forms.CharField(min_length = 2, max_length = 50)

    email = forms.CharField(min_length = 6, max_length = 70, widget = forms.EmailInput() )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']

        username_taked = User.objects.filter(username = username).exists()

        if username_taked:
            raise forms.ValidationError('Username is alredy in use.')

        return username

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()

        password = data.get('passwd')
        password_confirmation = data.get('passwd_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match')

        return data

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user = user)
        profile.save()



class ProfileForm( forms.Form ):
    """Profile form."""

    website = forms.URLField( max_length = 200, required = True )
    biography = forms.CharField( max_length = 500, required = True )
    phone_number = forms.CharField( max_length = 20, required = False )
    picture = forms.ImageField(required=False)