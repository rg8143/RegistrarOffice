from django.contrib import admin

from .models import (DepartmentInfo, Designation, ExtraInfo, Faculty, Feedback,
                     Issue, IssueImage, Staff)
from applications.office_module.models import Registrar_File
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
admin.site.register(File)
admin.site.register(Tracking)


