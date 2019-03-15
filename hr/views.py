from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Employee, Technology_type, Technology, Employee_tech, Other


def index(request):
    employees = Employee.objects.order_by('id').all()
    devs = Employee_tech.objects.all()
    context = {'employees': employees,
               'devs':devs}
    return render(request, 'index.html', context)


def employee(request):
    devs = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query = request.GET['q']
        devs = Employee_tech.objects.filter(Q(employee__first_name__contains=query) |
                                            Q(employee__last_name__contains=query) |
                                            Q(technology__name__contains=query) |
                                            Q(technology_type__name__contains=query) |
                                            Q(skil_level__contains=query)
                                            )
    else:
        devs = Employee_tech.objects.all()

    others = Other.objects.all()
    technologys = Technology.objects.all()
    frameworks = Technology_type.objects.all()

    context = {'devs': devs,
               'others':others,
               'technologys':technologys,
               'frameworks':frameworks}
    return render(request, 'employee.html', context)


def employee_details(request, id):
    path = request.path
    print(path)
    print('info ' + id)
    devs = get_object_or_404(Employee_tech, id=id)
    technologys = devs.technology.all()
    technologys_type = devs.technology_type.all()
    others = devs.other.all()

    context = {
        'devs': devs,
        'technologys': technologys,
        'technologys_type':technologys_type,
        'others':others
    }
    return render(request, 'employee_details.html', context)
