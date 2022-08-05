from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# ============================================================================ #
from .models import User

# ============================================================================ #


# ============================= CREATE USER FORM ============================= #


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"


# ============================= CHANGE USER FORM ============================= #


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"
