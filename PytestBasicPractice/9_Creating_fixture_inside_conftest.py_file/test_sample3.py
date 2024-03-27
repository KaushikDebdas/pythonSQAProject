'''
In Pytest,
- pytest.fixture() by using this, it will mean before run any test, the fixture portion is run first
- marker is: @pytest.fixture()
'''


def test_search_with_valid_input(test_setup_and_teardown):
    print("Testing test_search_with_valid_input")
def test_search_with_invalid_input(test_setup_and_teardown):
    print("Testing test_search_with_invalid_input")