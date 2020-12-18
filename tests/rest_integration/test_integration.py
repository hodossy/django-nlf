from rest_framework.test import APIClient

from ..utils import BaseTestCase


class RestFrameworkIntegrationTestCase(BaseTestCase):
    def setUp(self):
        self.clinet = APIClient()

    def test_filtering_json(self):
        res = self.client.get("/articles/?q=body+contains+NASA")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)

    def test_filtering_html(self):
        res = self.client.get("/articles/?q=body+contains+NASA&format=api")
        self.assertTrue(b'value="body contains NASA"' in res.content)

    def test_no_filtering_html(self):
        res = self.client.get("/articles/?format=api")
        self.assertTrue(b'value=""' in res.content)
