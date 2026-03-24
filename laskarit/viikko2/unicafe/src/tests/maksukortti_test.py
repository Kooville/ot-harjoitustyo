import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_kortti_latautuu_oikein(self):
        self.maksukortti.lataa_rahaa(250)
        self.assertEqual(self.maksukortti.saldo_euroina(), 12.5)

    def test_kortilta_otto_toimii_oikein(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.5)

    def test_kortilta_otto_ei_toimi_jos_rahaa_ei_riita(self):
        self.maksukortti.ota_rahaa(1050)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_otto_palauttaa_true_jos_rahaa_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(250), True)

    def test_rahan_otto_palauttaa_false_jos_rahaa_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1050), False)

    def test_str_palauttaa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
