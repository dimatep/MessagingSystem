from django.contrib import admin
from . models import Message
# Register your models here.
# here I decide how the administrative panel of this app will look like

admin.site.register(Message)    # must register this model

