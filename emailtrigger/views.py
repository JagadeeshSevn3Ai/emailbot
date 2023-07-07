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

    toemail = request.POST.get('toemail')
    ccemail = request.POST.get('ccemail')
    totext = request.POST.get('totext')
    cctext = request.POST.get('cctext')
    fromemail = request.POST.get('fromemail')
    fromccemail = request.POST.get('fromccemail')
    fromtext = request.POST.get('fromtext')
    fromcctext = request.POST.get('fromcctext')
    panchayat = request.POST.get('panchayat')
    arepollingboth = request.POST.get('arepollingboth')
    nameofaccused = request.POST.get('nameofaccused')

    natureofcomplaint = json.loads(request.POST.get('natureofcomplaint'))
    
    # print(natureofcomplaint)
    # print(type(natureofcomplaint))
    # print(name,address,city,state,pincode,panchayat,area,nameofaccused)

    emailcontent = {}
    emailcontent['toemail'] = toemail
    emailcontent['ccemail'] = ccemail
    emailcontent['totext'] = totext
    emailcontent['cctext'] = cctext
    emailcontent['fromemail'] = fromemail
    emailcontent['fromccemail'] = fromccemail
    emailcontent['fromtext'] = fromtext
    emailcontent['fromcctext'] = fromcctext
    emailcontent['panchayat'] = panchayat
    emailcontent['arepollingboth'] = arepollingboth
    emailcontent['nameofaccused'] = nameofaccused   
    evidencefile = request.FILES.get('evidencefile')
    # print(uploadtext, "===========", freetext , "+++++",uploadimage1.name)
    # newdoc = Document(uploadimage=uploadimage)
    Botfiles.objects.create(Botfile=evidencefile)

    # print(emailcontent)
    sendemailrespornse = sendemailfun(emailcontent,evidencefile,natureofcomplaint)
    print(sendemailrespornse)

    return JsonResponse(output)