from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import AccountCreationForm, AccountChangeForm
from .models import Account

class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    list_display = ["username", "email", "is_admin", "is_charity", "wallet_addr"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_admin', 'is_charity', 'wallet_addr')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_admin', 'is_charity', 'wallet_addr')}),
    )

admin.site.register(Account, AccountAdmin)
