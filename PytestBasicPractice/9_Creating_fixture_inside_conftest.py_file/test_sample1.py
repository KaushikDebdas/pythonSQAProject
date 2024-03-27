'''
In Pytest,
- if we have multiple file in a folder and then we need to run same test again and again, then we need fixture
- the fixture format can store in a separate file called conftest.py
- this file use centrally
'''


def test_login_with_valid_credentials(test_setup_and_teardown):
    print("Testing test_login_with_valid_credentials")
def test_login_with_valid_email_and_invalid_password(test_setup_and_teardown):
    print("Testing test_login_with_valid_email_and_invalid_password")
def test_login_with_invalid_email_and_valid_password(test_setup_and_teardown):
    print("Testing test_login_with_invalid_email_and_valid_password")