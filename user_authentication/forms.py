from datetime import datetime
from typing import Any

from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            try:
                user = self.Meta.model.objects.get(username=username)
            except self.Meta.model.DoesNotExist:
                user = None

            if user is not None:
                #check if the user account is locked or not
                if user.account_locked_dt is not None:
                    
                    #if locked date is not None, calculate the time difference
                    timedelta = datetime.now().replace(tzinfo=None) - user.account_locked_dt.replace(tzinfo=None)
                    
                    #if the time difference is greater than 5 minutes
                    #unlock the user
                    if timedelta.seconds > 300:
                        user.login_attempts = 0
                        user.is_active = True
                        user.account_locked_dt = None
                        user.save()

                #check if user is active
                if user.is_active:
                    #if active, check if credential is correct or not by calling authenticate function
                    self.user_cache = authenticate(username=username,
                                                   password=password)

                    #if credentials are invalid,update the login attempts and raise validation error
                    if self.user_cache is None:
                        user.login_attempts += 1;
                        if user.login_attempts < 3:
                            error_message = 'Invalid Username/Password.'
                            user.save()
                            raise forms.ValidationError(error_message)

                        #if login attempt exceeds 2, lock the account and raise validation error
                        else:
                            user.is_active = False
                            user.account_locked_dt = datetime.now()
                            user.save()
                            error_message = 'You exceeded maximum login attempts. Your account has been temporarily Inactive. Please contact Admin to reactivate.' + str(
                                user.account_locked_dt)
                            raise forms.ValidationError(error_message)
                    
                    #if user provides correct credentials before he exceeds the login attempts
                    #then let the user login and reset the login attempts if any
                    else:
                        if user.login_attempts > 0:
                            user.login_attempts = 0
                            user.save()
                        self.confirm_login_allowed(self.user_cache)

                #if user is inactive (i.e. account is locked)
                #then raise a validation error
                else:
                    error_message = 'Your account is currently Inactive. Please contact Admin to reactivate.'
                    raise forms.ValidationError(error_message)

            #if user doesn't exist in the database
            #then taise a validation error
            else:
                error_message = 'Invalid Username/Password.'
                raise forms.ValidationError(error_message)
        return self.cleaned_data
