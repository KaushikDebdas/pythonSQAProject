'''
- first need to import pytes
- use @pytest.mark.TESTNAME
- pytest -rA -m regression [If i run this, it will run only regression marking tests]
- pytest -rA -m "smoke or regression" [It will run both smoke and regression tests]
- if we want to skip the test. we can use
    - pytest -rA -m test_sample_Skipmarkers
'''
import pytest

@pytest.mark.smoke
def test_sample_one():
    a = 5
    b = 5
    assert a == b , "a is equal to b"
@pytest.mark.skip
def test_sample_two():
    a = 7
    b = 3
    assert a > b , "a is greater than b"
@pytest.mark.regression
def test_sample_three():
    a = "Arun"
    b = "Das"
    assert a.__eq__(b), "a is not equal to b"