
# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import User, UserRole


class UserAdmin(ModelAdmin):
    list_display = ['first_name','username','email','user_role','is_active','last_login','login_attempts']

    #
    # def role(self,obj):


#     #     return "\n".join([u.user_role_id for u in obj.user_role.all()])
# # Register your models here.

admin.site.register(User,UserAdmin)
admin.site.register(UserRole)
