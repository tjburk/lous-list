from django.test import TestCase

class testcases(TestCase):
    def test_call_view(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'lous_list/index.html')