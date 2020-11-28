from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from restaurants.models import Account, Menu, Order

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name',
                    'phone_number', 'date_joined', 'is_staff')
    search_field = ('email', 'first_name', 'last_name')
    read_only = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Menu)
admin.site.register(Order)
