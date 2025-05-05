"""Tests the flask app routes"""


import unittest
from app import app



class TestHomepage(unittest.TestCase):
    """Tests the homepage route"""

    def setUp(self):
        """Sets up the test client"""

        self.app = app.test_client()


    def test_homepage(self):
        """Test for route for the homepage"""

        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b'Hello! Welcome to our website with the amazingly' \
    b'curated title: Analyzing Criminal Drug Abuse Treatment in Females' \
    b'\nAlso known as drug_abuse_treatment.py' \
    b'\n' \
    b'\n' \
    b'Here are the main usages of our program for your research/interests: ' \
    b'\npython3 app.py --meeting ["frequency", "count"]' \
    b'\npython3 app.py --sellArrests lowerBoundCount upperBoundCount' \
    b'\n' \
    b'\nTo reach the drug sale arrests page, take the path /arrests/lower/upper', response.data)


class TestDrugSaleArrests(unittest.TestCase):
    """Tests the drug sale arrests route"""

    def setUp(self):
        """Sets up the test client"""

        self.app = app.test_client()


    def test_drug_sale(self):
        """Test for route for drug sale arrests"""

        response = self.app.get('/arrests/1/10', follow_redirects=True)
        self.assertEqual(b"283 people", response.data)


if __name__ == "__main__":
    unittest.main()
