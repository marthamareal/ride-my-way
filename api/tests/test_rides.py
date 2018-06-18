
import unittest

from app import app


class APITestRideCase(unittest.TestCase):

    def setUp(self):
        # create test client
        self.test_client = app.test_client()
        pass

    def test_get_rides(self):
        # get expected response
        response = self.test_client.get('/api/v1/rides')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
