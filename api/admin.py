from django.contrib import admin
from .models import Workspace, Invoice, Subscription

admin.site.register(Workspace)
admin.site.register(Invoice)
admin.site.register(Subscription)