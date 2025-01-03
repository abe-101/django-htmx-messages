# Django Htmx Messages

<p align="center">
  <a href="https://github.com/abe-101/django-htmx-messages/actions/workflows/ci.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/abe-101/django-htmx-messages/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://django-htmx-messages.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/django-htmx-messages.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/abe-101/django-htmx-messages">
    <img src="https://img.shields.io/codecov/c/github/abe-101/django-htmx-messages.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
</p>
<p align="center">
  <a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/django-htmx-messages/">
    <img src="https://img.shields.io/pypi/v/django-htmx-messages.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/django-htmx-messages.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">
  <img src="https://img.shields.io/pypi/l/django-htmx-messages.svg?style=flat-square" alt="License">
</p>

---

**Documentation**: <a href="https://django-htmx-messages.readthedocs.io" target="_blank">https://django-htmx-messages.readthedocs.io </a>

**Source Code**: <a href="https://github.com/abe-101/django-htmx-messages" target="_blank">https://github.com/abe-101/django-htmx-messages </a>

---

Django+HTMX integration with the messages framework

A PyPI package for [Benoit Blanchon's django-htmx-messages-framework](https://github.com/bblanchon/django-htmx-messages-framework/blob/oob) (used with permission). It integrates Django's messages framework with HTMX for dynamic toast notifications.

<p align="center">
  <img src="https://raw.githubusercontent.com/bblanchon/django-htmx-messages-framework/main/django-htmx-messages-framework.gif" alt="Demo">
</p>

## Installation

Install this via pip (or your favourite package manager):

`pip install django-htmx-messages`

Add the app to your `INSTALLED_APPS`:

````python
```python
INSTALLED_APPS = [
    "django_htmx_messages",
]

MIDDLEWARE = [
    "django_htmx_messages.middleware.HtmxMessageMiddleware",
]
````

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

## Try the Demo

```bash
git clone https://github.com/abe-101/django-htmx-messages.git
cd django-htmx-messages
uv sync
uv run manage.py runserver
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- prettier-ignore-start -->
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.habet.dev/"><img src="https://avatars.githubusercontent.com/u/82916197?v=4?s=80" width="80px;" alt="Abe Hanoka"/><br /><sub><b>Abe Hanoka</b></sub></a><br /><a href="https://github.com/abe-101/django-htmx-messages/commits?author=abe-101" title="Code">💻</a> <a href="#ideas-abe-101" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/abe-101/django-htmx-messages/commits?author=abe-101" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-end -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

- Original implementation by [Benoit Blanchon](https://github.com/bblanchon/django-htmx-messages-framework/blob/oob)
  This package was created with
  [Copier](https://copier.readthedocs.io/) and the
  [browniebroke/pypackage-template](https://github.com/browniebroke/pypackage-template)
  project template.
