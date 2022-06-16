# install pytest to test this code: eg run "pytest test_calculator.py" on command-line 
from hello import hello

def test_default():
    assert hello() == "hello, world"
    
def test_argument0():
    assert hello("David") == "hello, David"