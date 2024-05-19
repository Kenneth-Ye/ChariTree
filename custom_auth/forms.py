from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account

class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ("username", "email", "is_admin", "is_charity", "wallet_addr")

class AccountChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Account
        fields = ("username", "email", "is_admin", "is_charity", "wallet_addr")
