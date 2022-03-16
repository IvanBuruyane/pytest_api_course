from unittest.mock import patch

from django.core import mail
import json


def test_send_email_should_succed(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    assert len(mailoutbox) == 0
    # Send messsage:
    mail.send_mail(
        subject="Test Subject here",
        message="Test here is the message",
        from_email="pytestcourse0@gmail.com",
        recipient_list=["iburuyane@gmail.com"],
        fail_silently=False,
    )

    assert len(mailoutbox) == 1
    assert mailoutbox[0].subject == "Test Subject here"


def test_send_email_without_arguments_should_send_empty_email(client) -> None:
    with patch(
        "api.coronavstech.companies.views.send_mail"
    ) as mocked_send_email_function:
        response = client.post(path="/send-email")
        response_content = json.loads(response.content)
        assert response.status_code == 200
        assert response_content["status"] == "success"
        assert response_content["info"] == "email sent successfully"
        mocked_send_email_function.assert_called_with(
            subject=None,
            message=None,
            from_email="pytestcourse0@gmail.com",
            recipient_list=["iburuyane@gmail.com"],
        )


def test_send_email_with_get_verb_should_fail(client):
    response = client.get(path="/send-email")
    response_content = json.loads(response.content)
    assert response.status_code == 405
    assert response_content["detail"] == 'Method "GET" not allowed.'
