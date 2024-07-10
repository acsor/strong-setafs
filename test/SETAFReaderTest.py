from src.Attack import Attack
from src.SETAF import SETAF
from src.SETAFReader import SETAFReader
from test.BaseTestCase import BaseTestCase


class SETAFReaderTest(BaseTestCase):
    def _test_path(self, *paths):
        return super()._test_path('SETAFReaderTest', *paths)

    def test_no_zero(self):
        """
        Tests whether reading a file with a line not terminated by a 0
        raises an exception.
        """
        with self.assertRaises(ValueError):
            SETAFReader(
                self._test_path('test_no_zero.ccl')
            )()

    def test_truncated(self):
        """
        Tests whether reading a file with fewer attacks than declared
        on the first lines raises an exception.
        """
        with self.assertRaises(IOError):
            SETAFReader(
                self._test_path('test_truncated.ccl')
            )()

    def test_read_setaf_1(self):
        expected = SETAF(
            (
                Attack((91, ), 113),
                Attack((81, ), 30),
                Attack((127, 80, ), 83),
                Attack((70, ), 124),
                Attack((26, ), 123),
                Attack((11, ), 121),
                Attack((127, 60, ), 83),
                Attack((119, ), 120),
                Attack((127, 71, ), 83),
                Attack((69, 68, ), 119),
                Attack((141, ), 25),
                Attack((81, ), 112),
                Attack((37, ), 111),
                Attack((127, 78, ), 83),
                Attack((18, ), 110),
                Attack((127, 119, ), 83),
                Attack((50, ), 108),
                Attack((103, 127, ), 83),
                Attack((66, ), 6),
                Attack((69, 87, ), 119),
                Attack((105, ), 108),
                Attack((20, 127, ), 83),
                Attack((127, 38, ), 83),
                Attack((78, ), 52),
                Attack((18, 127, ), 83),
                Attack((119, ), 51),
                Attack((90, 127, ), 83),
                Attack((122, ), 50),
                Attack((64, ), 82),
                Attack((136, ), 50),
                Attack((34, ), 82),
                Attack((15, ), 4),
                Attack((108, ), 50),
                Attack((30, ), 81),
                Attack((83, ), 3),
                Attack((50, ), 107),
                Attack((100, ), 80),
                Attack((34, 50, ), 36),
                Attack((126, ), 50),
                Attack((127, 114, ), 83),
                Attack((83, ), 67),
                Attack((82, 43, ), 34),
                Attack((69, 83, ), 119),
                Attack((127, 13, ), 83),
                Attack((26, ), 137),
                Attack((118, 82, ), 34),
                Attack((127, 63, ), 83),
                Attack((105, 82, ), 34),
                Attack((83, ), 25),
                Attack((127, 25, ), 83),
                Attack((2, ), 79),
                Attack((50, ), 136),
                Attack((69, 120, ), 119),
                Attack((11, ), 76),
                Attack((39, ), 135),
                Attack((48, 82, ), 34),
                Attack((115, ), 73),
                Attack((53, ), 25),
                Attack((106, ), 57),
                Attack((83, ), 33),
                Attack((69, 116, ), 119),
                Attack((9, ), 21),
                Attack((79, ), 2),
                Attack((57, ), 106),
                Attack((105, ), 73),
                Attack((43, ), 117),
                Attack((111, ), 21),
                Attack((108, 73, ), 105),
                Attack((31, ), 115),
                Attack((14, ), 115),
                Attack((49, ), 73),
                Attack((81, ), 88),
                Attack((69, 26, ), 119),
                Attack((119, ), 87),
                Attack((6, ), 66),
                Attack((41, ), 86),
                Attack((69, 109, ), 119),
                Attack((127, 89, ), 83),
                Attack((82, ), 65),
                Attack((127, 98, ), 83),
                Attack((73, ), 115),
                Attack((82, ), 64),
                Attack((83, ), 44),
                Attack((24, 73, ), 105),
                Attack((125, ), 63),
                Attack((127, 55, ), 83),
                Attack((110, 88, ), 18),
                Attack((79, ), 62),
                Attack((127, 81, ), 83),
                Attack((8, ), 142),
                Attack((79, 83, ), 58),
                Attack((5, 73, ), 105),
                Attack((50, ), 99),
                Attack((144, ), 17),
                Attack((25, ), 141),
                Attack((108, ), 17),
                Attack((83, ), 104),
                Attack((94, ), 139),
                Attack((36, ), 12),
                Attack((80, 117, ), 43),
                Attack((127, 79, ), 83),
                Attack((39, ), 10),
                Attack((59, 80, ), 43),
                Attack((135, ), 39),
                Attack((73, 40, ), 95),
                Attack((10, ), 39),
                Attack((47, 73, ), 95),
                Attack((135, ), 138),
                Attack((111, ), 37),
                Attack((68, ), 94),
                Attack((11, ), 32),
                Attack((84, ), 27),
                Attack((127, 8, ), 83),
                Attack((95, ), 94),
                Attack((83, ), 42),
                Attack((11, ), 135),
                Attack((75, ), 32),
                Attack((69, 22, ), 119),
                Attack((94, ), 132),
                Attack((73, ), 93),
                Attack((25, ), 102),
                Attack((41, ), 56),
                Attack((93, ), 131),
                Attack((50, ), 16),
                Attack((127, 129, ), 83),
                Attack((11, ), 128),
                Attack((96, ), 127),
                Attack((142, ), 8),
                Attack((86, ), 41),
                Attack((85, ), 41),
                Attack((24, ), 27),
                Attack((7, ), 8),
                Attack((115, ), 14),
                Attack((88, ), 113),
                Attack((127, 130, ), 83),
                Attack((8, ), 7),
                Attack((115, ), 31),
            )
        )
        actual = SETAFReader(
            self._test_path('test_read_setaf_1.ccl')
        )()

        self.assertEqual(
            expected, actual
        )