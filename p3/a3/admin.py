from django.contrib import admin
from. models import Leaves ,Assign_sub,Salary,Profile  , Feedback, Syl_updates
# Register your models here.
admin.site.register(Leaves)
admin.site.register(Feedback)
admin.site.register(Salary)
admin.site.register(Profile)
admin.site.register(Assign_sub)
admin.site.register(Syl_updates)