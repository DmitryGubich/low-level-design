from designs.sms_provider.providers.primary import PrimarySmsApiProvider
from designs.sms_provider.providers.secondary import SecondarySmsApiProvider


def sms_factory(api):
    if api == "primary":
        return PrimarySmsApiProvider()
    elif api == "secondary":
        return SecondarySmsApiProvider()
    else:
        raise NotImplementedError()
