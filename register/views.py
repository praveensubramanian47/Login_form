from django.shortcuts import render, HttpResponse
from register.models import register


def sign_up (request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['pass']
        user = register(name=name, password=password)
        user.save()
        return HttpResponse("<h1><center>Signin successfully</center></h1>")
    else:
        return render(request, "register/signup.html")
    

def log_in (request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['pass']
        users = list(register.objects.all().values())
        for get in users:
            if get['name'] == name and get['password'] == password:
                return HttpResponse("<h1><center>Login Sucessfully</center></h1>")
              
        return HttpResponse("<h1><center>OOPS You Typed Wrong Username or Password</center></h1>")
    
    else:
        return render(request, 'register/login.html')
