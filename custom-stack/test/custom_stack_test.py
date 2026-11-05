import pytest

from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


@pytest.fixture
def cut():
    return CustomStack(5)


def test_new_stack_is_empty(cut):
    assert cut.is_empty() is True
    assert cut.size() == 0
    assert cut.limit == 5


def test_push_one_elementinstack(cut):
    element_value = 5.0

    cut.push(element_value)

    assert cut.is_empty() is False
    assert cut.top() == element_value
    assert cut.size() == 1


def test_push_many_elements_keeps_lifo_order(cut):
    for value in [1, 2, 3]:
        cut.push(value)

    assert cut.size() == 3
    assert cut.top() == 3
    assert cut.pop() == 3
    assert cut.pop() == 2
    assert cut.pop() == 1
    assert cut.is_empty() is True


def test_push_until_limit(cut):
    for value in range(5):
        cut.push(value)

    assert cut.size() == cut.limit
    assert cut.top() == 4


def test_push_on_full_stack_raises_exception(cut):
    for value in range(5):
        cut.push(value)

    with pytest.raises(StackFullException):
        cut.push(99)

    assert cut.size() == 5
    assert cut.top() == 4


def test_pop_returns_and_removes_top_element(cut):
    cut.push("a")
    cut.push("b")

    assert cut.pop() == "b"
    assert cut.size() == 1
    assert cut.top() == "a"


def test_pop_on_empty_stack_raises_exception(cut):
    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_does_not_remove_element(cut):
    cut.push(10)

    assert cut.top() == 10
    assert cut.top() == 10
    assert cut.size() == 1


def test_top_on_empty_stack_raises_exception(cut):
    with pytest.raises(StackEmptyException):
        cut.top()


def test_pop_after_emptying_stack_raises_exception(cut):
    cut.push(1)
    cut.pop()

    with pytest.raises(StackEmptyException):
        cut.pop()
