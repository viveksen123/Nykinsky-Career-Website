from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import AllTeam
from .models import  Job
from .models import Application
from .forms import Form

def index(request):
    return render(request,'index.html')
def career(request):
    # all_teams = AllTeam.objects.all()
    # uteam = AllTeam.objects.values('team').distinct()
    # uteam_types = AllTeam.objects.values('team_type','team').distinct()
    #
    # return render(request, 'index.html', {'data': all_teams,'uteam': uteam,'uteam_types': uteam_types})
    all_teams = Job.objects.all()
    uteam = Job.objects.values('title').distinct()
    uteam_types = Job.objects.values('title', 'job_name').distinct()

    return render(request, 'career.html', {'data': all_teams, 'uteam': uteam, 'uteam_types': uteam_types})
# Create your views here.

def team_detail(request):
    id = request.GET.get('id', None)
    print(id)
    if id is not None:
         team_details = get_object_or_404(Job, id=id)
         return render(request, 'team_detail.html', {'team_details': team_details})
    else:
        # Handle the case when the job_name parameter is not provided
        return HttpResponse("Job name not specified in the URL.")

def applicant(request):
    id = request.GET.get('id', None)
    print(id)
    if id is not None:
         team_details = get_object_or_404(Job, id=id)
         return render(request, 'applicant.html', {'team_details': team_details})
    else:
        # Handle the case when the job_name parameter is not provided
        return HttpResponse("Job name not specified in the URL.")


def submit(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"po_pup.html",{'status':"Success", 'message':"Application submitted successfully"})

        else:
            return render(request,"po_pup.html",{'status':"Failure", 'message':"Application submition is failed"})
    else:
        form = Form()
    return render(request,"po_pup.html",{'status':"Failure", 'message':"Application submition is failed"})