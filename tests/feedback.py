import unittest
import requests

class TestFeedbackService(unittest.TestCase):
	def setUp(self):
		self.host = "http://127.0.0.1"
		
		self.create_feedback = {
			"type": "feedback",
			"firstname": "Никита",
			"lastname": "Бережной",
			"number": "89964177136",
			"email": "nikitoshi@gaspatchi.ru",
			"text": "Test, test, test"
		}
		

		self.create_claim = {
			"type": "driving",
			"firstname": "Никита",
			"lastname": "Бережной",
			"number": "89964177136"
		}

	
	def test_feedback(self):
		result = requests.post("{0}/form/create".format(self.host),json=self.create_feedback)
		body = result.json()
		self.assertEqual(result.status_code,200)
		self.assertIn("id",body)	
	
	def test_claim(self):
		result = requests.post("{0}/form/create".format(self.host),json=self.create_claim)
		body = result.json()
		self.assertEqual(result.status_code,200)
		self.assertIn("id",body)
	
	def test_count(self):
		result = requests.get("{0}/form/count/feedback".format(self.host))
		body = result.json()
		self.assertEqual(result.status_code,200)
		self.assertIn("count",body)

	def test_metrics(self):
		result = requests.get("{0}/form/metrics".format(self.host))
		self.assertEqual(result.status_code,200)
		
class TestInvalideFeedbackService(unittest.TestCase):
	def setUp(self):
		self.host = "http://127.0.0.1"
		
		self.create_feedback = {
			"type": "",
			"firstname": "Никита",
			"lastname": "Бережной",
			"number": "89964177136",
			"email": "nikitoshi@gaspatchi.ru",
			"text": "Test, test, test"
		}
		

		self.create_claim = {
			"type": "driving",
			"firstname": "",
			"lastname": "Бережной",
			"number": "89964177136"
		}

	def test_feedback(self):
		result = requests.post("{0}/form/create".format(self.host),json=self.create_feedback)
		body = result.json()
		self.assertEqual(result.status_code,404)
		self.assertIn("message",body)	
	
	def test_claim(self):
		result = requests.post("{0}/form/create".format(self.host),json=self.create_claim)
		body = result.json()
		self.assertEqual(result.status_code,400)
		self.assertIn("message",body)	
	
	def test_count(self):
		result = requests.get("{0}/form/count/test".format(self.host))
		body = result.json()
		self.assertEqual(result.status_code,404)
		self.assertIn("message",body)