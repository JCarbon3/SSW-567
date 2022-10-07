import unittest

from GitHubAPI import GitHubAPI

class TestAPI(unittest.TestCase):
    def testNoUser(self):
        self.assertEqual(GitHubAPI("JCarbon17"),"Not a valid user")
    
    def testUserExists(self):
        self.assertEqual(GitHubAPI("JCarbon3"),"Repo: 345Course Number of commits: 20\nRepo: Complexity Number of commits: 30\nRepo: CS115 Number of commits: 1\nRepo: SSW-567 Number of commits: 16")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()