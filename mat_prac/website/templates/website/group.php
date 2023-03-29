{% extends 'website/base.php' %}

{% block title%}Group 1{% endblock %}

{% block content %}
<h2>Nejnovější příspěvky</h2>
        {% for item in post.all %}
            {% if item.group == group %}
                <h4>{{item.post_headline}}</h4>
                <p>{{item.pub_date}}</p>
                {% if item.img %} <img style='height: 100%; width: 100%; object-fit: contain' src="{{item.img.url}}" max-width="500"> {% endif %}
                <p>{{item.post_text}}</p>
            {% endif %}
        {% endfor %}
{% endblock %}