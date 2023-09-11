

def test_negative():
    assert squared(-2) == 4
    assert squared(-3) == 9

def test_zero():
    assert squared(0) == 0

def test_str():
    with pytest.raises(TypeError):
        squared("cat")
"""
from SProject24 import rand_n

def test_rand_n():
    assert rand_n(2) == 4
    assert rand_n(3) == 9