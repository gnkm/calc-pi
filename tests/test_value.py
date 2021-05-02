from calcpi import value
import mpmath


class TestSimplePi:
    def test_pi_round2(self):
        actual = mpmath.nstr(value.pi(3), 3)
        expected = mpmath.nstr(
            mpmath.mpf('3.14'), 3
        )
        assert actual == expected
