from django.contrib import admin

from .models import User,Owner,Admin
admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Admin)
