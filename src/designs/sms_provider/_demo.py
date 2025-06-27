from designs.sms_provider.providers import sms_factory

CORRECT_CONTENT = "content"
CORRECT_PHONE = "123456789"

if __name__ == "__main__":
    provider = sms_factory("primary")
    status, response = provider.set_recipient(CORRECT_PHONE).set_content(CORRECT_CONTENT).send()
    assert status
    assert response == {"recipient": "0048123456789", "status": "SENT", "api": "1"}

    ###############################################################

    provider = sms_factory("secondary")
    status, response = provider.set_recipient(CORRECT_PHONE).set_content(CORRECT_CONTENT).send()
    assert status
    assert response.get("status") == "OK"
    assert response.get("api") == "2"
