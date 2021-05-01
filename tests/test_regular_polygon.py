from calcpi import regular_polygon


class TestRegularPolygonPi:
    def test_pi_accuracy6(self):
        actual = regular_polygon.pi(6)
        expected = 3
        assert actual - expected < 0.1

    def test_pi_accuracy7(self):
        actual = regular_polygon.pi(7)
        expected = 3
        assert actual > expected
