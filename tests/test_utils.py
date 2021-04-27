from calcpi import utils


class TestUtils:
    def test_one(self):
        actual = utils.round(1.234, 1)
        expected = 1.2
        assert actual == expected
