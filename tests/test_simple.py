from calcpi import simple


class TestSimplePi:
    def test_pi_round2(self):
        actual = simple.pi(2)
        expected = 3.14
        assert actual == expected
