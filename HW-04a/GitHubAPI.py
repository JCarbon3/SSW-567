import requests
import json



def GitHubAPI(userID):
    repos = (requests.get('https://api.github.com/users/' + userID +'/repos')).json()
    for item in repos:
        item_name = item['name']
        commit_info = (requests.get('https://api.github.com/repos/'+ userID +'/'+ item_name + '/commits')).json()
        commits = 0
        for commit in commit_info:
            commits += 1
        print("Repo: " + item_name + " Number of commits: " + str(commits))


GitHubAPI('JCarbon3')