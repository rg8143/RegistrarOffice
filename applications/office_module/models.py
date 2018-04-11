from django.db import models


from applications.file_tracking.models import Tracking


class Constants:
    STATUS = (
        ('0', 'unseen'),
        ('1', 'seen')
    )
    APPROVAL = (
        ('0', 'reject'),
        ('1', 'accept')
    )

    """ using file_id we can access remark on the file,create date,receive date,forward date,"""
    """ using employee_id we can access intiator name,intiator email,"""


class Registrar_File(models.Model):
                file_id = models.ForeignKey(Tracking, on_delete=models.CASCADE)
                status = models.IntegerField(choices=Constants.STATUS, default=0)
                approval = models.IntegerField(choices=Constants.APPROVAL, default=0)
                section_name = models.CharField(max_length=50)
                section_type = models.CharField(max_length=20)
