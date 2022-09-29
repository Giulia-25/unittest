from assertpy import assert_that, soft_assertions

from mini_calculator import MiniCalculator


def test_sum():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.sum(5, 6)).is_equal_to(11)
        assert_that(mini_calculator.sum(5, 5)).is_equal_to(10)
        assert_that(mini_calculator.sum(0, 0)).is_equal_to(0)
        assert_that(mini_calculator.sum(8, 6)).is_equal_to(14)


def test_diff():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.diff(5, 6)).is_equal_to(-1)
        assert_that(mini_calculator.diff(5, 5)).is_equal_to(0)
        assert_that(mini_calculator.diff(0, 0)).is_equal_to(0)
        assert_that(mini_calculator.diff(8, 0)).is_equal_to(8)
        assert_that(mini_calculator.diff(0, 7)).is_equal_to(-7)
        assert_that(mini_calculator.diff(10, 7)).is_equal_to(3)


def test_produs():
    ...


def test_impartire():
    ...

