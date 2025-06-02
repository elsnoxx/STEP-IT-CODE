from django.shortcuts import render, redirect
from .models import Department

# Create your views here.
def index(request):
    dept = Department.objects.all()
    print(dept)
    return render(request, 'index.html', {'dept' : dept})

def dept_detail(req, deptno):
    dept = Department.objects.get(deptno=deptno)
    return render(req, 'dept_detail.html', {'dept' : dept})

def dept_edit(req, deptno):
    dept = Department.objects.get(deptno=deptno)
    if req.method == 'POST':
        dept.deptname = req.POST['dname']
        dept.save()
        return redirect('/')

    return render(req, 'dept_edit.html', {'dept' : dept})

def dept_delete(req, deptno):
    dept = Department.objects.get(deptno=deptno)
    if req.method == 'POST':
        dept.delete()
        return redirect('/')
    return render(req, 'dept_delete.html', {'dept' : dept})

def dept_add(req):
    if req.method == 'POST':
        deptname = req.POST['dname']
        Department.objects.create(
            deptname=deptname
        )
        return redirect('/')

    return render(req, 'dept_add.html')