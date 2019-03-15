from django.contrib import admin
from .models import Employee, Technology, Employee_tech, Technology_type, Other

admin.site.register(Employee_tech)
admin.site.register(Employee)
admin.site.register(Technology)
admin.site.register(Technology_type)
admin.site.register(Other)
