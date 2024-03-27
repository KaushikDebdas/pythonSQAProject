'''
In Pytest,
- if we have multiple file in a folder and then we need to run same test again and again, then we need fixture
- the fixture format can store in a separate file called conftest.py
- this file use centrally
- if we use autouse=True inside the pytest.fixture() then it will automatic set attribute in every other file
'''
import pytest


@pytest.fixture(autouse=True)
def test_setup_and_teardown():
    print("Launch Browser")
    print("Open Application")
    yield
    print("Logout")
    print("Close the Browser")