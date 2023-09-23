from main import add_func


def test_add():
    assert add_func(1) == 4
    assert add_func(2) == 5
    assert add_func(3) == 6