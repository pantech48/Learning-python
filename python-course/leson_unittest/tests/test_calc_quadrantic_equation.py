import pytest
from project import calc_quadrantic_equation


def test_no_solution():
    result = calc_quadrantic_equation(1, 0, 1)
    assert result is None, "Корней быть не должно!"

@pytest.mark.parametrize('args,expected',(
    ((1, 2, 1), -1),
    ((1, 4, 4), -2)
))
def test_one_root(args, expected):
    result = calc_quadrantic_equation(*args)
    assert result == expected, 'Корень должен быть один.'

@pytest.mark.parametrize('args,expected',(
    ((1, 4, 3), (-3, -1)),
    ((3, -12), (0, 4))
))
def test_two_roots(args, expected):
    result = calc_quadrantic_equation(*args)
    assert sorted(result) == sorted(expected), 'Корней должно быть два.'