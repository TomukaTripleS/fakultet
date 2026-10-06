from django.shortcuts import get_object_or_404, render

from .models import Department, FacultyInfo, Program


def home(request):
    faculty = FacultyInfo.objects.first()
    return render(request, "fakultet/home.html", {"faculty": faculty})


def program_list(request):
    programs = Program.objects.all()
    return render(
        request,
        "fakultet/program_list.html",
        {"programs": programs},
    )


def program_detail(request, id):
    program = get_object_or_404(Program, pk=id)
    return render(
        request,
        "fakultet/program_detail.html",
        {"program": program},
    )


def department_list(request):
    departments = Department.objects.all()
    return render(
        request,
        "fakultet/department_list.html",
        {"departments": departments},
    )


def department_detail(request, id):
    department = get_object_or_404(Department, pk=id)
    return render(
        request,
        "fakultet/department_detail.html",
        {"department": department},
    )
