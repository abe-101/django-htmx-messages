# ruff: noqa: S311

import random

from django.contrib import messages
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


SAMPLE_MESSAGES = [
    (messages.DEBUG, "Hello World!"),
    (messages.INFO, "System operational"),
    (messages.SUCCESS, "Congratulations! You did it."),
    (messages.WARNING, "Hum... not sure about that."),
    (messages.ERROR, "Oops! Something went wrong"),
]


def message(request):
    messages.add_message(request, *random.choice(SAMPLE_MESSAGES))
    return render(request, "lorem.html")
