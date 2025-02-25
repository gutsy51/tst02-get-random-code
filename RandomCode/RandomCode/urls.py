from django.contrib import admin
from django.urls import path, include, reverse_lazy

from django.views.generic import CreateView
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationWithEmailForm(UserCreationForm):
    """ Extended UserCreationForm with additional e-mail field. """

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('codeAuth.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationWithEmailForm,
            success_url=reverse_lazy('index'),
        ),
        name='registration',
    ),
]
