from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

# pomocí těchto odkazů se člověk pohybuje na stránkách

app_name = "website"
urlpatterns = [
    path("", views.IndexView, name="index"),
    path("contacts", views.ContactView, name="contacts"),
    path("group/<str:group>", views.GroupView, name="group"),
    path("group/<str:group>/soupiska", views.SoupiskaView, name="soupiska"),
    path("aboutus", views.AboutUsView, name="aboutus"),
    path("signup", views.SignUpView, name="signup"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
