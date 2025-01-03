from django.contrib.messages import constants as message_constants
from django.contrib.messages.storage.base import Message
from django.http import HttpResponse
from django.test import RequestFactory, TestCase

from django_htmx_messages.middleware import HtmxMessageMiddleware


class TestHtmxMessageMiddleware(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        def get_response(request):
            return HttpResponse()

        self.middleware = HtmxMessageMiddleware(get_response=get_response)

    def test_non_htmx_request_returns_unmodified(self):
        """Test that non-HTMX requests are returned unmodified."""
        request = self.factory.get("/")
        response = HttpResponse("Test response")

        processed_response = self.middleware.process_response(request, response)

        self.assertEqual(processed_response.content, b"Test response")

    def test_redirect_response_returns_unmodified(self):
        """Test that redirect responses are returned unmodified."""
        request = self.factory.get("/", HTTP_HX_REQUEST="true")
        response = HttpResponse(status=302)

        processed_response = self.middleware.process_response(request, response)

        self.assertEqual(processed_response.status_code, 302)
        self.assertEqual(processed_response.content, b"")

    def test_htmx_redirect_header_returns_unmodified(self):
        """Test that responses with HX-Redirect header are returned unmodified."""
        request = self.factory.get("/", HTTP_HX_REQUEST="true")
        response = HttpResponse()
        response.headers["HX-Redirect"] = "/new-location/"

        processed_response = self.middleware.process_response(request, response)

        self.assertEqual(processed_response.content, b"")

    def test_htmx_request_without_messages_returns_unmodified(self):
        """Test that HTMX requests without messages are returned unmodified."""
        request = self.factory.get("/", HTTP_HX_REQUEST="true")
        response = HttpResponse("Test response")

        processed_response = self.middleware.process_response(request, response)

        self.assertEqual(processed_response.content, b"Test response")

    def test_htmx_request_with_messages_adds_toast(self):
        """Test that HTMX requests with messages have toast content appended."""
        request = self.factory.get("/", HTTP_HX_REQUEST="true")
        request._messages = []
        request._messages.append(
            Message(level=message_constants.SUCCESS, message="Test message")
        )
        response = HttpResponse("<div>Original content</div>")

        processed_response = self.middleware.process_response(request, response)

        # Check that original content is preserved
        self.assertIn(b"<div>Original content</div>", processed_response.content)
        # Check that toast container is added with correct classes
        self.assertIn(
            b'class="toast-container position-fixed top-0 end-0 p-3"',
            processed_response.content,
        )
        # Check that message is included
        self.assertIn(b"Test message", processed_response.content)

    def test_multiple_messages_all_included(self):
        """Test that multiple messages are all included in the response."""
        request = self.factory.get("/", HTTP_HX_REQUEST="true")
        request._messages = []
        messages = [
            Message(level=message_constants.SUCCESS, message="Success message"),
            Message(level=message_constants.ERROR, message="Error message"),
            Message(level=message_constants.INFO, message="Info message"),
        ]
        for msg in messages:
            request._messages.append(msg)
        response = HttpResponse()

        processed_response = self.middleware.process_response(request, response)

        for msg in messages:
            self.assertIn(msg.message.encode(), processed_response.content)

    def test_message_levels_included_as_classes(self):
        """Test that message levels are included as CSS classes."""
        request = self.factory.get("/", HTTP_HX_REQUEST="true")
        request._messages = []
        request._messages.append(
            Message(level=message_constants.SUCCESS, message="Success message")
        )
        response = HttpResponse()

        processed_response = self.middleware.process_response(request, response)

        # Check for the Bootstrap-styled success class
        self.assertIn(
            b'class="toast align-items-center border-0 text-white bg-success"',
            processed_response.content,
        )

    def test_middleware_chain(self):
        """Test that the middleware properly chains the get_response call."""
        request = self.factory.get("/")
        response = self.middleware(request)
        self.assertIsInstance(response, HttpResponse)
