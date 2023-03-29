{% extends 'website/base.php' %}

{% block title%}Kontakty{% endblock %}

{% block content%} 
    <h1>Dopravní spojení</h1>
    <ul>
        <li>Tramvaj</li>
        <ul>
            <li><b>Zastávky</b>: Sparta, Letenské Náměstí</li>
            <li><b>Linky</b>: 1, 8, 12, 25, 26</li>
            <li>5 minut chůze</li>
            <li>Mimořádne události v dopravě můžete vidět <a href="https://www.dpp.cz/omezeni-a-mimoradne-udalosti?fulltext=1%2C+8%2C+12%2C+25%2C+26" class="text-warning">zde</a></li>
        </ul>
    </ul>

    <h1>Mapa</h1>
    {% for item in webelement.all %}
    <iframe src="{{item.map}}" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    {% endfor %}

        <h1>Kontakty</h1>
    {% for item in contacts.all %}
        <h3>{{item.person}}</h3>
        <p>Telefoní číslo: {{item.phone}}</p>
        <p>E-mail: {{item.email}}</p>
        <p>Adresa: {{item.address}}</p>
    {% endfor %}

{% endblock %}