import requests
from datetime import date, timedelta


def get_trending_repositories(top_size):
    boundary_date = date.today() - timedelta(days=7)
    github_url = "https://api.github.com/search/repositories"
    search_params = {
        'q': 'created:>{}'.format(boundary_date),
        'page': '1',
        'per_page': top_size,
        'sort': 'stars',
        'order': 'desc'
    }
    response = requests.get(github_url, search_params)
    repos_list = response.json()['items']

    return repos_list


def get_open_issues_amount(repo_owner, repo_name):
    github_issues_url = "https://api.github.com/repos/{owner}/{repo}/issues"\
                         .format(owner=repo_owner, repo=repo_name)

    response = requests.get(github_issues_url)

    return len(response.json())


if __name__ == '__main__':

    top_size = 20
    trending_repositories = get_trending_repositories(top_size)
    for repo in trending_repositories:
        repo_open_issues = get_open_issues_amount(repo['owner']['login'],
                                                  repo['name'])
        print('-------------------------------------')
        print("Repository owner: {owner}\nRepository name: {name}\nURL: {repo_url}"
              "\nOpen issues: {issues}"
            .format(owner=repo['owner']['login'],
                    name=repo['name'],
                    repo_url=repo['owner']['html_url']+'/'+repo['name'],
                    issues=repo_open_issues))
