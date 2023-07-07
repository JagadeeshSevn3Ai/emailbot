from django.http import HttpResponse
from django.shortcuts import render
from emailtrigger.models import Botfiles
from django.http import JsonResponse
from emailtrigger.sendemail import sendemailfun
import json

# Create your views here.
def login(request):
    return render(request,"login.html")

def logincheck(request):
    output = ""
    name = request.POST.get('name')
    password = request.POST.get('password')
    if name == "admin" and password == "admin":
        output = {"result":"login success"}
    else:
        output = {"result":"login failed"} 

    return JsonResponse(output)

def landingpage(request):
    return render(request, "index.html")

def uploadfile(request):
    output = {"okay":"Process Completed"}

    name = request.POST.get('name')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    pincode = request.POST.get('pincode')
    panchayat = request.POST.get('panchayat')
    area = request.POST.get('area')
    nameofaccused = request.POST.get('nameofaccused')
    natureofcomplaint = json.loads(request.POST.get('natureofcomplaint'))
    
    print(natureofcomplaint)
    print(type(natureofcomplaint))
    # print(name,address,city,state,pincode,panchayat,area,nameofaccused)

    emailcontent = {}
    emailcontent['name'] = name
    emailcontent['address'] = address
    emailcontent['city'] = city
    emailcontent['state'] = state
    emailcontent['pincode'] = pincode
    emailcontent['panchayat'] = panchayat
    emailcontent['area'] = area
    emailcontent['nameofaccused'] = nameofaccused   
    evidencefile = request.FILES.get('evidencefile')
    # print(uploadtext, "===========", freetext , "+++++",uploadimage1.name)
    # newdoc = Document(uploadimage=uploadimage)
    Botfiles.objects.create(Botfile=evidencefile)

    print(emailcontent)
    # sendemailrespornse = sendemailfun(emailcontent,evidencefile)
    # print(sendemailrespornse)

    return JsonResponse(output)