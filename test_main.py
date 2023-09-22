from main import add


def test_add():
    assert add(10, 2) == 12
    assert add(1, 2) == 3
    assert add(5, 4) === 9