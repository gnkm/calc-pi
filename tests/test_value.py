from calcpi import value


class TestSimplePi:
    def test_pi_round2(self):
        actual = value.pi(2)
        expected = 3.14
        assert actual == expected
