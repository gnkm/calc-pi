from calcpi import gauss_legendre


class TestGaussLegendrePi:
    def test_pi_round2(self):
        actual = gauss_legendre.pi(2)
        expected = 3.14
        assert abs(actual - expected) < 0.1
