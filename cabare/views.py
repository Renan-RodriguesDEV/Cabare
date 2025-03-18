from django.http import HttpRequest
from django.shortcuts import redirect, render

from middlewares.auth import check_passwd
from .models import Images, Post, Usuarios, Videos


def index(request: HttpRequest):
    return render(request, "home/home.html", {"user": "Renan"})


def contact(request: HttpRequest):
    return render(request, "contact/contact.html", {"user": "Renan"})


def accounts(request: HttpRequest):
    user = Usuarios.objects.first()
    return render(request, "accounts/accounts.html", {"user": user})


def galery(request: HttpRequest):
    images = Images.objects.all()
    return render(request, "galery/galery.html", {"images": images})


def videos(request: HttpRequest):
    videos = Videos.objects.all()
    return render(request, "videos/videos.html", {"videos": videos})


def meetings(request: HttpRequest):
    meetings = Post.objects.first()
    return render(request, "meetings/meetings.html", {"meetings": meetings})


def login(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = Usuarios.objects.get(username=username)
            if user:
                if check_passwd(password, user.password):
                    # User found, you could set a session variable to keep the user logged in
                    print("Passou")
                    request.session["user_id"] = user.id
                    request.session["username"] = user.username
                    # Redirect to home or dashboard after successful login
                    return redirect("index")
        except Exception as e:
            print(f"Error: {e}")
    return render(request, "login/login.html")
