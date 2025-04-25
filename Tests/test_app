"""Tests the flask app routes"""

from app import *
import unittest


class TestHomepage(unittest.TestCase):
    """Tests the route for the homepage"""
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b"Hello! Welcome to our website with the amazingly" \
    "curated title: Analyzing Criminal Drug Abuse Treatment in Females" \
    "\nAlso known as drug_abuse_treatment.py" \
    "\n" \
    "\n" \
    "Here are the main usages of our program for your research/interests: " \
    '\npython3 app.py --meeting ["frequency", "count"]' \
    '\npython3 app.py --sellArrests lowerBoundCount upperBoundCount' \
    '\n' \
    '\nTo reach the drug sale arrests page, take the path /arrests/lower/upper', response.data)


class TestDrugSaleArrests(unittest.TestCase):
    """Tests the route for drug sale arrests"""
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/arrests/1/10', follow_redirects=True)
        self.assertEqual(b"283 people", response.data)

if __name__ == "__main__":
    unittest.main()