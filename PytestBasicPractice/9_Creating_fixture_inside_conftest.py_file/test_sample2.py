'''
In Pytest,
- pytest.fixture() by using this, it will mean before run any test, the fixture portion is run first
- marker is: @pytest.fixture()
'''


def test_with_mandatory_fields(test_setup_and_teardown):
    print("Testing test_with_mandatory_fields")
def test_with_all_fields(test_setup_and_teardown):
    print("Testing test_with_all_fields")