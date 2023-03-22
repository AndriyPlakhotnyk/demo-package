

from andriy.functions import hello_world


def test__hello_world():
    actual = hello_world()
    expected = 'Hello world!'

    assert expected == actual, f'hello_world() returned {actual} instead of {expected}'

