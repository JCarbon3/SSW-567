import unittest
from unittest import mock
import json

class FakeResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

switcher = {
    'https://api.github.com/users/JCarbon3/repos': 'JCarbon3_Info.json',
    'https://api.github.com/users/JCarbon17/repos': 'InvalidUser.json',
    'https://api.github.com/repos/JCarbon3/SSW-567/commits': 'SSW-567_Info.json'   
}

def mocked_requests_get(*args):
    if args[0] in switcher:
        with open(switcher[args[0]]) as f:
            return FakeResponse(json.load(f))
    return FakeResponse(None)


from GitHubAPI import GitHubAPI

class TestAPI(unittest.TestCase):


    @mock.patch('requests.get', side_effect = mocked_requests_get)
    def testNoUser(self, mock_get):
        self.assertEqual(GitHubAPI("JCarbon17"),"Not a valid user")
    
    @mock.patch('requests.get', side_effect = mocked_requests_get)
    def testUserExists(self, mock_get):
        self.assertEqual(GitHubAPI("JCarbon3"),"Repo: SSW-567 Number of commits: 22")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()