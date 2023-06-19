from django.shortcuts import render,get_object_or_404
from django.shortcuts import render,redirect
from .forms import inscrip
from .models import emploi,programme,cour,filiaire,professeur,salle
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import empform,addcurs,addcours,validation,addprog,addprof,salform
@login_required()
def interface(request):
    form = emploi.objects.all()
    if request.method == 'POST':
        valid = validation(request.POST)
        if valid.is_valid():
            return redirect('conexion:modifier')
    else:
        valid=validation()
    return render(request,'connexion/interface.html',{"form":form,"valid":valid})

def ess(request):
    if request.method== 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username= username,password = password)

        if user is not None:
            login(request,user)
            return redirect("conexion:inter")
        else:
            messages.info(request,"Identifiant ou mot de passe incorrect")
    form =AuthenticationForm()
    return render(request,"connexion/formulaire.html",{"form":form})

@login_required()
def deco(request):
    logout(request)
    return redirect('conexion:essai')

def etudad(request):
    if request.method == 'POST':
        form = inscrip(request.POST)

        if form.is_valid():
            form.save()
            return redirect("conexion:essai")
    else:
        form=inscrip()
        
    return render(request,"connexion/inscription.html",{"form": form})


@login_required()
def presem(request,emp_id):
    emp=get_object_or_404(emploi,pk = emp_id)
    prog = programme.objects.all().filter(emploi = emp_id).order_by("hrd")
    return render(request,"connexion/presentemploi.html",{"emp":emp,"prog":prog})

@login_required()
def code(request):
   emp = emploi.objects.all()
   prof = professeur.objects.all() 
   fil = filiaire.objects.all()
   cou = cour.objects.all()
   sal = salle.objects.all()
   return render(request,"connexion/modification.html",{"emp":emp,"prof":prof,"fil":fil,"cou":cou,"sal":sal})

#les supression
@login_required()
def rememp(request,emp_id):
    emp= emploi.objects.filter(pk = emp_id)
    emp.delete()
    return redirect("conexion:modifier")
@login_required()
def remcour(request,cour_id):
    cou = cour.objects.filter(pk = cour_id)
    cou.delete()
    return redirect('conexion:modifier')
@login_required()
def remfil(request,fil_id):
    fil = filiaire.objects.filter(pk = fil_id)
    fil.delete()
    return redirect('conexion:modifier')
@login_required()
def remprof(request,prof_id):
    prof = professeur.objects.filter(pk=prof_id)
    prof.delete()
    return redirect('conexion:modifier')
@login_required()
def remsal(request,sal_id):
    sal = salle.objects.filter(pk=sal_id)
    sal.delete()
    return redirect('conexion:modifier')
@login_required()
def remprog(request,prog_id):
    sal = programme.objects.filter(pk=prog_id)
    sal.delete()
    return redirect('conexion:modifier')


#ajouter des trucs
@login_required()
def addemp(request):
    if request.method == 'POST':
        form = empform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conexion:modifier')
    else:
        form = empform()
    return render(request,"connexion/addemp.html",{"form":form})      

@login_required()
def cu(request):
    if request.method == 'POST':
        form = addcurs(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conexion:modifier')
    else:
        form = addcurs()
    return render(request,"connexion/addcurs.html",{"form":form})      


@login_required()
def cours(request):
    if request.method == 'POST':
        form = addcours(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conexion:modifier')
    else:
        form = addcours()
    return render(request,"connexion/addcou.html",{"form":form})  
@login_required() 
def pr(request,emp_id):
    if request.method == 'POST':
        form = addprog(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conexion:modifier')
    else:
        form = addprog()
    pro = programme.objects.all().filter(emploi = emp_id)
    return render(request,"connexion/addprog.html",{"form":form,"pro":pro})
@login_required
def prf(request):
    if request.method == 'POST':
        form = addprof(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conexion:modifier')
    else:
        form = addprof()
    return render(request,"connexion/addprof.html",{"form":form})
@login_required
def sal(request):
    if request.method == 'POST':
        form = salform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conexion:modifier')
    else:
        form = salform()
    return render(request,"connexion/addsal.html",{"form":form})