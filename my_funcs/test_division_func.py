from my_funcs.utils import division, multi
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5), (20, 10, 2), (30, -3, -10), (5, 2, 2.5)])
def test_division_positive(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, divider, div", [(ZeroDivisionError, 0, 10), (TypeError, "2", 20)])
def test_division_error(expected_exception, divider, div):
    with pytest.raises(expected_exception):
        division(div, divider)

@pytest.mark.parametrize("a, b, expected_result", [(5, 10, 50), (5, 5, 25), (2, -10, -20), (4, 0, 0)])
def test_multi_positive(a, b, expected_result):
    assert multi(a, b) == expected_result



