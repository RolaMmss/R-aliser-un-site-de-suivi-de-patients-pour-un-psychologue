from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username","email", "password1", "password2")