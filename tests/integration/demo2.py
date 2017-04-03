import unittest
import urllib2
from flask import Flask
from flask.ext.testing import TestCase 
import time

# Testing with LiveServer
class MyTest(TestCase):
  # if the create_app is not implemented NotImplementedError will be raised
  def create_app(self):
    app = Flask(__name__)
    app.config['TESTING'] = True
    self.baseURL = "http://localhost:5000"
    return app 

  def test_flask_application_is_up_and_running(self):
      response = urllib2.urlopen(self.baseURL)
      time.sleep(5)
      self.assertEqual(response.code, 200) 

if __name__ == "__main__":

  unittest.main()
