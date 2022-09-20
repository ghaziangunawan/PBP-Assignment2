from django.test import TestCase, Client


class watchlistTest(TestCase):
    def test_url_exist(self):
        resp = self.client.get('/mywatchlist/')
        self.assertEqual(resp.status_code, 200)

    def test_json_exist(self):
        resp = self.client.get('/mywatchlist/json/')
        self.assertEqual(resp.status_code, 200)

    def test_xml_exist(self):
        resp = self.client.get('/mywatchlist/xml/')
        self.assertEqual(resp.status_code, 200)

    
