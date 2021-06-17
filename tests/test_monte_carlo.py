from calcpi import monte_carlo


class TestMonteCarloPi:
    def test_pi_round12(self):
        actual = monte_carlo.pi(12)
        expected = 3.1415926535
        assert actual - expected < 1.0e-10
