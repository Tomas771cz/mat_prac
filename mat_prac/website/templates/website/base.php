<!DOCTYPE html>
<html lang="cs">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Název stránky{% endblock %}</title>
    {% for item in webelement.all %}
    <link rel="icon" href="{{item.comp_logo.url}}">
    {% endfor %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.bundle.min.js" integrity="sha384-qKXV1j0HvMUeCBQ+QVp7JcfGl760yU08IQ+GpUo5hlbpg51QRiuqHAJz8+BrxE/N" crossorigin="anonymous"></script>
</head>

<body>
    <div class="bg-black text-white">
    {% for item in webelement.all %}
    <img style='height: 100%; width: 100%; object-fit: contain' src="{{item.banner.url}}">
    {% endfor %}
        <nav class="navbar navbar-expand-lg">
            <div class="container-fluid bg-warning">
                <a class="navbar-brand" href="/">{% for item in webelement.all %}<img style='height: 20px; width: 20px; object-fit: contain' src="{{item.comp_logo.url}}">{{item.comp_name}} {% endfor %}</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="/group/Group 1" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Group 1
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="/group/1">Příspěvky</a></li>
                                <li>
                                    <hr class="dropdown-divider">
                                </li>
                                <li><a class="dropdown-item" href="#">Something else here</a></li>
                            </ul>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="/group/Group 2" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Groupe 2
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="/group/2">Příspěvky</a></li>
                                <li>
                                    <hr class="dropdown-divider">
                                </li>
                                <li><a class="dropdown-item" href="#">Something else here</a></li>
                            </ul>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/contacts">Kontakty</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/aboutus">O nás</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container">
            {% block content%}
            {% endblock %}
        </div>
        <footer class="page-footer bg-warning text-black">
            <div class="container">
                <div class="row">
                    <h4>Odkazy</h4>
                    <ul>
                        {% for item in social.all %}
                            <li><a class="nav-link" href="{{item.link}}"><img src="{{item.icon_link}}" width="20" height="20">{{item.text}}</a></li>
                        {% endfor %}
                        <li><a class="nav-link" href="/admin">Pouze pro editory a administrátory</a></li>
                        <li><a class="nav-link" href="/website/signup">Vytvoření účtu</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-copyright">
                <div class="container">Tomáš Janeček © 2023</div>
            </div>
        </footer>
    </div>
</body>

</html>