from django.contrib import admin

from .models import BookJob, Job, JobBegin, Leave , Bonus , Payroll , Salary

# Register your models here.


admin.site.register(Leave)
admin.site.register(Bonus)
admin.site.register(Payroll)
admin.site.register(Salary  )