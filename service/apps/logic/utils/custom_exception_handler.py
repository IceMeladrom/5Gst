import logging
import traceback

from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    handlers = {
        'BadRequest': _handler_badrequest_error,
    }

    response = exception_handler(exc, context)

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        logger.exception(traceback.format_exc())
        return handlers[exception_class](exc, context, response)
    return response


def _handler_badrequest_error(exc, context, response):
    response.data = {
        'status_code': response.status_code,
        'status_text': response.status_text,
    }
