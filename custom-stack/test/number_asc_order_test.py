import random

import pytest

from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder


@pytest.fixture
def cut():
    return NumberAscOrder()


@pytest.fixture
def stack_mock(mocker):
    # Mock da CustomStack: o spec garante que so a API existente seja usada
    # e que isinstance(mock, CustomStack) seja verdadeiro.
    mock = mocker.Mock(spec=CustomStack)
    mock.limit = 6
    return mock


def test_sort_stack_with_six_drawn_numbers(cut, stack_mock):
    drawn_numbers = random.sample(range(1, 61), 6)
    stack_mock.size.return_value = 6
    # is_empty: False 6 vezes (um por numero) e True para encerrar o laco
    stack_mock.is_empty.side_effect = [False] * 6 + [True]
    # pop devolve na ordem inversa do sorteio (LIFO)
    stack_mock.pop.side_effect = list(reversed(drawn_numbers))

    result = cut.sort(stack_mock)

    assert result == sorted(drawn_numbers)
    assert isinstance(result, list)
    assert len(result) == 6
    assert stack_mock.pop.call_count == 6
    assert stack_mock.is_empty.call_count == 7
    stack_mock.push.assert_not_called()


def test_sort_stack_with_six_fixed_numbers(cut, stack_mock):
    stack_mock.is_empty.side_effect = [False] * 6 + [True]
    stack_mock.pop.side_effect = [42, 7, 59, 13, 1, 30]

    assert cut.sort(stack_mock) == [1, 7, 13, 30, 42, 59]


def test_sort_empty_stack_with_six_positions(cut, stack_mock):
    stack_mock.size.return_value = 0
    stack_mock.is_empty.return_value = True

    result = cut.sort(stack_mock)

    assert result == []
    stack_mock.is_empty.assert_called_once()
    stack_mock.pop.assert_not_called()


def test_sort_none_raises_value_error(cut):
    with pytest.raises(ValueError):
        cut.sort(None)


def test_sort_invalid_type_raises_type_error(cut):
    with pytest.raises(TypeError):
        cut.sort([10, 20, 30])


@pytest.mark.parametrize("invalid_value", ["10", 3.5, True, None])
def test_sort_stack_with_non_integer_raises_type_error(cut, stack_mock, invalid_value):
    stack_mock.is_empty.side_effect = [False, False, True]
    stack_mock.pop.side_effect = [10, invalid_value]

    with pytest.raises(TypeError):
        cut.sort(stack_mock)


def test_sort_with_real_custom_stack(cut):
    stack = CustomStack(6)
    drawn_numbers = random.sample(range(1, 61), 6)
    for number in drawn_numbers:
        stack.push(number)

    assert cut.sort(stack) == sorted(drawn_numbers)
