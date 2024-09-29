from jinja2 import Template

html = """
{% macro input_func(name, placeholder, type="text") -%}
    <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
{% end macro %}

<p>{{ input_func('firstname', '���') }}</p>
<p>{{ input_func('lastname', '�������') }}</p>
<p>{{ input_func('address', '�����') }}</p>
<p>{{ input_func('phone', '�������','tel' ) }}</p>
<p>{{ input_func('email', '�����', 'email') }}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)
