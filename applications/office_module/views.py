from django.shortcuts import render
from .models import *
from django.http import HttpResponse,HttpResponseRedirect


def officeOfDeanStudents(request):
    context = {}

    return render(request, "officeModule/officeOfDeanStudents/officeOfDeanStudents.html", context)


def officeOfPurchaseOfficr(request):
    return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html", {})


def officeOfRegistrar(request):
    view = registrar_create_doc.objects.all()
    view2 = registrar_director_section.objects.all()
    view3 = registrar_establishment_section.objects.all()
    view4 = apply_for_purchase.objects.all()
    view5 = quotations.objects.all()
    context = {"view":view,"view2":view2,"view3":view3,"view4":view4,"view5":view5}

    return render(request, "officeModule/officeOfRegistrar/officeOfRegistrar.html", context)


def officeOfDeanRSPC(request):
    context = {}

    return render(request, "officeModule/officeOfDeanRSPC/officeOfDeanRSPC.html", context)


def officeOfDeanPnD(request):
    context = {}

    return render(request, "officeModule/officeOfDeanPnD/officeOfDeanPnD.html", context)


def genericModule(request):
    context = {}

    return render(request, "officeModule/genericModule/genericModule.html", context)




def upload(request):
    docname = request.POST.get("docname")
    purpose = request.POST.get("purpose")
    description = request.POST.get("description")
    file = request.FILES['upload']
    request = registrar_create_doc(file_name=docname, purpose=purpose, Description=description, file=file)
    request.save()
    return HttpResponseRedirect("/office/officeOfRegistrar/")

