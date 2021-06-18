from calcpi.algorithms import regular_polygon


class TestRegularPolygonPi:
    def test_pi_accuracy4(self):
        actual = regular_polygon.pi(4)
        expected = 2 * 1.41421356
        assert actual - expected < 0.1

    def test_pi_accuracy6(self):
        actual = regular_polygon.pi(6)
        expected = 3
        assert actual == expected
