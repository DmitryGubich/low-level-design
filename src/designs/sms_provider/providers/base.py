import abc
from functools import wraps

from designs.sms_provider import settings


class BaseSmsProvider(metaclass=abc.ABCMeta):
    """Base SMS Provider class"""

    recipient, content = None, None
    SENDER_NAME = "Alice"
    COUNTRY_CODES = settings.COUNTRY_CODES

    # pylint: disable=no-self-argument
    def _validation(func):
        """Validation decorator"""

        @wraps(func)
        def wrapped(obj, *args, **kwargs):
            # pylint: disable=no-member, not-callable
            getattr(obj, "_validate_" + func.__name__)(*args)
            return func(obj, *args, **kwargs)

        return wrapped

    @abc.abstractmethod
    def send(self):
        """Abstract sending method"""
        pass

    @abc.abstractmethod
    def _process_response(self, resp):
        """Protected abstract method responsible for response processing"""
        pass

    @abc.abstractmethod
    def _prepare_payload(self):
        """Protected abstract method responsible for creating payload"""
        pass

    @_validation
    def set_content(self, content):
        """Set content and make the method chainable"""
        self.content = content
        return self

    @_validation
    def set_recipient(self, phone_number, country_code="PL"):
        """Set recipient attribute - remember to add a country code like in the `old.py` file.
        Make the method chainable"""
        self.recipient = settings.COUNTRY_CODES[country_code] + phone_number
        return self
