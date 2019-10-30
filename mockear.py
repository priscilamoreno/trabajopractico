import sut
import unittest
from unittest.mock import MagicMock

class TestBase(unittest.TestCase):
  def test_costo_total(self):
    sut.sumar=MagicMock(return_value=2)
    a=sut.costototal(5,4)
if __name__=="__main__":
  unittest.main()