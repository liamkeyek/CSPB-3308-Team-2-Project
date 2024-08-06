import unittest
from project import app
from datetime import datetime

"""
Testing Framework for Home Page:
This provides the unit tests for the home page functionality.
Test Cases:
- Verifies home page loads successfully (status code 200)
- Checks for presence of expected content
- Ensures current month and year are displayed correctly
Features Tested:
- Basic page loading
- Content rendering
- Date display accuracy
Test Setup:
- Uses Python's unittest module
- Creates a test client from the Flask app

Last updated: Liam Keyek 8/6/2024
"""
class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        response = self.app.get('/home')
        
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.app.get('/home')
        
        self.assertIn(b'Welcome to Your Calendar', response.data)

    def test_current_month_year(self):
        response = self.app.get('/home')
        
        current_date = datetime.now()
        current_month = current_date.strftime('%B')  # Full month name
        current_year = str(current_date.year)
        
        self.assertIn(current_month.encode(), response.data)
        self.assertIn(current_year.encode(), response.data)

if __name__ == '__main__':
    unittest.main()