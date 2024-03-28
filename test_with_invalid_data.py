import pytest
from authorization_page import AUTH_PAGE



def test_name_field_are_empty():
    name = " "
    response_message = AUTH_PAGE.get_username_error_message(name)
    assert response_message == "Заполните это поле"


@pytest.mark.parametrize(
    'version_email',
    [
        pytest.param(('email'), id="only string"),
        pytest.param(('12344'), id="only intiger"),
        pytest.param(('#$%%^'), id="only simbols"),
        pytest.param((' '), id="empty field")
    ]
)
def test_email_field(version_email):
    email = version_email
    response_message = AUTH_PAGE.get_email_error_message(email)
    assert response_message == "Неверный формат" or "Заполните это поле"


@pytest.mark.parametrize(
    'version_phone_number',
    [
        pytest.param(('123'), id="not enough numbers"),
        pytest.param(('qwer'), id="srtings"),
        pytest.param(('#$%%^'), id="simbols"),
        pytest.param((' '), id="empty field")
    ]
)
def test_phone_number_field(version_phone_number):
    phone_number = version_phone_number
    response_message = AUTH_PAGE.get_phone_number_error_message(phone_number)
    assert response_message == "Неверный формат" or "Заполните это поле"



@pytest.mark.parametrize(
    'version_password',
    [
        pytest.param(('qwert'), id="<6"),
        pytest.param(('1'), id="1"),
        pytest.param((' '), id="empty field")
    ]
)
def test_password_field(version_password):
    password = version_password
    response_message = AUTH_PAGE.get_password_error_message(password)
    assert response_message == "Минимум 6 символов" or "Заполните это поле"


@pytest.mark.parametrize(
    'version_repeat_password',
    [
        pytest.param(('qwert'), id="<6"),
        pytest.param(('1'), id="1"),
        pytest.param((' '), id="empty field")
    ]
)

def test_repeat_password_field(version_repeat_password):
    repeat_password = version_repeat_password
    response_message = AUTH_PAGE.get_repeat_password_error_message(repeat_password)
    assert response_message == "Пароли не совпадают" or "Заполните это поле"