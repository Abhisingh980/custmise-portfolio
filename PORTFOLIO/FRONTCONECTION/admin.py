from django.contrib import admin
from .models import Project, Contact, corosel, posts, services_des

# Register your models here.

admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(corosel)
admin.site.register(posts)
admin.site.register(services_des)
