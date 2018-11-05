from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from . forms import DashboardForm,UploadForm,FindForm
from . models import Student,Books,Branch,Semester
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    # if not request.user.is_authenticated:
    #     return render(request, "main/signin.html", {"message": None})
    # context = {
    #     "user": request.user
    # }
    # return render(request, "main/index.html", context)
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
        "user": request.user
    }
    if request.user.is_authenticated:
        return render(request,'main/index.html',context)

def login(request):
    # email = request.POST["email"]
    # password = request.POST["password"]
    # user = authenticate(request, email=email, password=password)

    # if user is not None:
    #     login(request, user)
    #     return HttpResponseRedirect(reverse("index"))
    # else:
    #     return render(request, "main/signin.html", {"message": "Invalid credentials."})
    
    return render(request,'registration/login.html')

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request,'registration/register.html',context)

def logout(request):
    auth_logout(request)
    return render(request, "registration/login.html", {"message": "Logged out."})
@login_required
def dashboard(request):
    user = request.user
    if request.method == 'POST':
        form = DashboardForm(request.POST)

        if form.is_valid():
            new_update = Student(username=user,phone=request.POST['phone'])
            new_update.save()
            return redirect('index')
    else:

        form = DashboardForm()
    try:
        student = Student.objects.get(username=user)
        book = Books.objects.filter(upload_id=user)
    except Exception as e:
        student = e
        book = e
    context = {'form':form,'student':student,'book':book}
    return render(request,'main/dashboard.html',context)
@login_required
def findBooks(request):
    user=request.user
    if request.method == "POST":
        form = FindForm(request.POST)
        if form.is_valid():
            branch = Branch.objects.get(name=form.cleaned_data['branch_name'])
            semester = Semester.objects.get(values=form.cleaned_data['semester'])
            result = Books.objects.filter(branch=branch,semester=semester)
            # phone = []
            # for i in result:
            #     phone.append(Student.objects.get(username=i.upload_id))
            context = {'result':result,'media_url':settings.MEDIA_URL}
            return render(request,'main/result.html',context)
    else:
        form = FindForm()
    context = {'form':form}
    return render(request,'main/findBooks.html',context)
@login_required
def upload(request):
    user=request.user
    if request.method == "POST":
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            branch = Branch.objects.get(name=form.cleaned_data['branch_name'])
            semester = Semester.objects.get(values=form.cleaned_data['semester'])
            book_url = form.cleaned_data['image']
            new_book = Books(name=name,branch=branch,semester=semester,upload_id=user,book_url=book_url)
            new_book.save()
            return redirect('index')
    else:
        form = UploadForm()
    context = {'form':form}
    try:
        student = Student.objects.get(username=user)
    except Exception as e:
        return redirect('dashboard')
    return render(request,'main/upload.html',context)

@login_required
def details(request, user_id):
    try:
        # user = User.objects.get(pk=user_id)
        user = get_object_or_404(User,pk=user_id)
        student = get_object_or_404(Student,username=user)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    context={'user':user,'student':student}
    return render(request,'main/details.html',context)

def result(request):
    user = request.user
    result = Books.objects.filter(upload_id=user)
    context = {'result':result,'media_url':settings.MEDIA_URL}
    return render(request,'main/results.html',context)

def delete(request,book_id):
    book = Books.objects.get(id=book_id)
    book.delete()
    return redirect('index')