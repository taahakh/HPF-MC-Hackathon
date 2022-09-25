from math import remainder
import re
from django.shortcuts import render, redirect
from proj.models import DonorList, DonorTransactions, Project, Address, Donor, FacilityList, ProjectTransactions

def index(request):
    return render(request, "index_.html")

def home(request):
    return render(request, "home.html")

def user_viewer(request):
    return render(request, "user_viewer.html", {"content" : Donor.objects.all()})

def donation(request):

    donors = Donor.objects.all()

    dic = {
        "content" : donors,
    }

    if request.method == "GET":
        if "amount" not in request.GET or "currency" not in request.GET or "specific_project" not in request.GET:
            return redirect("home")
        dic["amount"] = request.GET["amount"]
        dic["currency"] = request.GET["currency"]
        # dic["project"] = request.GET["project"]
        dic["project_name"] = request.GET["project_name"]
        dic["specific_project"] = request.GET["specific_project"]
        

    if request.method == "POST":

        # print(request.POST["firstname"])
        # print(request.POST["email"])
        # print(request.POST["address"])
        # print(request.POST["city"])
        # print(request.POST["town"])
        # print(request.POST["postcode"])
        # print(request.POST["donationAmount"])
        
        # adding address and donor to the database
        address = Address.objects.create(
            address=request.POST["address"],
            city=request.POST["city"],
            town=request.POST["town"],
            postcode=request.POST["postcode"]
        )

        donor = Donor.objects.create(
            name=request.POST["firstname"], 
            email=request.POST["email"],
            card_last_four=0000,
            address=address,
        )

        if request.POST.get('anon') == None: 
            state = False 
        else: 
            state = True

        proj_query = Project.objects.filter(
            project_name__contains=request.POST["project_name"]
        )[0]

        locate_facilities = FacilityList.objects.filter(
            name__contains=request.POST["specific_project"],
            project=proj_query
        )[0]

        trans = DonorTransactions.objects.create(
            paid=request.POST["donationAmount"],
            currency=request.POST["currency"],
            anonymous=state,
            specific_facilities=locate_facilities,
        )

        dl = DonorList.objects.create(
            donor=donor,
            transactions=trans
        )

        ProjectTransactions.objects.create(
            project=proj_query,
            donors=dl
        )

        if request.GET["specific_project"] != None:
            update_facility_amount(locate_facilities, request.POST["donationAmount"])
        
        update_project_values(proj_query, request.POST["donationAmount"])

        return redirect("end_donating")


        # recording transaction with accordance to project
        
    return render(request, "donation.html", dic)

def update_facility_amount(facility, amount):
    # print(facility.current_ammount)
    am = int(facility.current_ammount) + int(amount)
    # print(am)
    facility.current_ammount = am
    facility.save()

def update_project_values(project, value):
    am = int(project.so_far) + int(value)
    project.so_far = am
    project.save()

def end_donating(request):
    return render(request, "thanksfordonating.html")

def add_facility(request):
    if request.method == "POST":
        proj = Project.objects.filter(project_name__contains=request.POST['f_project'])[0]
        FacilityList.objects.create(
            name=request.POST['f_name'],
            max_amount=request.POST['amount'],
            current_ammount=0,
            project=proj,
        )
        
    return redirect('manage')
    # return render(request)

def project_management(request):
    projects = Project.objects.all()
    # projects = Project.objects.filter(project_name__contains="ambegudin")
    # print(projects)
    # facility = FacilityList.objects.filter(project__in=projects)
    # print(facility)
    if request.method == "POST":
        Project.objects.create(project_name=request.POST['proj_name'], max_goal=request.POST['goal'])

    return render(request, "create_project.html", {"content" : projects})

def view_facilities(request):
    if request.method == "GET":
        projects = Project.objects.filter(project_name__contains=request.GET["proj"])
        facility = FacilityList.objects.filter(project__in=projects)
    return render(request, "view_facilities.html", {"content" : facility})