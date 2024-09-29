from jinja2 import Template

pages = [
    {'title': "Главная", 'url_name': '/index'},
    {'title': "Новости", 'url_name': '/news'},
    {'title': "О компании", 'url_name': '/about'},
    {'title': "Магазин", 'url_name': '/shop'},
    {'title': "Контакты", 'url_name': '/contacts'},
]

link = """"<ul name="pages">
{% for p in pages -%}
{%if p.'title' == "Главная"-%}
<li><a href="{{ p['url_name']}}">{{ p['title']}}</a></li>
{% else -%}
<li><a href="{{ p['url_name']}}"class="active">{{ p['title']}}</a></li>
{% endif -%}
{% endfor -%}
"""

tm = Template(link)
msg = tm.render(pages=pages)
print(msg)
