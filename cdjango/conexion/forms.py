from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import emploi,filiaire,cursus,cour,programme,professeur,salle
from django.forms.widgets import DateInput
from django.db.models import Q


class inscrip(UserCreationForm):
    class Meta:
        model = User
        fields = ['last_name','first_name','username','email']

class empform(forms.ModelForm):
    filiaire = forms.ModelChoiceField(queryset= filiaire.objects.all(),label="filiaire" )
    Annee = forms.ModelChoiceField(queryset=cursus.objects.all(),label="classe")
    class Meta:
        model = emploi
        fields = ['date','filiaire','Annee']
        widgets = {
            'date': forms.DateInput(),
        }

class addcurs(forms.ModelForm):
    class Meta:
        model = filiaire
        fields =['nom']

class addcours(forms.ModelForm):
    class Meta:
        model = cour
        fields =['nom']

class validation(forms.Form):
    code = forms.IntegerField(widget=forms.PasswordInput,label="code")

    def clean_code(self):
        code = self.cleaned_data['code']
        if code != 1234:
            raise forms.ValidationError("vous devez entrer le code administracteur avant d'aller plus loin")
        return code 

class addprog(forms.ModelForm):
    class Meta:
        model = programme
        fields = ['jour','cour','professeur','emploi','salle','hrd','hrf']
        def clean_all(self):
            sal = self.cleaned_data['salle']
            hr = self.cleaned_data['hrd']
            h =self.cleaned_data['hrf']
            em = self.cleaned_data['emploi']
            day= self.cleaned_data['jour']
            al = programme.objects.filter(Q(jour=day) & Q(emploi=em) & Q(salle=sal))
            if h<hr:
                raise forms.ValidationError("votre cour se termine anvant de commencer")
            for i in al:
                if (hr<i.hrf and hr>=i.hrd) or (h<i.hrf and h>=i.hrd):
                    raise forms.ValidationError("un cour a deja ete programmer ce jour dans cette salle")
            return sal,hr,em,day

class addprof(forms.ModelForm):
    class Meta :
        model = professeur
        fields = ['nom','prenom']
    
class salform(forms.ModelForm):
    class Meta :
        model = salle
        fields = ['nom']