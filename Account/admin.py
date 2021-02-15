from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Account.models import User

# Register your models here.

UserAdmin.fieldsets[2][1]['fields'] = (
                                          'is_active',
                                          'is_staff',
                                          'is_superuser',
                                          'groups',
                                          'is_author',
                                          'user_permissions',
                                      ),

UserAdmin.fieldsets += (
    ("Bio", {'fields': ('bio',)}),
)

UserAdmin.list_display += ('is_author',)

admin.site.register(User, UserAdmin)
