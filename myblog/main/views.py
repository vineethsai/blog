from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import hashlib
from django.contrib.auth.models import User


def home(request):
    """
    routes to home page on GET request
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, "main/index.html", status=200)
    else:
        return HttpResponse("Method not allowed on /.", status=405)


def specificUser(request, user_id):
    """
    Displays a single user's information and their picture on GET request
    :param request: request object
    :param user_id: user_id provided by parent call
    :return:
    """
    if request.method == "GET":
        if request.user.is_authenticated:
            user = User.objects.get(pk=user_id)
            email = user.email.lower().encode()
            gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email).hexdigest()
            return render(request, 'main/specificUser.html', {"user": user, "url": gravatar_url})
        else:
            return HttpResponseRedirect("/auth/signin")
    else:
        return HttpResponse("Method not allowed on main/users/.", status=405)
