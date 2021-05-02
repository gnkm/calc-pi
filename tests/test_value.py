from calcpi import value
import mpmath


class TestValuePi:
    def test_pi_accuracy3(self):
        actual = mpmath.nstr(value.pi(3), 3)
        expected = mpmath.nstr(
            mpmath.mpf('3.14'), 3
        )
        assert actual == expected

    def test_pi_accuracy21(self):
        accuracy = 21
        actual = mpmath.nstr(value.pi(accuracy), accuracy)
        expected = mpmath.nstr(
            mpmath.mpf('3.14159265358979323846'), accuracy
        )
        assert actual == expected
