from django.contrib import admin

# Register your models here.
from proposals.models import CustomUser, Proposal

admin.site.register(CustomUser)
admin.site.register(Proposal)
