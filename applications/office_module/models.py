from django.db import models
import datetime


from applications.globals.models import ExtraInfo, Designation, DepartmentInfo, Staff, Faculty
# Create your models here.h
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

PURCHASE_STATUS = (

        ('0', "Pending"),
        ('1', "Approve"),
        ('2', "Items Ordered"),
        ('3', "Items Puchased"),
        ('4', "Items Delivered"),

    )

APPROVE_TAG = (

        ('0', "Pending"),
        ('1', "Approve"),
    )

PURCHASE_TYPE = (

        ('0', "Amount < 25000"),
        ('1', "25000<Amount<250000"),

        ('2', "250000<Amount < 2500000"),
        ('3', "Amount>2500000"),

    )

NATURE_OF_ITEM1 = (
        ('0', "Non-consumable"),
        ('1', "Consumable"),

    )
NATURE_OF_ITEM2 = (
        ('0', "Equipment"),
        ('1', "Machinery"),
        ('2', "Furniture"),
        ('3', "Fixture"),

    )

ITEM_TYPE = (
        ('0', "Non-consumable"),
        ('1', "Consumable"),

    )

""" using file_id we can access remark on the file,create date,receive date,forward date,"""
""" using employee_id we can access intiator name,intiator email,"""


class Registrar_File(models.Model):
                file_id = models.ForeignKey(Tracking, on_delete=models.CASCADE)
                status = models.IntegerField(choices=Constants.STATUS, default=0)
                approval = models.IntegerField(choices=Constants.APPROVAL, default=0)
                section_name = models.CharField(max_length=50)
                section_type = models.CharField(max_length=20)

class vendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_address = models.CharField(max_length=200)


class apply_for_purchase(models.Model):
    indentor_name = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='indentor_name')
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    inspecting_authority = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='inspecting_authority')
    expected_purchase_date = models.DateField()
    order_date = models.DateField(default=datetime.date.today)
    purchase_status = models.IntegerField(choices=PURCHASE_STATUS, default='0')
    purchase_officer = models.ForeignKey(Staff, on_delete=models.CASCADE)
    amount = models.IntegerField(default='0')
    purchase_date = models.DateField()

    registrar_approve_tag = models.IntegerField(choices=APPROVE_TAG, default='0')
    accounts_approve_tag = models.IntegerField(choices=APPROVE_TAG, default='0')

    purchase_type = models.IntegerField(choices=PURCHASE_TYPE, default='0')
    purpose = models.CharField(max_length=200)

    budgetary_head = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='bud_head')
    invoice = models.FileField()
    nature_of_item1 = models.IntegerField(choices=NATURE_OF_ITEM1, default='0')
    nature_of_item2 = models.IntegerField(choices=NATURE_OF_ITEM2, default='0')

    item_name = models.CharField(max_length=100)
    expected_cost = models.IntegerField(default='0')
    quantity = models.IntegerField(default='0')

class stock(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default='0')

    item_type = models.IntegerField(choices=ITEM_TYPE, default='0')


class purchase_commitee(models.Model) :
    local_comm_mem1 = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='local_comm_mem1')
    local_comm_mem2 = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='local_comm_mem2')
    local_comm_mem3 = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='local_comm_mem3')
    approve_mem1 = models.IntegerField(choices=APPROVE_TAG, default ='0')
    approve_mem2 = models.IntegerField(choices=APPROVE_TAG, default ='0')
    approve_mem3 = models.IntegerField(choices=APPROVE_TAG, default ='0')


class quotations(models.Model) :
    quotation1 = models.FileField()
    quotation2 = models.FileField()

class registrar_create_doc(models.Model):
    file_name = models.CharField(max_length=50)
    purpose =  models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    file=models.FileField()

class registrar_director_section(models.Model):
        file_name = models.CharField(max_length=50)
        date = models.DateField()
        purpose = models.CharField(max_length=100)
        status = models.CharField(max_length=1,choices=Constants.STATUS, default=0)


class registrar_purchase_sales_section(models.Model):
    file_name = models.CharField(max_length=50)
    member1 = models.CharField(max_length=50)
    member2 = models.CharField(max_length=50)
    member3 = models.CharField(max_length=50)
    date = models.DateField()
    purpose = models.CharField(max_length=100)
    status = models.IntegerField(choices=Constants.STATUS, default=0)
    file = models.FileField()

class registrar_finance_section(models.Model):
        file_name = models.CharField(max_length=50)
        date = models.DateField()
        purpose = models.CharField(max_length=100)
        status = models.IntegerField(choices=Constants.STATUS)
        file = models.FileField()


class registrar_establishment_section(models.Model):
    person_name = models.CharField(max_length=50)
    person_mail_id = models.CharField(max_length=50,default="xyz")
    date = models.DateField()
    duration = models.IntegerField()
    post = models.CharField(max_length=100)
    file = models.FileField()

class registrar_general_section(models.Model):
    file_name = models.CharField(max_length=50)
    date = models.DateField()
    amount = models.IntegerField()
    status = models.IntegerField(choices=Constants.STATUS, default=0)
    file = models.ForeignKey(registrar_create_doc, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.file_name & self.purpose & self.Description & self.file