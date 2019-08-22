from django.shortcuts import render

from .models import UserInfo, LatestProject

# Create your views here.


def index(request):
    user = UserInfo.objects.first()
    project_list = LatestProject.objects.all()
    context = {
        'full_name': user,
        'project_list': project_list
    }

    return render(request, 'home/index.html', context)
