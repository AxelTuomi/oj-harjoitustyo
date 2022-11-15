import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kassan_rahamaara_on_oikein(self):
        self.assertTrue(self.kassa.kassassa_rahaa == 100000)
        self.assertTrue(self.kassa.edulliset == 0)
        self.assertTrue(self.kassa.maukkaat == 0)
