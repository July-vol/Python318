from jinja2 import Template

html = """
{% macro input_func(name, placeholder, type="text") -%}
    <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
{% end macro %}

<p>{{ input_func('firstname', 'Имя') }}</p>
<p>{{ input_func('lastname', 'Фамилия') }}</p>
<p>{{ input_func('address', 'Адрес') }}</p>
<p>{{ input_func('phone', 'Телефон','tel' ) }}</p>
<p>{{ input_func('email', 'Почта', 'email') }}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)
