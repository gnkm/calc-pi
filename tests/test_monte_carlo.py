from calcpi.algorithms import monte_carlo


class TestMonteCarloPi:
    def test_pi_round_100_000(self):
        actual = monte_carlo.pi(100_000)
        expected = 3.1415926535
        assert abs(actual - expected) < 0.1
