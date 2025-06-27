from designs.sms_provider import settings, errors
from designs.sms_provider.fake import fake_secondary_external_api
from designs.sms_provider.providers.base import BaseSmsProvider


class SecondarySmsApiProvider(BaseSmsProvider):
    """
    Secondary SMS API Provide
    Write this class from scratch based on `primary.py` and `old.py` files
    """

    API_KEY = settings.SECONDARY_API_KEY

    def _validate_set_recipient(self, *args):
        """Validate recipient using the same logic as defined in `old.py` file.
        Throw appropriate exception or return a boolean"""
        phone = args[0] if len(args) > 0 else None
        country_code = args[1] if len(args) > 1 else None
        if country_code and country_code not in settings.COUNTRY_CODES.keys():
            raise errors.InvalidCountryException("Invalid country code")
        if not phone.isdigit():
            raise errors.InvalidPhoneNumber("Invalid phone number")

    def _validate_set_content(self, *args):
        """Validate content.
        Throw appropriate exception or return a boolean"""
        content = args[0] if len(args) > 0 else None
        if len(content) > 160:
            raise errors.InvalidContentLength("Invalid content length")

    def _validate_before_sending(self):
        """Check if content and recipient are set.
        Throw appropriate exception from `app.errors` module"""
        if not self.recipient:
            raise errors.RecipientNotSet
        if not self.content:
            raise errors.ContentNotSet

    def _process_response(self, resp):
        """Check response content.
        Return (boolean, resp)"""
        return resp.get("status") == "OK", resp

    def _prepare_payload(self):
        """Construct and return payload - check `old.py` for the implementation details"""
        return {
            "body": self.content,
            "recipient": self.recipient,
            "sender_name": "Alice",
            "auth_key": self.API_KEY,
        }

    def send(self):
        """Send the message"""
        self._validate_before_sending()
        payload = self._prepare_payload()
        response = fake_secondary_external_api(payload)
        return self._process_response(response)
