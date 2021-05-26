import textwrap

from mpmath import (
    mp,
    mpf,
 )

from calcpi import utils


class TestUtils:

    def test_format_not_separated(self):
        mp.dps = 30
        num_mpf = mpf('0.1234567890123456789')
        actual = utils.format_pi(num_mpf, accuracy=20)
        expected = textwrap.dedent('''\
        0.1234567890123456789\
        ''').strip(' ')
        assert actual == expected

    def test_format_separated(self):
        mp.dps = 30
        num_mpf = mpf('0.1234567890123456789')
        actual = utils.format_pi(num_mpf, accuracy=20, is_separated=True, grouped_digit=5)
        expected = textwrap.dedent('''\
        0.
        12345 67890 12345 6789\
        ''').strip(' ')
        assert actual == expected
