from calcpi import gauss_legendre


class TestGaussLegendrePi:
    def test_pi_round12(self):
        actual = gauss_legendre.pi(12)
        expected = 3.1415926535
        assert actual - expected < 1.0e-10
