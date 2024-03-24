'''
to find flags, pytest --help
# pytest -v [It will got all information got run, output is not coming here]
# pytest -rA [not only passed test also show information about failed test]
# pytest -k [if i want to run only one test_sample then we need to run this.
            suppose test_sample_two needs to be run, then use pytest -rA -k test_sample_two.]
            [if i want to run only two test then, use
            pytest -rA -k "one or three"]
'''

def test_sample_one():
    print("Inside sample one")

def test_sample_two():
    print("Inside sample two")

def test_sample_three():
    print("Inside sample three")