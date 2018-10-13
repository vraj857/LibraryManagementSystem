from datetime import datetime

from django import forms
from user_authentication.models import User


class UserUpdateForm(forms.ModelForm):
    locked = forms.BooleanField(required=False)

    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )

    def __init__(self, *args, **kwargs):
        # extract user data from kwargs
        self.user = kwargs.pop('user', None)
        self.user_locked = kwargs.pop('user_locked', None)

        super(UserUpdateForm, self).__init__(*args, **kwargs)

        # initial form content
        self.fields['first_name'].initial = self.user.first_name
        self.fields['email'].initial = self.user.email
        self.fields['locked'].initial = self.user_locked
        # self.fields['locked'].widget.attrs['class'] = 'switch slider_round'

    class Meta:
        model = User
        fields = ('first_name', 'email')

    def clean(self):
        self.user.first_name = self.cleaned_data.get('first_name')
        self.user.email = self.cleaned_data.get('email')
        locked = self.cleaned_data.get('locked')

        if locked is False:
            self.user.login_attempts = 0
            self.user.is_active = True
            self.user.account_locked_dt = None

        else:
            self.user.login_attempts = 3
            self.user.is_active = False
            if (self.user.account_locked_dt is None):
                self.user.account_locked_dt = datetime.now()

        return self.cleaned_data

    def save(self, commit=True):

        user, created = User.objects.update_or_create(id=self.user.id, defaults={'first_name': self.user.first_name,
                                                                                 'email': self.user.email,
                                                                                 'login_attempts': self.user.login_attempts,
                                                                                 'is_active': self.user.is_active,
                                                                                 'account_locked_dt': self.user.account_locked_dt})

        return user
