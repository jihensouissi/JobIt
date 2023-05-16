

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
# Function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.is_superuser

# View that requires admin login
@login_required
@user_passes_test(is_admin)
def PeHome(request):
    return render(request, 'PE/PEHome.html')
@login_required
@user_passes_test(is_admin)
def dashboard(request):
    return render(request, 'PE/dashboard.html')
@login_required
@user_passes_test(is_admin)
def termsofuse(request):
    return render(request, 'PE/terms-of-use.html')



