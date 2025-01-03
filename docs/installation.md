(installation)=

# Installation

The package is published on [PyPI](https://pypi.org/project/django-htmx-messages/) and can be installed with `pip` (or any equivalent):

```bash
pip install django-htmx-messages
```

Add to your Django settings:

```python
INSTALLED_APPS = [
    # ...
    "django_htmx_messages",
]

MIDDLEWARE = [
    # ...
    "django_htmx_messages.middleware.HtmxMessageMiddleware",
]
```

Add to your base template:

```html
<head>
  <script src="{% static 'htmx.min.js' %}" defer></script>
  <script src="{% static 'toasts.js' %}" defer></script>
</head>
<body>
  {# Your content here #} {% include 'toasts.html' %}
</body>
```

Next, see the {ref}`section about usage <usage>` to see how to use it.
