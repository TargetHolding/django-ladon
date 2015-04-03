from django.test import TestCase, Client

class ExampleTestCase(TestCase):

    def test_jsonrpc10(self):
        """We can add two numbers via the calculator webservice"""
        client = Client()
        response = client.post('/api/calculator/jsonrpc10', 
                               '{"method": "add", "params": [1,2], "id": "1"}', content_type='text/json')
        self.assertJSONEqual(response.content.decode(), 
                             '{"id": "1", "error": null, "result": 3}')


