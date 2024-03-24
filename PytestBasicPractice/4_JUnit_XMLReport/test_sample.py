'''
Create junit-xml style report file at given path
- pytest --junit-xml="path"
Prepend prefix to classnames in junit-xml output
- pytest --junit-prefix=str
'''

def test_sample_one():
    a = 5
    b = 5
    assert a == b , "a is equal to b"

def test_sample_two():
    a = 7
    b = 3
    assert a > b , "a is greater than b"

def test_sample_three():
    a = "Arun"
    b = "Das"
    assert a.__eq__(b), "a is not equal to b"