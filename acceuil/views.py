from django.shortcuts import render

import JobIt.settings
# Create your views here.
def home(request):
    return render(request, 'acceuil/acceuil.html')

def aboutus(request):
    return render(request, 'acceuil/about-us.html')