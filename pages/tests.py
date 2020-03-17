from django.test import SimpleTestCase

# Create your tests here.


class SimpleTest(SimpleTestCase):
    def homepagetest(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def aboutPagetest(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
