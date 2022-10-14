import requests
import json



def GitHubAPI(userID):
    final_message = ""
    repos = (requests.get('https://api.github.com/users/' + userID +'/repos')).json()
    if type(repos) == dict:
        if 'message' in repos:
            if repos['message'] == "Not Found":
                return("Not a valid user")
    items_left_in_repos = len(repos)
    for item in repos:
        item_name = item['name']
        commit_info = (requests.get('https://api.github.com/repos/'+ userID +'/'+ item_name + '/commits')).json()
        commits = 0
        for commit in commit_info:
            commits += 1
        final_message += "Repo: " + item_name + " Number of commits: " + str(commits)
        items_left_in_repos -=  1
        if items_left_in_repos > 0:
            final_message += "\n"
    return(final_message)