{% extends 'website/base.php' %}

{% block title%}Soupiska{% endblock %}

{% block content %}

   


</table>

<table class="table table-striped text-white">
    <thead class="text-white">
        <tr>
            <th scope="col">Jméno</th>
            <th scope="col">Datum narození</th>
            <th scope="col">Foto</th>
        </tr>
    </thead>
    <tbody class="text-white">
    {% for item in soupiska.all %}
        {% if item.group == group %}
        <tr>
            <td class="text-white">{{item.name}}</td>
            <td class="text-white">{{item.birthday}}</td>
            <td class="text-white"><img style='height: 50%; width: 50%; object-fit: contain' src="{{item.photo.url}}"></td>
        </tr>
        {% endif %}
    {% endfor %}
    </tbody>
</table>

{% endblock %}
