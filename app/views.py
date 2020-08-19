from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(username = u , password = p)
        try:
            if user:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error' : error}

    return render(request, 'user_login.html',d)

def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u , password = p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error' : error}

    return render(request, 'login_admin.html',d)

def user_signup(request):
    error = ""
    if request.method == 'POST':
        f= request.POST['first_name']
        l= request.POST['last_name']
        c= request.POST['contact']
        e= request.POST['e_mail']
        p= request.POST['password']
        b = request.POST['branch']
        r = request.POST['role']
        q = request.FILES['photo']

        try:
            user = User.objects.create_user(username = e,password = p,first_name = f,last_name = l)
            Signup.objects.create(user=user,contact = c, branch =b,role =r,photo =q)
            error = "no"
        except:
            error = "yes"
    d = {'error':error} 
    return render(request, 'user_signup.html', d)

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin.html')

    pending_notes = Notes.objects.filter(status='pending')
    accepted_notes = Notes.objects.filter(status='accept')
    rejected_notes = Notes.objects.filter(status='reject')
    allnotes_admin = Notes.objects.all()

    p = 0
    a = 0
    r = 0
    all = 0

    for i in pending_notes:
        p+=1

    for j in accepted_notes:
        a+=1
    
    for k in rejected_notes:
        r+=1

    for l in allnotes_admin:
        all+=1

    d = {'p':p, 'a':a, 'r': r, 'all':all}



    return render(request, 'admin_home.html',d)

def admin_logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    user = User.objects.get(id = request.user.id)
    data = Signup.objects.get(user = user)
    d = {'data':data, 'user':user}
    return render(request, 'profile.html',d)

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error =""

    if request.method == 'POST':
        c = request.POST['current']
        n = request.POST['new']
        f = request.POST['confirm']
        if f == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "no"
        else:
            error = "yes"
    d = {'error':error}
    return render(request, 'change_password.html', d)

def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error =""
    if request.method == 'POST':
        b = request.POST['branch']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['desc']
        ct = User.objects.filter(username=request.user.username).first()
        try:
            up = Notes(user=ct,uploading_date=date.today(),branch=b,subject=s,notesfile=n,filetype=f,description=d,
            status='pending')
            up.save()
            error ="no"
        except:
            error = "yes"
    stud = User.objects.all()
    d = {'error': error, 'stud': stud}
    return render(request, 'upload_notes.html',d)

def viewmy_notes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user=user)
    d = {'notes': notes}
    return render(request, 'viewmy_notes.html',d)

def deletemy_notes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')

    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('viewmy_notes')


def viewall_notes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes = Notes.objects.filter(status='accept')
    d = {'notes': notes}
    return render(request, 'viewall_notes.html',d)

def view_users(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    users = Signup.objects.all()
    d = {'users': users}
    return render(request, 'view_users.html',d)

def delete_users(request, pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    users = Signup.objects.get(id=pid)
    users.delete()
    return redirect('view_users')

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error =""
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        c = request.POST['contact']
        b = request.POST['branch']
        try:
            user.first_name = f
            user.last_name = l
            user.username = u
            data.contact = c
            data.branch = b
            data.save()
            data.user.save()
            user.save()
            error= "no"
            return redirect('profile')
        except:
            error = "yes"

    d = {'data': data, 'error':error}
    return render(request, 'edit_profile.html', d)

def pending_notes(request):
    if not request.user.is_staff:
        return redirect('login_admin')

    status = Notes.objects.filter(status='pending')
    d = {'status': status}
    return render(request, 'pending_notes.html', d)

def rejected_notes(request):
    if not request.user.is_staff:
        return redirect('login_admin')

    status = Notes.objects.filter(status='reject')
    d = {'status': status}
    return render(request, 'rejected_notes.html',d)

def accepted_notes(request):
    if not request.user.is_staff:
        return redirect('login_admin')

    status = Notes.objects.filter(status='accept')
    d = {'status': status}
    return render(request, 'accepted_notes.html',d)

def allnotes_admin(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    notes = Notes.objects.all()
    d = {'notes': notes}
    return render(request, 'allnotes_admin.html',d)

def deletenotes_admin(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')

    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('allnotes_admin')

def status(request,pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    
    stat = Notes.objects.get(id=pid)
    if request.method == 'POST':
        s = request.POST['status']
        try:
           stat.status = s
           stat.save()
           return redirect('allnotes_admin')
        except:
            return redirect('status')
    
    d = {'stat':stat}
    return render(request, 'status.html',d)

