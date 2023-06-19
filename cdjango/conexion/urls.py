from django.urls import path
from . import views 
app_name="conexion"

urlpatterns=[
     path('inter/',views.interface,name="inter"),
#     path('etudiant/',views.etudiant,name="etud"),
#     path('admi/',views.ad,name="admn"),
     path('inscription/',views.etudad,name="etudadd"),
     path('',views.ess,name="essai"),
     path('emploi<int:emp_id>/',views.presem,name="show"),
     path('deconexion/',views.deco,name="deco"),
     path('modifier/',views.code,name="modifier"),
     path('supprimeremploie<int:emp_id>/',views.rememp,name="supemp"),
     path('supprimercour<int:cour_id>/',views.remcour,name="supcour"),
     path('supprimerfiliaire<int:fil_id>/',views.remfil,name="supfil"),
     path('supprimerprof<int:prof_id>/',views.remprof,name="supprof"),
     path('supprimersalle<int:sal_id>/',views.remsal,name="supsal"),
     path('supprimerprog<int:prog_id>/',views.remprog,name="supprog"),
     path('addemp/',views.addemp,name="addemp"),
     path('addprof/',views.prf,name="addprof"),
     path('addcurs/',views.cu,name="cur"),
     path('addcours/',views.cours,name="cour"),
     path('addprog<int:emp_id>/',views.pr,name="addprog"),
     path('addsalle/',views.sal,name="sal"),
#     path('acceuiletud/',views.accetu,name="accetu")
]