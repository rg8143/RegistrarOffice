from django.contrib import admin

from .models import (DepartmentInfo, Designation, ExtraInfo, Faculty, Feedback,
                     Issue, IssueImage, Staff)
from applications.office_module.models import Registrar_File,vendor,apply_for_purchase,stock,purchase_commitee,quotations
from applications.file_tracking.models import Tracking,File



# Register your models here.
admin.site.register(IssueImage)
admin.site.register(ExtraInfo)
admin.site.register(Issue)
admin.site.register(Feedback)
admin.site.register(Staff)
admin.site.register(Faculty)
admin.site.register(DepartmentInfo)
admin.site.register(Designation)
admin.site.register(Registrar_File)
admin.site.register(vendor)
admin.site.register(purchase_commitee)
admin.site.register(quotations)
admin.site.register(stock)
admin.site.register(apply_for_purchase)
admin.site.register(File)
admin.site.register(Tracking)


