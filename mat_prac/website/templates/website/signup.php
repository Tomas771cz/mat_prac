{% extends 'website/base.php' %}

{% block title%}Registrace{% endblock %}

{% block content %}
<div class="container py-5">
	<h1>Registrace</h1>
	<form method="POST">
		{% csrf_token %}
		<p>Uživatelské jméno</p>{{ register_form.username }}
        <p>E-mail</p>{{ register_form.email }}
        <p>Heslo</p>{{ register_form.password1 }}
        <p>Heslo znovu</p>{{ register_form.password2 }}
		<button class="btn btn-primary" type="submit">Registrovat</button>
	</form>
</div>

{% endblock %}