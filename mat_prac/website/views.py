from django.shortcuts import render
from .models import Post, Contact, Social, WebElement, Soupiska
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

social = Social.objects
webelement = WebElement.objects
post = Post.objects.order_by("-pub_date")


def IndexView(response):
    return render(
        response,
        "website/index.php",
        {"post": post, "social": social, "webelement": webelement},
    )


def ContactView(response):
    contacts = Contact.objects
    return render(
        response,
        "website/contacts.php",
        {"contacts": contacts, "social": social, "webelement": webelement},
    )


def GroupView(response, group):
    return render(
        response,
        "website/group.php",
        {"group": group, "post": post, "social": social, "webelement": webelement},
    )


def AboutUsView(response):
    return render(
        response,
        "website/about.php",
        {"social": social, "webelement": webelement},
    )


def SoupiskaView(response, group):
    soupiska = Soupiska.objects
    return render(
        response,
        "website/soupiska.php",
        {
            "group": group,
            "soupiska": soupiska,
            "social": social,
            "webelement": webelement,
        },
    )


def SignUpView(response):
    if response.method == "POST":
        form = NewUserForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
            messages.success(response, "Registration successful.")
            return render(
                response,
                "website/index.php",
                {"post": post, "social": social, "webelement": webelement},
            )
        messages.error(response, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        response,
        "website/signup.php",
        {"register_form": form, "social": social, "webelement": webelement},
    )
