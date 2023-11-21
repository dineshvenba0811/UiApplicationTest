from django.test import TestCase
from django.urls import reverse
# Create your tests here.
#test cases are moidifed.
class MyViewTestCase(TestCase):
    def test_view_returns_items(self):
        # Get the URL for your view (replace 'your_view_name' with the actual view name or URL pattern)
        url = reverse('index')

        # Make a request to the view
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)