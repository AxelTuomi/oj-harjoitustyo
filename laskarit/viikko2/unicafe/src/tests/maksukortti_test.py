import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortin_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(25)
        self.assertEqual(str(self.maksukortti), "saldo: 0.35")

    def test_kortin_saldo_vahenee_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_kortin_saldo_ei_muutu_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(0)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortin_ota_rahaa_metodi_plautta_true_jos_riitavasti_rahaa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))

    def test_kortin_ota_rahaa_metodi_plautta_false_jos_ei_ole_riitavasti_rahaa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(13))
