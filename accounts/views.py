from django.shortcuts import render, redirect
from accounts.forms import LoginForm
from django.contrib.auth import login, authenticate

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("home")

    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


# def user_logout(request):
#     logout(request)
#     return redirect("login")


# def sign_up(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             password_confirmation = form.cleaned_data["password_confirmation"]

#             if password == password_confirmation:
#                 # create a new user with those values
#                 user = User.objects.create_user(
#                     username,
#                     password=password,
#                 )
#                 # login the user
#                 login(request, user)

#                 return redirect("home")

#             else:
#                 # add an error message for the person trying to sign up that
#                 # tells them their passwords don't match if they type them in wrong
#                 form.add_error("password", "passwords do not match")

#     else:
#         # aka GET
#         form = SignUpForm()
#     context = {
#         "form": form,
#     }
#     return render(request, "accounts/signup.html", context)
