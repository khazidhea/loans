import pytest
from core.foobar import foobar, positive, division


@pytest.mark.parametrize(
    "test_input, expected",
    [(1, '1'), (2, '2'), (3, 'Foo'), (4, '4'), (5, 'Bar'), (15, 'FooBar')]
)
def test_foobar_ok(test_input, expected):
    assert foobar(test_input) == expected


def test_division_ok():
    assert division(4, 2) == 2


def test_division_exception():
    with pytest.raises(ZeroDivisionError):
        division(2, 0)


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ([-1, 0, 1], [1]), ([1], [1]),
        ([0], []), ([-1], []),
        ([1, 2], [1, 2]), ([1, -2], [1])
    ]
)
def test_positive(test_input,  expected):
    assert positive(test_input) == expected

