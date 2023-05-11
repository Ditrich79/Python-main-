from jinja2 import Template


# Задание №1

headlines = [
    {'caption': 'index', 'name': 'Главная'},
    {'caption': 'news', 'name': 'Новости'},
    {'caption': 'about', 'name': 'О компании'},
    {'caption': 'shop', 'name': 'Магазин'},
    {'caption': 'contacts', 'name': 'Контакты'}
]

link = """<ul>
{%- for h in headlines -%}
{%- if h.name == 'Главная' %}
<li><a href="/{{ h['caption'] }}" class="active">{{ h['name'] }}</a></li>
{% else -%}
<li><a href="/{{ h['caption'] }}">{{ h['name'] }}</a></li>
{% endif -%}
{% endfor -%}
</ul>"""

temp = Template(link)
tags = temp.render(headlines=headlines)

print(tags)


# Задание №2

html = """
{% macro text_input(type='text', name='', placeholder='') -%}
    <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}" >
{%- endmacro %}

<p>{{ text_input(name='firstname', placeholder='Имя') }}</p>
<p>{{ text_input(name='lastname', placeholder='Фамилия') }}</p>
<p>{{ text_input(name='address', placeholder='Адрес') }}</p>
<p>{{ text_input(type='tel', name='phone', placeholder='Телефон') }}</p>
<p>{{ text_input(type='email', name='email', placeholder='Почта') }}</p>
"""

temp = Template(html)
out = temp.render()

print(out)
