from django.contrib import admin
from proposals.models import CustomUser, Proposal

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Proposal)
