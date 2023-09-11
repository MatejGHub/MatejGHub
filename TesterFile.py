"""
from SProject24 import squared

def main():
    test_Squared()

def test_Squared():
    try:
        assert squared(2) == 4
    except AssertionError:
        print("2 quared was not 4")
    try: 
        assert squared(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert squared(-2) == 4
    except AssertionError:
        print("-2 quared was not 4")
    try:
        assert squared(0) == 0
    except AssertionError:
        print("0 quared was not 0")

if __name__ == "__main__":
    main()
"""
#newtest
"""
import pytest
from SProject24 import squared

def test_positive():
    assert squared(2) == 4
    assert squared(3) == 9

def test_negative():
    assert squared(-2) == 4
    assert squared(-3) == 9

def test_zero():
    assert squared(0) == 0

def test_str():
    with pytest.raises(TypeError):
        squared("cat")
"""
#newtest2
"""
from SProject24 import rand_n

def test_rand_n():
    assert rand_n(2) == 4
    assert rand_n(3) == 9
    assert rand_n(-4) == 16
"""
#newtask3
from SProject24 import hello

def test_hello():
    assert hello("David") == "Hello, David"
    assert hello() == "Hello, world"