(usage)=

# Usage

Assuming that you've followed the {ref}`installation steps <installation>`, you're now ready to use Django HTMX Messages.

## Basic Setup

### Using Django Messages

Use Django's messages framework as normal:

```python
from django.contrib import messages

def my_view(request):
    messages.success(request, "This will show as a toast!")
    messages.error(request, "Error messages work too!")
    return HttpResponse()
```

## HTMX Integration

The middleware automatically handles HTMX requests. When using HTMX to make requests:

```html
<button hx-post="/save/" hx-target="#result">Save</button>
```

Any messages added in the view will appear as toasts automatically.

## Message Types

All Django message levels are supported with appropriate styling:

```python
messages.debug(request, "Debug message")
messages.info(request, "Info message")
messages.success(request, "Success message")
messages.warning(request, "Warning message")
messages.error(request, "Error message")
```

## Customization

To customize the toast appearance, create your own templates:

1. Create `templates/toasts.html` in your project to override the default Bootstrap styling
2. Create `static/toasts.js` to modify the toast behavior

For reference, see the default templates in the package source.

## Example Views

Here's a complete example:

```python
from django.contrib import messages
from django.http import HttpResponse

def save_item(request):
    try:
        # Your save logic here
        messages.success(request, "Item saved successfully!")
    except Exception:
        messages.error(request, "Failed to save item")

    return HttpResponse()  # Empty response for HTMX
```
