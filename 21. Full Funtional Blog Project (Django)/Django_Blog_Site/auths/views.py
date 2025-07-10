from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# calling the user model functions
User = get_user_model()


# creating new userCreating form object (because we have modified the User model ---> AbstractUser)
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


# Create your views here.


# register and login automatically in any application
def register_view(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = MyUserCreationForm()

    context = {"form": form}
    return render(request, "auths/register.html", context)
