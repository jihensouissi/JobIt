from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect

import authentification.views
from etudiant.models import *
from etudiant.forms import *
from . import  views
from authentification import views

from django.contrib.auth.decorators import login_required,user_passes_test

from django.shortcuts import render
import pythoncom
pythoncom.CoInitialize()
import comtypes.client

# Create your views here.

# Create your views here.
def resume(request):
    return render(request, 'etudiant/resume.html')
def etudiantHome(request):
    return render(request, 'etudiant/homeEtudiant.html')
@login_required(login_url='/signin')
@user_passes_test(authentification.views.is_student)
def resumeupload(request):
    return render(request,"etudiant/resume.html")
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'

relevtags=['Hobbies','HOBBIES','ExtraCurricularActivities','Activites','ACTIVITIES','Projects','PROJECTS','WORK','Work',
           'ACHIEVEMENTS','Achievements','SKILLS','Skills','Skill','Experience','EXPERIENCE','Qualification','QUALIFICATION','Education',
           'EDUCATION','EDUCATIONAL','Educational']
def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    wdFormatPDF = 17
    word=comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open('word/document.xml')
    doc.SaveAs(FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
