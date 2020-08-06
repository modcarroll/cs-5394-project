import unittest
from unittest.mock import patch, Mock
import requests
import json
import main

allUsers = []
allLogs = []
url = "https://pycontrolapi.us-south.cf.appdomain.cloud"

class TestFunctions(unittest.TestCase):

	mock = Mock()

	@patch('main._populateUsers')
	def test_populateUsers(self, mock_populateUsers):
		main._populateUsers()
		self.assertIsNotNone(allUsers)
		print("testing _populateUsers")

	@patch('main._populateLogsTab')
	def test_populateLogsTab(self, mock_populateLogsTab):
		main._populateLogsTab()
		self.assertIsNotNone(allLogs)
		print("testing _populateLogsTab")

	@patch('requests.post')
	def test_postToLog(self, mock_post):
		data = {"name": "carla", "device": "speaker", "action": "turn-on"}
		req = requests.post(url + "/logs", data = json.dumps(data))
		mock_post.assert_called_with(url + "/logs", data = json.dumps(data))
		print("testing post method")

	def test_get(self):
		r = requests.get(url + "/allLogs")
		if r.status_code == 200:
			print("success")
		elif r.status_code == 404:
			print("failure")


if __name__ == '__main__': 
	unittest.main()
