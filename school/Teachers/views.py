from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request,"index.html", {"allteachers":teachers})

def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        image = request.FILES.get("image")

        teacher = Teacher(
            name= name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None

        )
        teacher.save()
        return redirect("all-teachers")
    return render(request,"index.html")

def update_teacher(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        image = request.FILES.get("image")

        teacher = Teacher(
            id =id,
            name= name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None

        )
        teacher.save()
        return redirect("all-teachers")
    return render(request, 'teachers/index.html',{'teacher':teacher})

def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher,id=id)
    teacher.delete()
    return redirect("all-teachers")

def manager_dashboard(request):
    context = {
        "role": "Principal",
        "username": request.user.username,
        "total_teachers": Teacher.objects.count(),
    }
    return render(request, "manager_dashboard.html", context)

@login_required
def manager_logout(request):
    auth_logout(request)
    return redirect('home')
