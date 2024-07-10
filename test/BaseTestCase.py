import unittest
from os.path import abspath, dirname, join, pardir


class BaseTestCase(unittest.TestCase):
	"""
	A base TestCase class for all classes that implement unit tests in this
	project.
	"""
	# Configure path environment
	PROJECT_ROOT = abspath(
		join(dirname(__file__), pardir)
	)
	TEST_DATA_ROOT = join(PROJECT_ROOT, "test")

	@classmethod
	def _test_path(cls, *paths):
		"""
		:return: An absolute file system path starting at `PROJECT_ROOT`
		and extended with `paths`.
		"""
		return join(cls.TEST_DATA_ROOT, *paths)
