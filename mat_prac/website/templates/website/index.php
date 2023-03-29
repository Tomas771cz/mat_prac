{% extends 'website/base.php' %}

{% block title%}Domovská stránka{% endblock %}

{% block content %}
    <h2>Nejnovější příspěvky</h2>
        {% for item in post.all %}
            <h4>{{item.post_headline}}</h4>
            <a class="nav-link" href="/group/{{item.group}}">{{item.group}}</a>
            <p>{{item.pub_date}}</p>
            {% if item.img %} 
                <img style='height: 50%; width: 50%; object-fit: contain' src="{{item.img.url}}" max-width="500"> 
            {% endif %}
            <p>{{item.post_text}}</p>

        {% endfor %}


{% endblock %}
