import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassan_saldo_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaatteen_myytyjen_lounaiden_maara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_toimii_oikein_jos_rahaa_riittaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_toimii_oikein_jos_rahaa_ei_riitä(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_toimii_oikein_jos_rahaa_riittaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kateisella_toimii_oikein_jos_rahaa_ei_riitä(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_toimii_oikein_jos_rahaa_riittää(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(onnistui, True)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla_toimii_oikein_jos_rahaa_ei_riitä(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistui, False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_toimii_oikein_jos_rahaa_riittää(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(onnistui, True)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_toimii_oikein_jos_rahaa_ei_riitä(self):
        kortti = Maksukortti(300)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistui, False)
        self.assertEqual(kortti.saldo, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_rahaa_kortille_toimii_oikein_positiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_lataa_rahaa_kortille_ei_toimi_jos_summa_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina_toimii_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
