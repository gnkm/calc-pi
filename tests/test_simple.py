from calcpi import simple


class TestSimplePi:
    def test_pi_one(self):
        actual = simple.pi()
        expected = 3.14
        assert actual >= expected
