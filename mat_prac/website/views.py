from django.shortcuts import render

from .models import Post, Contact, Social, WebElement

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
