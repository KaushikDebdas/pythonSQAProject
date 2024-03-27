'''
In Pytest,
- if we have multiple file in a folder and then we need to run same test again and again, then we need fixture
- the fixture format can store in a separate file called conftest.py
- this file use centrally
- if we use autouse=True inside the pytest.fixture() then it will automatic set attribute in every other file
'''

def test_with_mandatory_fields():
    print("Testing test_with_mandatory_fields")
def test_with_all_fields():
    print("Testing test_with_all_fields")