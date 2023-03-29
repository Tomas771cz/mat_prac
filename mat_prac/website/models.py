from django.db import models


class Post(models.Model):
    post_headline = models.CharField(max_length=50)
    post_text = models.TextField(max_length=5000)
    pub_date = models.DateTimeField("datum zveřejnění")
    img = models.ImageField(null=True, blank=True, upload_to="static/")
    group = models.CharField(max_length=20)


class Contact(models.Model):
    phone = models.CharField(null=True, blank=True, max_length=30)
    email = models.CharField(max_length=50)
    address = models.CharField(null=True, blank=True, max_length=500)
    person = models.CharField(max_length=500)


class Social(models.Model):
    link = models.CharField(max_length=500)
    icon_link = models.CharField(null=True, blank=True, max_length=2000)
    text = models.CharField(max_length=50)


class WebElement(models.Model):
    comp_name = models.CharField(max_length=10)
    comp_logo = models.ImageField(null=True, blank=True, upload_to="static/")
    banner = models.ImageField(upload_to="static/")
    map = models.CharField(max_length=2000)


class Soupiska(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField("Datum narození")
    photo = models.ImageField(upload_to="static/")
    group = models.CharField(max_length=20)
