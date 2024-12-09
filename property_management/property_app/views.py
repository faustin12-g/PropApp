from django.shortcuts import render
from .models import Property, Tenant

def properties(request):
    properties = Property.objects.all()
    context= {"properties": properties}
    return render(request, "property.html", context)

def tenants(request):
    tenants = Tenant.objects.all()
    context = {"tenants": tenants}
    return render(request, 'tenants.html', context)

def login_view(request):
    if request.method=="POST":
        
