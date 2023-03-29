from django.contrib import admin


from .models import Post, Contact, Social, WebElement, Soupiska


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Nadpis", {"fields": ["post_headline"]}),
        ("Text", {"fields": ["post_text"]}),
        ("Obrázky", {"fields": ["img"]}),
        ("Skupina", {"fields": ["group"]}),
        ("Datum", {"fields": ["pub_date"]}),
    ]
    list_display = ("post_headline", "group", "pub_date")
    list_filter = ["pub_date"]
    search_fields = ["post_headline"]


class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Jméno", {"fields": ["person"]}),
        ("Telefoní číslo", {"fields": ["phone"]}),
        ("E-mail", {"fields": ["email"]}),
        ("Adresa", {"fields": ["address"]}),
    ]
    list_display = ("person", "phone", "email")
    search_fields = ["person", "phone", "email"]


class SocialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Odkaz", {"fields": ["link"]}),
        ("Odkaz na ikonku", {"fields": ["icon_link"]}),
        ("Text zobrazený vedle ikonky", {"fields": ["text"]}),
    ]
    list_display = ("link",)
    search_fields = ["link"]


class WebElementAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Název uskupení", {"fields": ["comp_name"]}),
        ("Logo společnosti", {"fields": ["comp_logo"]}),
        ("Banner (pouze obrázky 1:4)", {"fields": ["banner"]}),
        ("Mapa", {"fields": ["map"]}),
    ]
    list_display = ("comp_name",)


class SoupiskaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Jméno", {"fields": ["name"]}),
        ("Datum narození", {"fields": ["birthday"]}),
        ("Fotka", {"fields": ["photo"]}),
        ("Skupina", {"fields": ["group"]})
    ]
    list_display = ("name", "birthday", "group")


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(WebElement, WebElementAdmin)
admin.site.register(Soupiska, SoupiskaAdmin)
