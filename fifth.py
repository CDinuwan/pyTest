import pytest
@pytest.mark.parametrize("x,y,z",[(10,20,200),(10,40,200)])
def test_method(x,y,z):
    assert x*y==z