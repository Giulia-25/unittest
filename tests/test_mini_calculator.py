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
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.produs(5, 6)).is_equal_to(30)
        assert_that(mini_calculator.produs(6, 6)).is_equal_to(36)
        assert_that(mini_calculator.produs(3000000000, 0)).is_equal_to(0)


def test_impartire():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.impartire(6, 6)).is_equal_to(1)
        assert_that(mini_calculator.impartire(6, 2)).is_equal_to(3)
        assert_that(mini_calculator.impartire(6000000000, 6)).is_equal_to(1000000000)
        assert_that(mini_calculator.impartire(1, 2)).is_equal_to(0.5)
        assert_that(mini_calculator.impartire(1, 0)).is_equal_to("Nu se poate imparti la 0")
