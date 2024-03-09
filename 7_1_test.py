import requests

def get_repo_info(repo_name):
    url = f"https://api.github.com/repos/{repo_name}"
    url2 = "/birthdays?month=april&department=HR"

  
    response = requests.get(url)

  
    if response.status_code == 200:
        data = response.json()
        print(data)
        return {
            "name": data["name"],
            "owner": data["owner"]["login"],
            "description": data.get("description", ""),
            "license": data.get("license", None),
            "created_at": data["created_at"],
        }
    else:
        print(f"Error retrieving information for repository: {repo_name} (Status code: {response.status_code})")
        return None
    
def get_recent_commits(repo_name):
    url = f"https://api.github.com/repos/{repo_name}/commits?per_page=5"

  
    response = requests.get(url)

  
    if response.status_code == 200:
        data = response.json()
        commits = []
        for commit in data:
            commit_info = {
                "message": commit["commit"]["message"],
                "author": commit["commit"]["author"]["name"],
                "sha": commit["sha"],
                "html_url": commit["html_url"],
                "date": commit["commit"]["committer"]["date"],
            }
        commits.append(commit_info)
        return commits
    else:
        print(f"Error retrieving commits for repository: {repo_name} (Status code: {response.status_code})")
        return []
    
repo_info = get_repo_info("myroslava-martyniuk/Milestones")

if repo_info:
  print(f"Repository Name: {repo_info['name']}")
  print(f"Owner: {repo_info['owner']}")
  print(f"Description: {repo_info['description']}")
  license = repo_info.get("license")
  if license:
    print(f"License: {license['name']}")
  print(f"Created at: {repo_info['created_at']}")
else:
  print("Repository not found or error retrieving information.")
print("!!!!!!")
repo_commits = get_recent_commits("myroslava-martyniuk/Milestones")

if repo_commits:
  for commit in repo_commits:
    print(f"Commit Message: {commit['message']}")
    print(f"Author: {commit['author']}")
    print(f"Commit SHA: {commit['sha']}")
    print(f"Commit URL: {commit['html_url']}")
    print(f"Commit Date: {commit['date']}")
    print("-"*20)
else:
  print("Error")
